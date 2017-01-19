# Import custom class for getting SDE/file gdb table changes
import GDBDataTableChanges

##=======================================================================##
##============================Testing Output=============================##
##=======================================================================##
# Executing Program for Storm Response Tables:
"""
Database Features:
C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb
TABLES:
---
GDB tablename       -->SDE tablename: ["fieldnames"]
---
Anchor_Unit         -->GISADM.Anchor: ['OBJECTID', 'DOWNGUYOBJECTID', 'INSTALLYEAR', 'NUMBEROFANCHORS', 'SUBTYPECD'] # 'ServerOID'
Cutout              -->GISADM.Electric/GISADM.CutOut: ['OBJECTID', 'SHAPE@XY', 'SUBTYPECD', 'INSTALLYEAR'] # 'ServerOID'
Down_Guys           -->GISADM.Electric/GISADM.DownGuy: ['OBJECTID', 'SHAPE@XY', 'INSTALLYEAR', 'SUBTYPECD', 'SYMBOLROTATION', 'NUMBEROFGUYS'] # 'ServerOID'
Line_Cutout_Unit    -->GISADM.CutOutUnit: ['CUTOUTOBJECTID', 'SUBTYPECD', 'INSTALLYEAR', 'AMPS', 'LOADBREAK', 'ACCESSBANKOBJECTID'] # 'ServerOID'
Pedestals           -->GISADM.Electric/GISADM.SurfaceStructure: ['OBJECTID', 'SHAPE@XY', 'INSTALLYEAR', 'FACILITYOWNER', 'SUBTYPECD', 'BARCODE', 'BARCODE2'] # 'ServerOID'
Transformer         -->GISADM.Electric/GISADM.Transformer: ['OBJECTID', 'SHAPE@XY', 'SUBTYPECD', 'OPERATINGVOLTAGE', 'SECVOLTAGE', 'MULTIVOLT', 'DUALVOLT'] # 'ServerOID'
Transformer_Unit    -->GISADM.TransformerUnit: ['OBJECTID', 'SUBTYPECD', 'TRANSFORMEROBJECTID', 'KVA', 'INSTALLYEAR', 'CUTOUTINSTALLYEAR'] # 'ServerOID'


C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_Poles_v5_11212016\StormAssessment_Demo_Poles_v5_11212016.gdb
TABLES:
---
GDB tablename       -->SDE tablename
---
Crossarm_Unit       -->GISADM.CrossArms: ['OBJECTID', 'STRUCTUREOBJECTID', 'INSTALLYEAR', 'NUMBERINSTALLED'] # 'ServerOID'
Pole_Attachments_   -->GISADM.INSP_POLE_ATTACHMENTS: ['OBJECTID', 'SUPPORTSTRUCTUREOBJECTID', 'PHYSICALTYPE', 'FUNCTIONTYPE', 'INSPECTIONDATE', 'ATTACHING_COMPANY', 'USEFORBILLING'] # 'ServerOID'
Poles               -->GISADM.Electric/GISADM.SupportStructure: ["OBJECTID", "SHAPE@XY", "INSTALLYEAR", "SUBTYPECD", "HEIGHT", "CLASS", "MATERIAL", "BARCODE", "PRIOR_TAG_NUMBER", "FACILITYOWNER"] # "ServerOID"
Poles               -->Poles__ATTACH (this is the picture attachment table & may not yet have an associated table in the SDE yet)

"""
#=======================================================================##
#=============================Poles=====================================##
## PREVIOULSY RUN ON: 12/23/2016 by full comparison (not by an OID list)
## SUCCESSFULLY COMPLETED, RECONCILED & POSTED ON: 12/22/2016 by full comparison (not by an OID list)
## EXECUTION NOTES:
##=======================================================================##
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_poles_v2.sde'  # Version should be the KIM version & Not DEFAULT
# # sourcetable = r'Database Connections\GISArcFM_Test_ksundeen_KIM_poles_v.sde\GISADM.Electric\GISADM.SupportStructure'  # for bringing back data edits from 12/21 back into production SDE
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_Poles_v5_11212016\StormAssessment_Demo_Poles_v5_11212016.gdb\Poles'
# desttable = sde_path + r'\GISADM.Electric\GISADM.SupportStructure'
# sourcefields = ["ServerOID", "DATEMODIFIED", "LASTUSER", "SHAPE@XY", "INSTALLYEAR", "SUBTYPECD", "HEIGHT", "CLASS", "MATERIAL", "BARCODE", "PRIOR_TAG_NUMBER", "FACILITYOWNER"]
# destfields = ["OBJECTID", "DATEMODIFIED", "LASTUSER", "SHAPE@XY", "INSTALLYEAR", "SUBTYPECD", "HEIGHT", "CLASS", "MATERIAL", "BARCODE", "PRIOR_TAG_NUMBER", "FACILITYOWNER"]
# poletable = GDBDataTableChanges.TableChanges(tablename='poles',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
# #
# # print('Running updateRecords() method for Poles')
# # myUpdatesCompletedDict = poletable.updateRecords()
# # for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
# #
# # print('Exporting updates using exportUpdatesToCsv() method for Poles')
# # poletable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
# #                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
# #                                              outfilename='PoleUpdatedMade')
# #
# print('Running updateRecordsInList() method for Poles')
# myUpdatesCompletedDict = poletable.updateRecordsInList(recordidlist=officialupdates_oidlist_poles)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Poles')
# poletable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict, outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                              outfilename='PoleUpdatesMade_ByOIDlist')


#=======================================================================##
#============================Cross Arms=================================##
## PREVIOULSY RUN ON: 1/5/17 (nothing was updated)
## EXECUTION NOTES: 1/5/17=>ServerOID was not included in the extract for the storm app. The STRUCTUREOBJECTID is the OID for the pole & I'll check for all duplicates in the file gdb; take those OIDs & check them manually. in the 8,211 crossarm units that were included in the storm response project, 178 have duplicate STRUCTUREOBJECTIDS meaning there are more than 1 cross arm for a pole. When exporting the records, they were probably exported in the same order of the of OIDs. Maybe I can use the order of OBJECTIDs in the file gdb to find the same order in the CrossArms in the SDE to get the order of crossarms for each pole.
##=======================================================================##
sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM.sde'  # Version should be the KIM version & Not DEFAULT
# duplicates_oidlist_crossarms = [116742]
sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_Poles_v5_11212016\StormAssessment_Demo_Poles_v5_11212016.gdb\Crossarm_Unit'
# officialupdates_oidlist_crossarms = []
desttable = sde_path + r'\GISADM.CrossArms'
sourcefields = ["STRUCTUREOBJECTID", "DATEMODIFIED", "LASTUSER", "INSTALLYEAR", "NUMBERINSTALLED"]
destfields = ["STRUCTUREOBJECTID", "DATEMODIFIED", "LASTUSER", "INSTALLYEAR", "NUMBERINSTALLED"]
crossarmstable = GDBDataTableChanges.TableChanges(tablename='crossarms',
                       sourcetablepath=sourcetable,
                       desttablepath=desttable,
                       sourcefieldlist=sourcefields,
                       destfieldlist=destfields,
                       sdeConnection=sde_path)
#
# print('Running findUpdatedRecords() method for Cross Arms')
# myPotentialUpdatesDict = crossarmstable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Cross Arms')
# crossarmstable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                              outfilename='CrossArms_PotentialUpdates')
# #
# print('Running updateRecordsInList() method for Cross Arms')
# myUpdatesCompletedDict = crossarmstable.updateRecordsInList(recordidlist=duplicates_oidlist_crossarms)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Cross Arms')
# crossarmstable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                   outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                   outfilename='CrossArmsUpdatesMade_ByOIDlist')

##=======================================================================##
##=================================Cutouts===============================##
## PREVIOULSY RUN ON: 12/23/2016
## SUCCESSFULLY COMPLETED, RECONCILED & POSTED ON:
## EXECUTION NOTES: not completing correctly. With error "RuntimeError: The modified geometry must be a different geometry instance from the feature's original geometry (e.g., a copy or new instance). [class name = GISADM.CutOut, object id = 471106]"
# Either update locations manually or use reference here to edit geometric network: http://support.esri.com/technical-article/000010000
##=======================================================================##
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Cutout'
# desttable = sde_path + r'\GISADM.Electric\GISADM.CutOut'
# sourcefields = ['ServerOID', 'SHAPE@XY', 'SUBTYPECD', 'INSTALLYEAR']
# destfields = ['OBJECTID', 'SHAPE@XY', 'SUBTYPECD', 'INSTALLYEAR']
# cutouttable = GDBDataTableChanges.TableChanges(tablename='cutouts',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
#
# print('Running findUpdateRecords() method for Cutouts')
# myPotentialUpdatesDict = cutouttable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# print('Running updateRecords() method for Cutouts')
# myUpdatesCompletedDict = cutouttable.updateRecords()
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Cutouts')
# cutouttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                              outfilename='Cutout_UpdatesMade')

# ##=======================================================================##
# ##========================Pole Attachments===============================##
## PREVIOULSY RUN ON: 12/23/2016
## SUCCESSFULLY COMPLETED, RECONCILED & POSTED ON: 12/23/2016
## EXECUTION NOTES: Had errors with field names being wrong.
##=======================================================================##
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_Poles_v5_11212016\StormAssessment_Demo_Poles_v5_11212016.gdb\Pole_Attachments_'
# desttable = sde_path + r'\GISADM.INSP_POLE_ATTACHMENTS'
# sourcefields = ['ServerOID', 'INSPECTIONDATE', 'PHYSICALTYPE', 'FUNCTIONTYPE', 'ATTACHING_COMPANY', 'USEFORBILLING']
# destfields = ['OBJECTID', 'INSPECTIONDATE', 'PHYSICALTYPE', 'FUNCTIONTYPE', 'ATTACHING_COMPANY', 'USEFORBILLING']
# poleattachtable = GDBDataTableChanges.TableChanges(tablename='cutouts',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
#
# # print('Running findUpdatedRecords() method for Pole Attachments')
# # myUpdatesDict = poleattachtable.findUpdatedRecords()
# # for key, vals in myUpdatesDict.iteritems(): print(key,vals)
#
# print('Running updateRecords() method for Pole Attachments')
# myUpdatesCompletedDict = poleattachtable.updateRecords()
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Pole Attachments')
# poleattachtable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                              outfilename='PoleAttachments_UpdatesMade')

##=======================================================================##
##===============================Anchor Units============================##
## PREVIOULSY RUN ON: 12/23/2016 using comparison (not by an OID list)
## SUCCESSFULLY COMPLETED: 12/23/2016
## RECONCILED & POSTED ON: 12/23/2016
## EXECUTION NOTES:
##=======================================================================##
# officialupdates_oidlist_anchornit = [51252, 51253, 53492, 53493, 53514, 60510, 60517, 63695, 75622, 75623, 75628, 75810, 75813, 80476, 96077, 402889, 601953]
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_anchorunits.sde'  # Version should be the KIM version & Not DEFAULT
# ### sourcetable = r'Database Connections\GISArcFM_Test_ksundeen_KIM_poles.sde\GISADM.Anchor'
# sourcetable = r'C:\GDBReplication\ClientBase\Production_Replica\Production_Replica.gdb\Anchor'
# ### sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Anchor_Unit'
# desttable = sde_path + r'\GISADM.Anchor'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'DOWNGUYOBJECTID', 'INSTALLYEAR', 'NUMBEROFANCHORS', 'SUBTYPECD']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'DOWNGUYOBJECTID', 'INSTALLYEAR', 'NUMBEROFANCHORS', 'SUBTYPECD']
# anchorunittable = GDBDataTableChanges.TableChanges(tablename='anchorunit',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)

## print('Running updateRecords() method for Anchor_Unit')
## myUpdatesCompletedDict = anchorunittable.updateRecords()
## for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
##
## print('Exporting updates using exportUpdatesToCsv() method for Anchor_Unit')
## anchorunittable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict, outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles', outfilename='AnchorUnits_UpdatesMade')

# print('Running updateRecordsInList() method for Anchor Units')
# myUpdatesCompletedDict = anchorunittable.updateRecordsInList(recordidlist=officialupdates_oidlist_anchornit)
# # for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Anchor Units')
# anchorunittable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict, outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles', outfilename='AnchorUnits_UpdatesMade_ByOIDlist')

##=======================================================================##
##===============================Down Guys===============================##
## PREVIOULSY RUN ON: 12/23/2016
## SUCCESSFULLY COMPLETED: 12/23/2016
## RECONCILED & POSTED ON: 12/23/2016
## EXECUTION NOTES: need to redo these changes
##=======================================================================##
# officialupdates_oidlist_downguys = [66235, 72071, 84111, 90161, 90162, 90167, 90544, 90547, 100374, 109845, 622449]
# desttable = sde_path + r'\GISADM.Electric\GISADM.DownGuy'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'INSTALLYEAR', 'SUBTYPECD', 'SYMBOLROTATION', 'NUMBEROFGUYS']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'INSTALLYEAR', 'SUBTYPECD', 'SYMBOLROTATION', 'NUMBEROFGUYS']
# downguytable = GDBDataTableChanges.TableChanges(tablename='downguy',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
# #
### print('Running updateRecords() method for DownGuy')
### myUpdatesCompletedDict = downguytable.updateRecords()
### for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
### print('Exporting updates using exportUpdatesToCsv() method for Anchor_Unit')
### downguytable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles', outfilename='DownGuys_UpdatesMade')

# print('Running updateRecordsInList() method for Down Guys')
# myUpdatesCompletedDict = downguytable.updateRecordsInList(recordidlist=officialupdates_oidlist_downguys)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Down Guys')
# downguytable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                 outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                 outfilename='DownGuysRevertedUpdatesMade')

##=======================================================================##
##============================Line_Cutout_Unit===========================##
## PREVIOULSY RUN ON: 12/23/2016; 12/27/2016
## SUCCESSFULLY COMPLETED: 12/23/2016; but decided not to post since the installyears seemed to be changed back to 0 from 2016, making me think the changes were updating already changed records.
## RECONCILED & POSTED ON: No changes were found. But I do need to change the code so that the LASTMODIFIED date is not attempted to be changed (even though it still would be updated to today's date), my username is still put in as the lastmodified user.
## EXECUTION NOTES:
##=======================================================================##
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Line_Cutout_Unit'
# desttable = sde_path + r'\GISADM.CutOutUnit'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'SUBTYPECD', 'INSTALLYEAR', 'AMPS', 'LOADBREAK']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'SUBTYPECD', 'INSTALLYEAR', 'AMPS', 'LOADBREAK']
# linecutoutunittable = GDBDataTableChanges.TableChanges(tablename='linecutoutunit',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
#
# print('Running findUpdatedRecords() method for Line Cutout Unit')
# myPotentialUpdatesdDict = linecutoutunittable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesdDict.iteritems(): print(key,vals)
# #
# # print('Exporting potential updates using exportUpdatesToCsv() method for Line Cutout Unit')
# # linecutoutunittable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesdDict,
# #                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
# #                                              outfilename='LineCutoutUnit_PotentialUpdatesMade')
#
# print('Running updateRecords() method for Line Cutout Unit')
# myUpdatesCompletedDict = linecutoutunittable.updateRecords()
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Line Cutout Unit')
# linecutoutunittable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict, outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',outfilename='LineCutoutUnit_UpdatesMade')


##=======================================================================##
##=================================Pedestals=============================##
## PREVIOULSY RUN ON: 12/28/2016
## SUCCESSFULLY COMPLETED: 12/28/2016
## RECONCILED & POSTED ON: no need. There were no updates.
## EXECUTION NOTES:
##=======================================================================##
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Pedestals'
# desttable = sde_path + r'\GISADM.Electric\GISADM.SurfaceStructure'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'INSTALLYEAR', 'FACILITYOWNER', 'SUBTYPECD', 'BARCODE', 'BARCODE2']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'INSTALLYEAR', 'FACILITYOWNER', 'SUBTYPECD', 'BARCODE', 'BARCODE2']
# pedestalsttable = GDBDataTableChanges.TableChanges(tablename='pedestals',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
#
# print('Running findUpdatedRecords() method for Pedestals')
# myPotentialUpdatesDict = pedestalsttable.findUpdatedRecords(excludeuserlist=['ksundeen_mnpower', 'mstrukel_mnpower'])
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# pedestalsttable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Pedestals_PotentialUpdates')

# print('Running updateRecords() method for Pedestals')
# myUpdatesCompletedDict = pedestalsttable.updateRecords()
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Pedestals')
# pedestalsttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Pedestals_UpdatesMade')


##=======================================================================##
##================================Transformers===========================##
## PREVIOULSY RUN ON: 12/28/2016-attempting to run the update from a list of OIDs, but is taking a long time
## SUCCESSFULLY COMPLETED:
## RECONCILED & POSTED ON:
## EXECUTION NOTES: not completing correctly. With error "RuntimeError: The modified geometry must be a different geometry instance from the feature's original geometry (e.g., a copy or new instance). [class name = GISADM.CutOut, object id = 471106]"
# Either update locations manually or use reference here to edit geometric network: http://support.esri.com/technical-article/000010000 (same as Cutout geometric network issues)
##=======================================================================##
# officialupdates_oidlist_transformers [22489, 33173, 37528, 4474, 6147, 6486, 6815, 9181, 11104]
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Transformer'
# desttable = sde_path + r'\GISADM.Electric\GISADM.Transformer'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'SUBTYPECD', 'OPERATINGVOLTAGE', 'SECVOLTAGE', 'MULTIVOLT', 'DUALVOLT']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'SUBTYPECD', 'OPERATINGVOLTAGE', 'SECVOLTAGE', 'MULTIVOLT', 'DUALVOLT']
# transformerttable = GDBDataTableChanges.TableChanges(tablename='transformers',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
# #
# print('Running findUpdatedRecords() method for Transformers')
# myPotentialUpdatesDict = transformerttable.findUpdatedRecords(excludeuserlist=['ksundeen_mnpower', 'mstrukel_mnpower'])
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# transformerttable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Transformer_PotentialUpdates')

# print('Running updateRecords() method for Transformers')
# myUpdatesCompletedDict = transformerttable.updateRecords()
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)

# oidlist_transformers = [11104, 22489,33173,37528,4474,6147,6486,6815,9181]
# print('Running updateRecordsInList() method for Transformers using an OID list')
# myUpdatesCompletedDict = transformerttable.updateRecordsInList(recordidlist=oidlist_transformers)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Transformers')
# transformerttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Transfomer_UpdatesMade_fromOIDList')


##=======================================================================##
##============================Transformer Unit===========================##
## PREVIOULSY RUN ON:
## SUCCESSFULLY COMPLETED:
## RECONCILED & POSTED ON:
## EXECUTION NOTES:
##=======================================================================##
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Transformer_Unit'
# desttable = sde_path + r'\GISADM.TransformerUnit'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'SUBTYPECD', 'TRANSFORMEROBJECTID', 'KVA', 'INSTALLYEAR', 'CUTOUTINSTALLYEAR']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'SUBTYPECD', 'TRANSFORMEROBJECTID', 'KVA', 'INSTALLYEAR', 'CUTOUTINSTALLYEAR']
# txunitttable = GDBDataTableChanges.TableChanges(tablename='txunit',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
# #
# # print('Running findUpdatedRecords() method for Transformer Unit')
# # myPotentialUpdatesDict = txunitttable.findUpdatedRecords()
# # for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
# #
# # txunitttable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
# #                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
# #                                    outfilename='TxUnit_PotentialUpdates')
#
# oidlist_txunit = [7061, 7688, 7761, 7762, 7764, 7863, 7867, 7868, 7912, 8121, 10492, 10891, 10963, 11367, 11377, 11552, 11599, 11871, 12035, 12045, 12049, 12054, 12061, 12066, 12100, 12386, 12395, 12481, 13330, 13532, 13894, 13936, 13981, 14313, 14556, 17468, 17519, 17617, 17945, 18688, 18775, 18874, 22738, 22749, 23391, 26150, 26168, 26173, 26219, 26222, 26237, 26238, 26466, 26504, 26512, 26527, 26601, 35639, 36640, 37719, 151129]
# print('Running updateRecordsInList() method for Transformer Unit using an OID list')
# myUpdatesCompletedDict = txunitttable.updateRecordsInList(recordidlist=oidlist_txunit)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# # print('Running updateRecords() method for Transformer Unit')
# # myUpdatesCompletedDict = txunitttable.updateRecords()
# # for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
# #
# print('Exporting updates using exportUpdatesToCsv() method for Transformer Units')
# txunitttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='TxUnit_UpdatesMade')