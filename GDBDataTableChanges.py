# Process runs through a file gdb & compares tables & field values with another gdb for adds, deletes, & updates.
# Reports where changes are made before import. Once confirmed with updates, script continues &
# updates destination gdb with edits from origin gdb
# Created 8/25/2016
print('loading time package...')
import logging
from time import time as _timetime_
import datetime
start_time = _timetime_()
print('loading arcpy da modules...')
import arcpy
print('Load time of da arcpy module took {0} seconds'.format(_timetime_() - start_time))

# Modules for ArcFM editing:
import os, logging, getpass
from win32com.client import Dispatch
import win32api

# Must copy \\p\files2\Downloads\Python Packages\ArcFM\enumerations.py to C:\Python27\ArcGIS10.2\Lib for this to work
# Added packages "win32", "win32com" & "win32comext" to "..\Python27\ArcGIS10.2\Lib\site-packages" folder
from enumerations import mmRuntimeMode, mmLicensedProductCode, mmAutoUpdaterMode  # contains enumeration constants for working with MMAppInitialize and MMAutoUpdater classes

#import Tkinter

# Global Variables

#tk_wrapper = Tkinter.Tk()
print('loading TableChanges class')
# Class for creating an object for each table for comparing, updating, deleting, & adding features between 2 databases.
class TableChanges(object):

    # Class variable dictionaries shared by all instances of TableChanges class.
    # For each class instance of a table, dictionaries will hold key:values of idfield:(tuple of sourcefieldname1, sourcefieldvalue1, destfieldname1, destfieldvalue1, sourcefieldname2, sourcefieldvalue2, destfieldname2, destfieldvalue2...etc). until all fields in field list are recorded as added, deleted, or updated.
    addsDict = {}
    addsCompletedDict = {}
    deletesDict = {}
    potentialUpdatesDict = {}
    updatesCompletedDict = {}
    photoGlobalsDict = {}

    def __init__(self, tablename, sourcetablepath, desttablepath, sourcefieldlist, destfieldlist, sdeConnection):
        """
        :param tablename: (string) Keyword for referencing the table in both source & destination tables.
        :param sourcetablepath: (string) Full filepath to source table; this is the table from which you will pull records
        :param desttablepath: (string) Full filepath to destination table; this is the table to which you will put records.
        :param sourcefieldlist: (list) List of field names in double quotes "" in sourcetablepath in same exact order as destfieldlist. [0] should be the ID field and [1] should be the last modified date field.
        :param destfieldlist: (list) List of field names in double quotes "" in desttablepath in same exact order as sourcefieldlist. [0] should be the ID field and [1] should be the last modified date field.
        :param sdeConnection: (string) file path to SDE database connection for updating the SDE database table.
        """
        self.tablename = tablename
        self.sourcetablepath = sourcetablepath
        self.desttablepath = desttablepath
        self.sourcefieldlist = sourcefieldlist
        self.destfieldlist = destfieldlist
        self.sdeConnection = sdeConnection

    def findUpdatedRecords(self, distancethreshold=10): #, excludeuserlist=None):
        """
        :param:
        This script finds all updated records in the source file feature class when it compares it to the SDE record.
        Learn more about editing geometry: https://boxshapedworld.wordpress.com/tutorials/arcpy-cursors-and-geometry/
        NOT AN OPTION--> (b/c this only compares # records, spatial reference, subtypes, but not geometry or field values)Try the FeatureCompare_management() tool to check if geometry is different for all features: THIS WON'T WORK SINCE YOU CAN ONLY USE A SORT FIELD TO MATCH RECORDS. SINCE WE HAVE A SUBSET OF DATA IN THE "SOURCE" FEATURE CLASS, THE SORT OPTION WON'T WORK TO MATCH FEATURES.https://pro.arcgis.com/en/pro-app/tool-reference/data-management/feature-compare.htm; coordinate system must match!!!

        Checks if the geometry SHAPE feature rounded is the same to so many decimal places. If not, then replace the changed location to the updatedRow

        :return:
        """

        print('Finding updated records...')
        start_time = _timetime_()
        desttable_dict = {}
        sourcetable_dict = {}

        # logging
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger("SearchCursor")

        # create a file handler
        handler = logging.FileHandler('VersionedSDEDataSearchCursor.log')
        handler.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)

        # start logging
        logger.info('Checking for Updated Records in Versioned SDE data with Search Cursor')

        ##================================================================================================##
        ##=================Creating Dictionaries of Destination & Source Tables to compare equality=======##
        ##================================================================================================##

        with arcpy.da.SearchCursor(self.desttablepath, self.destfieldlist) as destCursor:
            # Create desttable dictionary of fields & data
            for destrow in destCursor:
                # Add destrow values list as value to ID key
                desttable_dict[destrow[0]] = destrow
        del destCursor
        # print('desttable_dict: {0}'.format(desttable_dict))

        with arcpy.da.SearchCursor(self.sourcetablepath, self.sourcefieldlist) as sourceCursor:
            # Create sourcetable dictionary of fields & data
            for sourcerow in sourceCursor:
                # Add sourcerow values list as the value to the ID key
                sourcetable_dict[sourcerow[0]] = sourcerow
        del sourceCursor

        # ===============================================================================#
        # TESTING ONLY A FEW UPDATE RECORDS & THEN SAVING TO SEE IF UPDATES ARE COMPLETED
        # REMOVE INDENT & FOR-LOOP WHEN DONE TESTING
        # ===============================================================================#
        # x = 0                                           # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
        # breakvalue = 50                                 # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
        # while x <= 50:                                  # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
        #     print("---\n----X: {0}----\n".format(x))    # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
        #     if x == breakvalue: break                   # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#

        # Check if dictionary key & values are the same
        for sourcekey, sourceval in sourcetable_dict.iteritems():
            # if x == breakvalue: break             # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#

            ##============== CHECKING DATE COMPARISONS HERE==============================##
            # Checking if values in rows have lastmodified date before file gdb's date
            # print("str(sourcetable_dict[sourcekey][1]): {0} > (str(desttable_dict[sourcekey][1]): {1}".format(str(sourcetable_dict[sourcekey][1]), (str(desttable_dict[sourcekey][1]))))
            if (sourcekey in desttable_dict): #and (str(sourcetable_dict[sourcekey][1]) > (str(desttable_dict[sourcekey][1]))):
                # if (excludeuserlist is not None) and (sourcetable_dict[sourcekey][2] not in excludeuserlist):

                # Set up search cursor to search through source table
                whereclause = self.sourcefieldlist[0] + " = " + str(sourcekey)
                # whereclause = 'ServerOID = ' + str(sourcekey) # + ' AND ' + self.sourcefieldlist[1] + " < TO_DATE('" + checkdate + "', 'YYYY-MM-DD HH24:MI:SS')"

                print whereclause

                with arcpy.da.SearchCursor(self.sourcetablepath, self.sourcefieldlist, whereclause) as searchcur:
                    for fromgdb_search_row in searchcur:
                        # if x == breakvalue: break       # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
                        # x += 1                          # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#

                        i = 3  # Setting counter to 3 to skip over the OID, DATEMODIFIED, & LASTUSER fields.
                        print("i = {0}; ID = {1}".format(i, sourcekey))

                        # If-else condition that checks if "SHAPE" is in the field list & the value is a tuple.
                        if self.sourcefieldlist[i] == "SHAPE@XY" and type(fromgdb_search_row[i]) is tuple:
                            # print type(fromgdb_search_row[i])
                            distance_difference = " < " + str(distancethreshold)

                            # Checking if SHAPE@XY tuple values of X & Y's are within 1 foot of each other. When tested using 1/10 of a foot, the changed points were basically the same. Therefore, only those points that were different by within 1 foot were considered points were legitimate location updates.
                            # if (round(fromgdb_search_row[i][0], 0) != round(desttable_dict[sourcekey][i], 0)) or (
                            #             round(fromgdb_search_row[i][1], 0) != round(desttable_dict[sourcekey][i][1], 0)):

                            # Checking a tolerance of difference in distance between source & dest locations
                            source_x = fromgdb_search_row[i][0]
                            source_y = fromgdb_search_row[i][1]
                            dest_x = desttable_dict[sourcekey][i][0]
                            dest_y = desttable_dict[sourcekey][i][1]
                            distance_difference = ((source_x - dest_x) ** 2 + (source_y - dest_y) ** 2) ** 0.5

                            if distance_difference > distancethreshold:
                                logger.info("From rounded XY: {0},{1}; SDE's rounded XY: {2},{3}".format(
                                    round(fromgdb_search_row[i][0], 0),
                                    round(fromgdb_search_row[i][1], 0),
                                    round(desttable_dict[sourcekey][i][0], 0),
                                    round(desttable_dict[sourcekey][i][1], 0)))

                            else:
                                i += 1  # Script continues by incrementing to next field after the tuple "SHAPE@XY" if there is no update in location. This will also check lastmodified or datemodified date, but when saving edits, the date field will still be changed to today's date upon saving edits. Storing the dates is for documentation purposes.

                            while i < len(self.sourcefieldlist):
                                print("i: {0}".format(i))

                                # Checks if sourcetable value in each field is different from desttable value for that same field. Read as "if source fieldvalue NOT EQUAL to dest field value: run this"
                                # print("fromgdb_search_row[i]: {0}; desttable_dict[sourcekey][i]: {1}".format(fromgdb_search_row[i], desttable_dict[sourcekey][i]))

                                if fromgdb_search_row[i] != desttable_dict[sourcekey][i]:
                                    # Check where id fields match in sourcetable & desttable
                                    print('Found update in: (source: {0}; dest: {1}).'.format(fromgdb_search_row[i],
                                                                                              desttable_dict[sourcekey][i]))
                                    whereclause = self.destfieldlist[0] + " = " + str(sourcekey)
                                    # whereclause = 'OBJECTID = ' + str(sourcekey)  # + ' AND ' + self.sourcefieldlist[1] + " < TO_DATE('" + checkdate + "', 'YYYY-MM-DD HH24:MI:SS')"
                                    print(whereclause)

                                    # Set up Update Cursor in SDE table for that ID
                                    with arcpy.da.SearchCursor(self.desttablepath, self.destfieldlist, whereclause) as togdb_searchcur:
                                        logger.info("\nLooking for ID: {0}".format(whereclause))
                                        for togdb_update_row in togdb_searchcur:

                                            # Iterating through field list where values equal
                                            # Print data values BEFORE change
                                            logger.info("**UPDATING - ID: {0} updated from SDE's {1}:{2} to GDB's values {3}:{4}".format(sourcekey, self.destfieldlist[i], togdb_update_row[i],self.sourcefieldlist[i], fromgdb_search_row[i]))

                                            # A list is created for each change made in SDE; then the list is appended to the dictionary key ID
                                            updatesvaluelist = ['SourceTable->', self.sourcefieldlist[i],
                                                                fromgdb_search_row[i], 'DestTable->',
                                                                self.destfieldlist[i], desttable_dict[sourcekey][i],
                                                                "Distance difference of " + str(distance_difference) + " ft"]
                                            if sourcekey in self.potentialUpdatesDict:
                                                self.potentialUpdatesDict[sourcekey].append(updatesvaluelist)

                                            else:
                                                self.potentialUpdatesDict[sourcekey] = [updatesvaluelist]
                                # Checks if i=last index number in field list. If so, adds the DATEMODIFIED date to the last dict value ONLY IF dict key exists. This will capture the DATEMODIFIED in the updates dictionary without making a change in the SDE database.
                                if (i == len(self.sourcefieldlist)-1) and (sourcekey in self.potentialUpdatesDict):
                                    newupdatesvaluelist = ['SourceTable->', self.sourcefieldlist[1],
                                                        fromgdb_search_row[1],
                                                        'DestTable->', self.destfieldlist[1],
                                                        desttable_dict[sourcekey][1],
                                                        'SourceTable->',
                                                        self.sourcefieldlist[2],
                                                        fromgdb_search_row[2],
                                                        'DestTable->', self.destfieldlist[2],
                                                        desttable_dict[sourcekey][2]]
                                    self.potentialUpdatesDict[sourcekey].append(newupdatesvaluelist)
                                i += 1

                        else:
                            while i < len(self.sourcefieldlist):
                                print("i: {0}".format(i))
                                # Checks if sourcetable value in each field is different from desttable value for that same field. Read as "if source fieldvalue NOT EQUAL to dest field value: run this"
                                print("fromgdb_search_row[i]: {0}; desttable_dict[sourcekey][i]: {1}".format(
                                    fromgdb_search_row[i],
                                    desttable_dict[sourcekey][i]))
                                if fromgdb_search_row[i] != desttable_dict[sourcekey][i]:
                                    # Check where id fields match in sourcetable & desttable
                                    print('Found update in: (source: {0}; dest: {1}).'.format(fromgdb_search_row[i],
                                                                                              desttable_dict[sourcekey][i]))
                                    whereclause = self.destfieldlist[0] + " = " + str(sourcekey)
                                    # whereclause = 'OBJECTID = ' + str(sourcekey)  # + ' AND ' + self.sourcefieldlist[1] + " < TO_DATE('" + checkdate + "', 'YYYY-MM-DD HH24:MI:SS')"

                                    print(whereclause)

                                    # Set up Update Cursor in SDE table for that ID
                                    with arcpy.da.SearchCursor(self.desttablepath, self.destfieldlist,
                                                               whereclause) as togdb_searchcur:
                                        logger.info("\nLooking for ID: {0}".format(whereclause))

                                        # A list is created for each change made in SDE; then the list is appended to the dictionary key ID
                                        updatesvaluelist = ['SourceTable->', self.sourcefieldlist[i],
                                                            fromgdb_search_row[i], 'DestTable->',
                                                            self.destfieldlist[i], desttable_dict[sourcekey][i]]

                                        if sourcekey in self.potentialUpdatesDict:
                                            self.potentialUpdatesDict[sourcekey].append(updatesvaluelist)

                                        else:
                                            self.potentialUpdatesDict[sourcekey] = [updatesvaluelist]

                                        for togdb_update_row in togdb_searchcur:
                                            # Iterating through field list where values equal
                                            # Print data values BEFORE change
                                            logger.info("**FOUND CHANGE - ID: {0} updated from {1}:{2} to {3}:{4}".format(
                                                    sourcekey, self.destfieldlist[i], fromgdb_search_row[i],
                                                    self.sourcefieldlist[i], togdb_update_row[i]))
                                # Checks if i=last index number in field list. If so, adds the DATEMODIFIED date to the last dict value ONLY IF dict key exists. This will capture the DATEMODIFIED in the updates dictionary without making a change in the SDE database.
                                if (i == len(self.sourcefieldlist)-1) and (sourcekey in self.potentialUpdatesDict):
                                    newupdatesvaluelist = ['SourceTable->', self.sourcefieldlist[1],
                                                        fromgdb_search_row[1],
                                                        'DestTable->', self.destfieldlist[1],
                                                        desttable_dict[sourcekey][1],
                                                        'SourceTable->',
                                                        self.sourcefieldlist[2],
                                                        fromgdb_search_row[2],
                                                        'DestTable->', self.destfieldlist[2],
                                                        desttable_dict[sourcekey][2]]
                                    self.potentialUpdatesDict[sourcekey].append(newupdatesvaluelist)
                                i += 1
                # else: x+=1          # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
        del desttable_dict, sourcetable_dict
        runtime = (_timetime_() - start_time) / 60
        print('Completed process in {0} minutes'.format(str(runtime)))
        return self.potentialUpdatesDict


    def findDeletedRecords(self):
        print('Finding deleted records...')

        start_time = _timetime_()
        desttable_dict = {}
        sourcetable_dict = {}

        with arcpy.da.SearchCursor(self.desttablepath, self.destfieldlist) as destCursor:
            # Create desttable dictionary of fields
            for destrow in destCursor:
                i = 0
                vals = []

                # Append all the field list names & their values into a list
                while i < len(self.destfieldlist):
                    vals.append((self.destfieldlist[i], str(destrow[i])))
                    i+=1

                # Add vals list as the value to the ID key
                desttable_dict[destrow[0]] = vals

        #print('desttable_dict: {0}'.format(desttable_dict))

        with arcpy.da.SearchCursor(self.sourcetablepath, self.sourcefieldlist) as sourceCursor:
            # Create sourcetable dictionary of fields
            for sourcerow in sourceCursor:
                i = 0
                vals = []

                # Append all the field list names & their values into a list
                while i < len(self.sourcefieldlist):
                    vals.append((self.sourcefieldlist[i], str(sourcerow[i])))
                    i+=1

                # Add vals list as the value to the ID key
                sourcetable_dict[sourcerow[0]] = vals

        #print('sourcetable_dict: {0}'.format(sourcetable_dict))

        # Compare dictionaries for different keys
        for keyid, vals in desttable_dict.items():
            if keyid not in sourcetable_dict:
                print('Record found that was deleted in source table in field {0}: {1}.'.format(self.sourcefieldlist[0], keyid))

                # For each key id not in the source table dictionary, add to the deletesDict by id (as key) with value of tuple of each fieldname, & each field value
                self.deletesDict[keyid] = vals
                print('Added to deletedDict dictionary')

        for key,val in self.deletesDict.items():
            print 'ID Field = {0}: Table Values = {1}'.format(key,val)

        del sourceCursor, destCursor, desttable_dict, sourcetable_dict
        runtime = (_timetime_() - start_time)/60
        print('Completed process in {0} minutes'.format(str(runtime)))
        return self.deletesDict

    def findAddedRecords(self):
        print('Finding added records...')
        start_time = _timetime_()
        desttable_dict = {}
        sourcetable_dict = {}

        with arcpy.da.SearchCursor(self.desttablepath, self.destfieldlist) as destCursor:
            # Create desttable dictionary of fields
            for destrow in destCursor:
                i = 0
                vals = []

                # Append all the field list names & their values into a list
                while i < len(self.destfieldlist):
                    vals.append((self.destfieldlist[i], str(destrow[i])))
                    i+=1

                # Add vals list as the value to the ID key
                desttable_dict[destrow[0]] = vals

        #print('desttable_dict: {0}'.format(desttable_dict))

        with arcpy.da.SearchCursor(self.sourcetablepath, self.sourcefieldlist) as sourceCursor:
            # Create sourcetable dictionary of fields
            for sourcerow in sourceCursor:
                i = 0
                vals = []

                # Append all the field list names & their values into a list
                while i < len(self.sourcefieldlist):
                    vals.append((self.sourcefieldlist[i], str(sourcerow[i])))
                    i+=1

                # Add vals list as the value to the ID key
                sourcetable_dict[sourcerow[0]] = vals

        #print('sourcetable_dict: {0}'.format(sourcetable_dict))

        # Compare dictionaries for different keys
        for keyid, vals in sourcetable_dict.items():
            if keyid not in desttable_dict:
                print('Record found that was added in source table in field {0}: {1}.'.format(self.sourcefieldlist[0], keyid))

                # For each key id not in the source table dictionary, add to the addssDict by id (as key) with value of tuple of each fieldname, & each field value
                self.addsDict[keyid] = vals
                print('Added to addsDict dictionary')

        for key,val in self.addsDict.items():
            print 'ID Field = {0}: Table Values = {1}'.format(key,val)

        del sourceCursor, destCursor, desttable_dict, sourcetable_dict
        runtime = (_timetime_() - start_time)/60
        print('Completed process in {0} minutes'.format(str(runtime)))
        return self.addsDict

    def updateRecords(self, excludeuserlist=None, distancethreshold=10):
        """
        :param: checkdate (string of date) Date string in format of 'yyy-mm-dd' to check if LASTMODIFIED or DATEMODIFIED date is before the current SDE date of when the field was last edited.
        This script finds all updated records in the source file feature class when it compares it to the SDE record.
        Learn more about editing geometry: https://boxshapedworld.wordpress.com/tutorials/arcpy-cursors-and-geometry/
        NOT AN OPTION--> (b/c this only compares # records, spatial reference, subtypes, but not geometry or field values)Try the FeatureCompare_management() tool to check if geometry is different for all features: THIS WON'T WORK SINCE YOU CAN ONLY USE A SORT FIELD TO MATCH RECORDS. SINCE WE HAVE A SUBSET OF DATA IN THE "SOURCE" FEATURE CLASS, THE SORT OPTION WON'T WORK TO MATCH FEATURES.https://pro.arcgis.com/en/pro-app/tool-reference/data-management/feature-compare.htm; coordinate system must match!!!
        :return:
        """
        print('Finding & editing updated records...')
        start_time = _timetime_()
        desttable_dict = {}
        sourcetable_dict = {}
        nonetype_var = None  # Added as a specific variable to allow UpdateCursor updates to pass over Null values.

        ##===============================================================================================##
        ##===============Added SHAPE geometry field to check for changes in location=====================##
        ##===============================================================================================##
        # But...the geometry SHAPE appears to be different within small precision & could relate to the publishing into AGOL. Thus, even though the location wasn't actually changed, something in the geometry was in the publishing process. I need to find some other general method to identify locational changes...maybe apply a distance threshold?
        # Need to add in Geometry field in cases where data are moved in the SHAPE@ geometry field
        # self.sourcefieldlist.append("SHAPE@")
        # self.destfieldlist.append("SHAPE@")
        ##===============================================================================================##

        # logging
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger("UpdateCursor")

        # create a file handler
        handler = logging.FileHandler('VersionedSDEDataUpdateCursor.log')
        handler.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)

        # start logging
        logger.info('Beginning Updating Versioned SDE data with Update Cursor')

        ###############################################
        # Must initialize ArcFM Solution when working with ArcFM Objects

        app = Dispatch('Miner.Framework.Dispatch.MMAppInitializeDispatch')
        au = Dispatch('Miner.Framework.Dispatch.MMAutoupdaterDispatch')
        runtime = Dispatch('Miner.Framework.Dispatch.MMRuntimeEnvironmentDispatch')

        runtime.RuntimeMode = mmRuntimeMode.mmRuntimeModeArcMap
        app.Initialize(mmLicensedProductCode.mmLPArcFM)

        # mmAUMNoEvents or mmAUMArcMap to fire AUs
        au.AutoUpdaterMode = mmAutoUpdaterMode.mmAUMStandAlone

        try:
            logger.info('Updating fields in ' + "fc")

            # Syntax: arcpy.da.UpdateCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
            # More info: http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-data-access/updatecursor-class.htm

            # Start an edit session. Must provide the workspace.
            edit = arcpy.da.Editor(self.sdeConnection)

            # Edit session is started without an undo/redo stack for versioned data
            #  (for second argument, use False for unversioned data)
            edit.startEditing(False, True)

            # Start an edit operation
            edit.startOperation()

##================================================================================================##
##=================Creating Dictionaries of Destination & Source Tables to compare equality=======##
##================================================================================================##

            with arcpy.da.SearchCursor(self.desttablepath, self.destfieldlist) as destCursor:
                # Create desttable dictionary of fields & data
                for destrow in destCursor:
                    # Add destrow values list as value to ID key
                    desttable_dict[destrow[0]] = destrow
            del destCursor
            # print('desttable_dict: {0}'.format(desttable_dict))

            with arcpy.da.SearchCursor(self.sourcetablepath, self.sourcefieldlist) as sourceCursor:
                # Create sourcetable dictionary of fields & data
                for sourcerow in sourceCursor:
                    # Add sourcerow values list as the value to the ID key
                    sourcetable_dict[sourcerow[0]] = sourcerow
            del sourceCursor
##================================================================================================##
## Iterating through source & dest dictionaries to find where values are different, then assign ==##
## a SearchCursor from sourcetable & an UpdateCursor in desttable to update sourcerow values to ==##
## destination table =============================================================================##
##================================================================================================##

            # ===============================================================================#
            # TESTING ONLY A FEW UPDATE RECORDS & THEN SAVING TO SEE IF UPDATES ARE COMPLETED
            # REMOVE INDENT & FOR-LOOP WHEN DONE TESTING
            # ===============================================================================#
            x=0                                           # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
            breakvalue = 200                              # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
            while x<=200:                                 # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
                print("---\n----X: {0}----\n".format(x))  # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
                if x == breakvalue: break                 # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#

                # Check if dictionary key & values are the same
                for sourcekey, sourceval in sourcetable_dict.iteritems():
                    if x == breakvalue: break             # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#

                    ##============== CHECKING DATE COMPARISONS HERE==============================##
                    # Checking if values in rows have lastmodified date before checkdate & if last user is not one the listed users
                    if (sourcekey in desttable_dict) and (str(sourcetable_dict[sourcekey][1]) > (str(desttable_dict[sourcekey][1]))):
                        if (excludeuserlist is not None) and (sourcetable_dict[sourcekey][2] not in excludeuserlist):
                            print("(sourcetable_dict[sourcekey][2] {0} not in excludeuserlist {1})".format(
                                sourcetable_dict[sourcekey][2], excludeuserlist))

                            ##========== This if statement was used before to check if all source values in the row were the same as the destination row values...but it turned out none of them were the same because the SHAPE tuple values were always 1/10 to 1/10000 off even if the original point locations were not changed. When publishing the feature service to ArcGIS Online, the values were slightly altered, possibly during reprojecting (even though the same NAD83UTM15N coordinate system was used for publishing to AGOL)

                            if x == breakvalue: break         # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
                            # print("sourcekey {0} in desttable_dict and desttable_dict[sourcekey] {1} != sourceval {2}".format(sourcekey, desttable_dict[sourcekey], sourceval))

                            # Set up search cursor to search through source table
                            # checkdate needs to be in format 'yyy-mm-dd'
                            whereclause = self.sourcefieldlist[0] + " = " + str(sourcekey)
                            # whereclause = 'ServerOID = ' + str(sourcekey)  # + ' AND ' + self.sourcefieldlist[1] + " < TO_DATE('" + checkdate + "', 'YYYY-MM-DD HH24:MI:SS')"
                            print(whereclause)

                            with arcpy.da.SearchCursor(self.sourcetablepath, self.sourcefieldlist, whereclause) as searchcur:
                                if x == breakvalue: break     # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
                                x += 1                        # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
                                for fromgdb_search_row in searchcur:
                                    # print("---\n----X: {0}----\n".format(x))  # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#
                                    # if x == breakvalue: break # === COMMENT OUT AFTER TESTING FOR # OF RECORDS ===#

                                    i = 3  # Setting counter to 2 to skip over the OID, DATEMODIFIED & LASTUSER fields.
                                    print("i = {0}; ID = {1}".format(i, sourcekey))

                                    # If-else condition that checks if "SHAPE" is in the field list & the value is a tuple.
                                    if self.sourcefieldlist[i] == "SHAPE@XY" and type(fromgdb_search_row[i]) is tuple:
                                        print type(fromgdb_search_row[i])
                                        distance_difference = " < " + str(distancethreshold)

                                        # # Checking if SHAPE@XY tuple values of X & Y's are within 1 foot of each other. When tested using 1/10 of a foot, the changed points were basically the same. Therefore, only those points that were different by within 1 foot were considered points were legitimate location updates.
                                        # if (round(fromgdb_search_row[i][0], 0) != round(togdb_update_row[i][0], 0)) or (
                                        #             round(fromgdb_search_row[i][1], 0) != round(togdb_update_row[i][1],0)):

                                        # Checking a tolerance of difference in distance between source & dest locations
                                        source_x = fromgdb_search_row[i][0]
                                        source_y = fromgdb_search_row[i][1]
                                        dest_x = togdb_update_row[i][0]
                                        dest_y = togdb_update_row[i][1]
                                        distance_difference = ((source_x - dest_x) ** 2 + (source_y - dest_y) ** 2) ** 0.5

                                        if distance_difference > distancethreshold:
                                            logger.info("From rounded XY: {0},{1}; SDE's rounded XY: {2},{3}".format(
                                                    round(fromgdb_search_row[i][0], 0),
                                                    round(fromgdb_search_row[i][1], 0),
                                                    round(togdb_update_row[0], 0),
                                                    round(togdb_update_row[i][1], 0)))

                                        else:
                                            i += 1  # Script continues by incrementing to next field after the tuple "SHAPE@XY" if there is no update in location. This will also check lastmodified or datemodified date, but when saving edits, the date field will still be changed to today's date upon saving edits. Storing the dates is for documentation purposes.

                                        while i < len(self.sourcefieldlist):
                                            print("i: {0}".format(i))

                                            # Checks if sourcetable value in each field is different from desttable value for that same field. Read as "if source fieldvalue NOT EQUAL to dest field value: run this"
                                            # print("fromgdb_search_row[i]: {0}; desttable_dict[sourcekey][i]: {1}".format(fromgdb_search_row[i], desttable_dict[sourcekey][i]))

                                            if fromgdb_search_row[i] != desttable_dict[sourcekey][i]:
                                                # Check where id fields match in sourcetable & desttable
                                                print('Found update in: (source: {0}; dest: {1}).'.format(fromgdb_search_row[i], desttable_dict[sourcekey][i]))

                                                whereclause = self.destfieldlist[0] + " = " + str(sourcekey)
                                                # whereclause = 'OBJECTID = ' + str(sourcekey)  # + ' AND ' + self.sourcefieldlist[1] + " < TO_DATE('" + checkdate + "', 'YYYY-MM-DD HH24:MI:SS')"
                                                print(whereclause)

                                                # Set up Update Cursor in SDE table for that ID
                                                with arcpy.da.UpdateCursor(self.desttablepath, self.destfieldlist, whereclause) as updatecur:
                                                    logger.info("\nLooking for ID: {0}".format(whereclause))
                                                    for togdb_update_row in updatecur:

                                                        # Iterating through field list where values equal
                                                        # Print data values BEFORE change
                                                        logger.info("**UPDATING - ID: {0} updated from SDE's {1}:{2} to GDB's values {3}:{4}".format(sourcekey, self.destfieldlist[i], togdb_update_row[i], self.sourcefieldlist[i], fromgdb_search_row[i]))

                                                        # A list is created for each change made in SDE; then the list is appended to the dictionary key ID
                                                        updatesvaluelist = ['SourceTable->', self.sourcefieldlist[i],
                                                                            fromgdb_search_row[i],
                                                                            'DestTable->', self.destfieldlist[i],
                                                                            desttable_dict[sourcekey][i],
                                                                            "Distance difference of " + str(distance_difference) + " ft"]
                                                        if sourcekey in self.updatesCompletedDict:
                                                            self.updatesCompletedDict[sourcekey].append(updatesvaluelist)

                                                        else:
                                                            self.updatesCompletedDict[sourcekey] = [updatesvaluelist]

                                                        # Assigns the updated value to the update row unless the value is None (which is the "nonetype_var"
                                                        togdb_update_row[i] = fromgdb_search_row[i] if fromgdb_search_row[i] else nonetype_var
                                                        updatecur.updateRow(togdb_update_row)  # This produces an error of "TypeError: argument must be sequence of values"; I'm testing changing the update value to a list since the updateRow function expects a list or tuple; see http://gis.stackexchange.com/questions/131961/insert-da-cursor-error-sequence-size-must-match-size-of-row

                                            # Checks if i=last index number in field list. If so, adds the DATEMODIFIED date to the last dict value ONLY IF dict key exists. This will capture the DATEMODIFIED in the updates dictionary without making a change in the SDE database.
                                            if (i == len(self.sourcefieldlist)-1) and (sourcekey in self.updatesCompletedDict):
                                                newupdatesvaluelist = ['SourceTable->', self.sourcefieldlist[1],
                                                                    fromgdb_search_row[1],
                                                                    'DestTable->', self.destfieldlist[1],
                                                                    desttable_dict[sourcekey][1],
                                                                    'SourceTable->',
                                                                    self.sourcefieldlist[2],
                                                                    fromgdb_search_row[2],
                                                                    'DestTable->', self.destfieldlist[2],
                                                                    desttable_dict[sourcekey][2]]
                                                self.updatesCompletedDict[sourcekey].append(newupdatesvaluelist)
                                            i += 1

                                    else:
                                        while i < len(self.sourcefieldlist):
                                            print("i: {0}".format(i))
                                            # Checks if sourcetable value in each field is different from desttable value for that same field. Read as "if source fieldvalue NOT EQUAL to dest field value: run this"
                                            print("fromgdb_search_row[i]: {0}; desttable_dict[sourcekey][i]: {1}".format(fromgdb_search_row[i],
                                                                                                                         desttable_dict[sourcekey][i]))
                                            if fromgdb_search_row[i] != desttable_dict[sourcekey][i]:
                                                # Check where id fields match in sourcetable & desttable
                                                print('Found update in: (source: {0}; dest: {1}).'.format(fromgdb_search_row[i],
                                                                                                          desttable_dict[sourcekey][i]))
                                                whereclause = self.destfieldlist[0] + " = " + str(sourcekey)
                                                # whereclause = 'OBJECTID = ' + str(sourcekey)  # + ' AND ' + self.sourcefieldlist[1] + " < TO_DATE('" + checkdate + "', 'YYYY-MM-DD HH24:MI:SS')"
                                                print(whereclause)

                                                # Set up Update Cursor in SDE table for that ID
                                                with arcpy.da.UpdateCursor(self.desttablepath, self.destfieldlist, whereclause) as updatecur:
                                                    logger.info("\nLooking for ID: {0}".format(whereclause))

                                                    # A list is created for each change made in SDE; then the list is appended to the dictionary key ID
                                                    updatesvaluelist = ['SourceTable->', self.sourcefieldlist[i],
                                                                        fromgdb_search_row[i], 'DestTable->',
                                                                        self.destfieldlist[i], desttable_dict[sourcekey][i]]

                                                    if sourcekey in self.updatesCompletedDict:
                                                        self.updatesCompletedDict[sourcekey].append(updatesvaluelist)

                                                    else:
                                                        self.updatesCompletedDict[sourcekey] = [updatesvaluelist]

                                                    for togdb_update_row in updatecur:
                                                        # Iterating through field list where values equal
                                                        # Print data values BEFORE change
                                                        logger.info("**UPDATING - ID: {0} updated from SDE's {1}:{2} to GDB's values {3}:{4}".format(sourcekey, self.destfieldlist[i], togdb_update_row[i], self.sourcefieldlist[i], fromgdb_search_row[i]))

                                                        # Assigns the updated value to the update row unless the value is None (which is the "nonetype_var"
                                                        togdb_update_row[i] = fromgdb_search_row[i] if fromgdb_search_row[i] else nonetype_var
                                                        updatecur.updateRow(togdb_update_row)  # This produces an error of "TypeError: argument must be sequence of values"; I'm testing changing the update value to a list since the updateRow function expects a list or tuple; see http://gis.stackexchange.com/questions/131961/insert-da-cursor-error-sequence-size-must-match-size-of-row

                                            # Checks if i=last index number in field list. If so, adds the DATEMODIFIED date to the last dict value ONLY IF dict key exists. This will capture the DATEMODIFIED in the updates dictionary without making a change in the SDE database.
                                            if (i == len(self.sourcefieldlist)-1) and (sourcekey in self.updatesCompletedDict):
                                                newupdatesvaluelist = ['SourceTable->', self.sourcefieldlist[1],
                                                                    fromgdb_search_row[1],
                                                                    'DestTable->', self.destfieldlist[1],
                                                                    desttable_dict[sourcekey][1],
                                                                    'SourceTable->',
                                                                    self.sourcefieldlist[2],
                                                                    fromgdb_search_row[2],
                                                                    'DestTable->', self.destfieldlist[2],
                                                                    desttable_dict[sourcekey][2]]
                                                self.updatesCompletedDict[sourcekey].append(newupdatesvaluelist)
                                            i += 1

            # reconcile and post the edit version
            # logger.info('Reconcile, post and delete the UpdateCursorEdits version')

            # Stop the edit operation.
            edit.stopOperation()

            # Stop the edit session and save the changes
            edit.stopEditing(True)

            # Optionally rec/post your version
            # arcpy.ReconcileVersions_management(arcpy.env.workspace, "ALL_VERSIONS", "SDE.Common",
            # versionName, "LOCK_ACQUIRED",
            # "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "KEEP_VERSION")
        except Exception, e:
            logger.error('General Error', exc_info=True)

        finally:
            ##Optionaly delete version when finished

            # arcpy.DeleteVersion_management(arcpy.env.workspace, versionName)

            # Release ArcFM License
            app.Shutdown

            del app, runtime, au
            logger.info('Finished the process to update fields via update cursor.')

        del desttable_dict, sourcetable_dict
        runtime = (_timetime_() - start_time) / 60
        logger.info('Completed Updates in SDE process in {0} minutes'.format(str(runtime)))
        logger.info(self.updatesCompletedDict)
        return self.updatesCompletedDict

    # def deleteRecords(self, deletesDict):
    #     print('Deleting records...')
    #
    # def addRecords(self, addsDict):
    #     print('Adding records...')

    def updateRecordsInList(self, recordidlist, distancethreshold=10):
        print('Finding & editing updated records...')
        start_time = _timetime_()
        desttable_dict = {}
        sourcetable_dict = {}
        nonetype_var = None  # Added as a specific variable to allow UpdateCursor updates to pass over Null values.

        ##===============================================================================================##
        ##===============Added SHAPE geometry field to check for changes in location=====================##
        ##===============================================================================================##
        # But...the geometry SHAPE appears to be different within small precision & could relate to the publishing into AGOL. Thus, even though the location wasn't actually changed, something in the geometry was in the publishing process. I need to find some other general method to identify locational changes...maybe apply a distance threshold?
        # Need to add in Geometry field in cases where data are moved in the SHAPE@ geometry field
        # self.sourcefieldlist.append("SHAPE@")
        # self.destfieldlist.append("SHAPE@")
        ##===============================================================================================##

        # logging
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger("UpdateCursor")

        # create a file handler
        handler = logging.FileHandler('VersionedSDEDataUpdateCursor.log')
        handler.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)

        # start logging
        logger.info('Beginning Updating Versioned SDE data with Update Cursor')

        ###############################################
        # Must initialize ArcFM Solution when working with ArcFM Objects

        app = Dispatch('Miner.Framework.Dispatch.MMAppInitializeDispatch')
        au = Dispatch('Miner.Framework.Dispatch.MMAutoupdaterDispatch')
        runtime = Dispatch('Miner.Framework.Dispatch.MMRuntimeEnvironmentDispatch')

        runtime.RuntimeMode = mmRuntimeMode.mmRuntimeModeArcMap
        app.Initialize(mmLicensedProductCode.mmLPArcFM)

        # mmAUMNoEvents or mmAUMArcMap to fire AUs
        au.AutoUpdaterMode = mmAutoUpdaterMode.mmAUMStandAlone

        try:
            logger.info('Updating fields in ' + "fc")

            # Syntax: arcpy.da.UpdateCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
            # More info: http://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-data-access/updatecursor-class.htm

            # Start an edit session. Must provide the workspace.
            edit = arcpy.da.Editor(self.sdeConnection)

            # Edit session is started without an undo/redo stack for versioned data
            #  (for second argument, use False for unversioned data)
            edit.startEditing(False, True)

            # Start an edit operation
            edit.startOperation()

            for recordID in recordidlist:
                whereclause = self.sourcefieldlist[0] + " = " + str(recordID)
                print(whereclause)

                with arcpy.da.SearchCursor(self.sourcetablepath, self.sourcefieldlist, whereclause) as searchcur:
                    for fromgdb_search_row in searchcur:
                        i = 3  # Setting counter to 2 to skip over the OID and DATEMODIFIED and LASTUSER fields.
                        print("i = {0}; ID = {1}".format(i, recordID))

                        # whereclause = 'OBJECTID = ' + str(recordID)
                        whereclause = self.destfieldlist[0] + " = " + str(recordID)

                        # Set up Update Cursor in SDE table for that ID
                        with arcpy.da.UpdateCursor(self.desttablepath, self.destfieldlist, whereclause) as updatecur:
                            logger.info("\nLooking for ID: {0}".format(whereclause))
                            for togdb_update_row in updatecur:

                                # If-else condition that checks if "SHAPE" is in the field list & the value is a tuple.
                                if self.sourcefieldlist[i] == "SHAPE@XY" and type(fromgdb_search_row[i]) is tuple:
                                    print type(fromgdb_search_row[i])
                                    distance_difference = " < " + str(distancethreshold)

                                    # Checking if SHAPE@XY tuple values of X & Y's are within 1 foot of each other. When tested using 1/10 of a foot, the changed points were basically the same. Therefore, only those points that were different by within 1 foot were considered points were legitimate location updates.
                                    # if (round(fromgdb_search_row[i][0], 0) != round(togdb_update_row[i][0], 0)) or (
                                    #             round(fromgdb_search_row[i][1], 0) != round(togdb_update_row[i][1], 0)):

                                    # Checking a tolerance of difference in distance between source & dest locations
                                    source_x = fromgdb_search_row[i][0]
                                    source_y = fromgdb_search_row[i][1]
                                    dest_x = togdb_update_row[i][0]
                                    dest_y = togdb_update_row[i][1]
                                    distance_difference = ((source_x - dest_x)**2 + (source_y - dest_y)**2)**0.5
                                    print distance_difference


                                    if distance_difference > distancethreshold:
                                        logger.info("From rounded XY: {0},{1}; SDE's rounded XY: {2},{3}".format(
                                            round(fromgdb_search_row[i][0], 0),
                                            round(fromgdb_search_row[i][1], 0),
                                            round(togdb_update_row[0], 0),
                                            round(togdb_update_row[i][1], 0)))

                                    else: i += 1  # Script continues by incrementing to next field after the tuple "SHAPE@XY" if there is no update in location. This will also check lastmodified or datemodified date, but when saving edits, the date field will still be changed to today's date upon saving edits. Storing the dates is for documentation purposes.

                                    while i < len(self.sourcefieldlist):
                                        print "i: %s" % (i)
                                        # Iterating through field list where values equal
                                        # Print data values BEFORE change

                                        if fromgdb_search_row[i] != togdb_update_row[i]:
                                            logger.info("**UPDATING - ID: {0} updated from SDE's {1}:{2} to GDB's values {3}:{4}".format(recordID, self.destfieldlist[i], togdb_update_row[i], self.sourcefieldlist[i], fromgdb_search_row[i]))

                                            # A list is created for each change made in SDE; then the list is appended to the dictionary key ID
                                            updatesvaluelist = ['SourceTable->', self.sourcefieldlist[i],
                                                                fromgdb_search_row[i],
                                                                'DestTable->', self.destfieldlist[i],
                                                                togdb_update_row[i],
                                                                "Distance difference of " + str(distance_difference) + " ft"]
                                            if recordID in self.updatesCompletedDict:
                                                self.updatesCompletedDict[recordID].append(updatesvaluelist)

                                            else:
                                                self.updatesCompletedDict[recordID] = [updatesvaluelist]

                                            # Assigns the updated value to the update row unless the value is None (which is the "nonetype_var"
                                            # togdb_update_row[i] = fromgdb_search_row[i] if fromgdb_search_row[i] else nonetype_var
                                            togdb_update_row[i] = fromgdb_search_row[i] if fromgdb_search_row[i] else nonetype_var  # 0
                                            updatecur.updateRow(togdb_update_row)  # This produces an error of "TypeError: argument must be sequence of values"; I'm testing changing the update value to a list since the updateRow function expects a list or tuple; see http://gis.stackexchange.com/questions/131961/insert-da-cursor-error-sequence-size-must-match-size-of-row

                                        # Checks if i=last index number in field list. If so, adds the DATEMODIFIED date to the last dict value ONLY IF dict key exists. This will capture the DATEMODIFIED in the updates dictionary without making a change in the SDE database.
                                        if (i == len(self.sourcefieldlist) - 1) and (recordID in self.updatesCompletedDict):
                                            newupdatesvaluelist = ['SourceTable->', self.sourcefieldlist[1],
                                                                   fromgdb_search_row[1],
                                                                   'DestTable->', self.destfieldlist[1],
                                                                   togdb_update_row[1],
                                                                   'SourceTable->',
                                                                   self.sourcefieldlist[2],
                                                                   fromgdb_search_row[2],
                                                                   'DestTable->', self.destfieldlist[2],
                                                                   togdb_update_row[2]]
                                            self.updatesCompletedDict[recordID].append(newupdatesvaluelist)

                                        i += 1

                                # Executes if there is no SHAPE@XY field
                                else:
                                    while i < len(self.sourcefieldlist):
                                        print "i: %s" % (i)

                                        # Iterating through field list where values equal
                                        # Print data values BEFORE change
                                        if fromgdb_search_row[i] != togdb_update_row[i]:
                                            logger.info("**UPDATING - ID: {0} updated from SDE's {1}:{2} to GDB's values {3}:{4}".format(recordID, self.destfieldlist[i], togdb_update_row[i], self.sourcefieldlist[i], fromgdb_search_row[i]))

                                            # A list is created for each change made in SDE; then the list is appended to the dictionary key ID
                                            updatesvaluelist = ['SourceTable->', self.sourcefieldlist[i],
                                                                fromgdb_search_row[i],
                                                                'DestTable->', self.destfieldlist[i],
                                                                togdb_update_row[i]]
                                            if recordID in self.updatesCompletedDict:
                                                self.updatesCompletedDict[recordID].append(updatesvaluelist)

                                            else:
                                                self.updatesCompletedDict[recordID] = [updatesvaluelist]

                                            # Assigns the updated value to the update row unless the value is None (which is the "nonetype_var"
                                            # togdb_update_row[i] = fromgdb_search_row[i] if fromgdb_search_row[i] else nonetype_var
                                            togdb_update_row[i] = fromgdb_search_row[i] if fromgdb_search_row[i] else nonetype_var  # 0
                                            updatecur.updateRow(togdb_update_row)  # This produces an error of "TypeError: argument must be sequence of values"; I'm testing changing the update value to a list since the updateRow function expects a list or tuple; see http://gis.stackexchange.com/questions/131961/insert-da-cursor-error-sequence-size-must-match-size-of-row

                                        # Checks if i=last index number in field list. If so, adds the DATEMODIFIED date to the last dict value ONLY IF dict key exists. This will capture the DATEMODIFIED in the updates dictionary without making a change in the SDE database.
                                        if (i == len(self.sourcefieldlist) - 1) and (recordID in self.updatesCompletedDict):
                                            newupdatesvaluelist = ['SourceTable->', self.sourcefieldlist[1],
                                                                   fromgdb_search_row[1],
                                                                   'DestTable->', self.destfieldlist[1],
                                                                   togdb_update_row[1],
                                                                   'SourceTable->',
                                                                   self.sourcefieldlist[2],
                                                                   fromgdb_search_row[2],
                                                                   'DestTable->', self.destfieldlist[2],
                                                                   togdb_update_row[2]]
                                            self.updatesCompletedDict[recordID].append(newupdatesvaluelist)

                                        i += 1

            # reconcile and post the edit version
            # logger.info('Reconcile, post and delete the UpdateCursorEdits version')

            # Stop the edit operation.
            edit.stopOperation()

            # Stop the edit session and save the changes
            edit.stopEditing(True)

            # Optionally rec/post your version
            # arcpy.ReconcileVersions_management(arcpy.env.workspace, "ALL_VERSIONS", "SDE.Common",
            # versionName, "LOCK_ACQUIRED",
            # "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "KEEP_VERSION")

        except Exception, e:
            logger.error('General Error', exc_info=True)

        finally:
            ##Optionaly delete version when finished

            # arcpy.DeleteVersion_management(arcpy.env.workspace, versionName)

            # Release ArcFM License
            app.Shutdown

            del app, runtime, au
            logger.info('Finished the process to update fields via update cursor.')

        del desttable_dict, sourcetable_dict
        runtime = (_timetime_() - start_time) / 60
        logger.info('Completed Updates in SDE process in {0} minutes'.format(str(runtime)))
        logger.info(self.updatesCompletedDict)
        return self.updatesCompletedDict

    def exportUpdatesToCsv(self, tableDictionary, outputFolder, outfilename):
        """
        Purpose: Method takes the updatesDict and exports it to a csv file.
        :param tableDictionary: (dictionary) Dictionary from this class' instance for the return dictionary of updatesDict, deletesDict, or addsDict records. Output dictionary data structure in format of:
            {131552: [['SourceTable->', 'INSTALLYEAR', 1946, 'DestTable->', 'INSTALLYEAR', 2016], ['SourceTable->', 'HEIGHT', 35, 'DestTable->', 'HEIGHT', 40], ['SourceTable->', 'CLASS', 5, 'DestTable->', 'CLASS', 3], ['SourceTable->', 'MATERIAL', u'CEDAR', 'DestTable->', 'MATERIAL', u'RED PINE'], ['SourceTable->', 'BARCODE', u'A0796565', 'DestTable->', 'BARCODE', u'M5442478'], ['SourceTable->', 'PRIOR_TAG_NUMBER', None, 'DestTable->', 'PRIOR_TAG_NUMBER', u'A0796565']]}
        :param outputFolder: (string filepath to folder where excel file will be saved.
        :return:
        """
        start_time = _timetime_()
        currentdate = datetime.date.today()
        timeformat = "%H%M%S"
        currenttime = datetime.datetime.today()
        z = currenttime.strftime(timeformat)

        # logging
        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger("exportUpdatesToCsv")

        # create a file handler
        handler = logging.FileHandler('exportUpdatesToCsv.log')
        handler.setLevel(logging.DEBUG)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)

        # start logging
        logger.info('Beginning Exporting of Updates Dictionary to a CSV file')

        # Take dictionary object & format those deletes/adds/updates to a csv, comma-separated.

        # Create outFile
        # outFileName = raw_input('Enter file name of csv table table:')
        outFile = open(outputFolder + '\\' + outfilename + "_" + str(currentdate) + "_" + str(z) + '.csv', 'w')

        # Iterate through selected dictionary & write to file list value 1
        for key, vals in tableDictionary.items():
            outFile.write('{0}: {1}\n'.format(key, vals))

        print('Find your file "{0}.csv" in: {1}'.format(outfilename, outputFolder))
        del outFile
        runtime = (_timetime_() - start_time)/60
        logger.info('Completed export of UpdatesDictionary process in {0} minutes'.format(str(runtime)))


    def exportAddsDeletesToCsv(self, tableDictionary, outputFolder, outfilename):
        """
        Purpose: Method takes the addsDict and exports it to a csv file.
        :param tableDictionary: (dictionary) Dictionary from this class' instance for the return dictionary of updatesDict, deletesDict, or addsDict records. Output dictionary data structure in format of:
            {189889: [('ServerOID', '189889'), ('TRANSFORMEROBJECTID', '141521'), ('INSTALLYEAR', '2005')])}
        :param outputFolder: (string filepath to folder where excel file will be saved.
        :return:
        """
        start_time = _timetime_()
        currentdate = datetime.date.today()
        timeformat = "%H%M%S"
        currenttime = datetime.datetime.today()
        z = currenttime.strftime(timeformat)

        # Take dictionary object & format those deletes/adds/updates to a csv, comma-separated.

        # Create outFile
        # outFileName = raw_input('Enter file name of csv table table:')
        outFile = open(outputFolder + '\\' + outfilename + "_" + str(currentdate) + "_" + str(z) + '.csv', 'w')

        fieldHeaderString = ''
        # Create string of sourcetable headers
        i = 0
        while i < len(sourcefields):
            fieldHeaderString += '{0}_source,'.format(sourcefields[i])
            i += 1

        # print(fieldHeaderString)
        outFile.write(fieldHeaderString + '\n')  # Writes fields to 1st line

        # Iterate through selected dictionary & write to file list value 1
        for key, vals in tableDictionary.items():
            # Source table values
            i = 0  # Counter for fieldname:fieldvalue for source table
            while i < len(sourcefields):
                # outFile.write('{0},'.format(vals[0][i][1])) # previous code that iterated through both source & dest updates rows.
                outFile.write('{0},'.format(vals[i][1]))
                i += 1

            # Add for next line
            outFile.write('\n')

        print('Find your file "{0}.csv" in: {1}'.format(outFileName, outputFolder))
        del outFile
        runtime = (_timetime_() - start_time) / 60
        print('Completed process in {0} minutes'.format(str(runtime)))


print('Finished loading TableChanges class\n')
#tk_wrapper.mainloop()
