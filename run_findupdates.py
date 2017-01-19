# Import custom class for getting SDE/file gdb table changes
import GDBDataTableChanges


#=======================================================================##
#=============================Poles=====================================##
"""
PREVIOULSY RUN ON: 1/9/17; 1/11/17-awaiting review by Marj & Paula; 1/11/17-running for all potential updates
RECONCILED & POSTED ON: 1/11/17
EXECUTION NOTES: Includes all poles that were modified during storm update & excludes those that Kim & Marjorie updated manually. 1/9/17: currently reviewing updates to ensure changes are valid. 267 rows were changed. All the SHAPE changes are only a few feet and require the snapping to be changed. I need to have Marjorie & Paula review these changes to see if they are valid location changes. Paula & Marj reviewed changes & noted that oids 115717, 113420, 2665, and 2508 should not be updated.
"""
##=======================================================================##
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_poles.sde'
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
#
# print('Running findUpdatedRecords() method for Poles')
# myPotentialUpdatesDict = poletable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Poles')
# poletable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                              outfilename='Poles_AllPotentialUpdates')
#
# reviewed_updates_oidlist_poles = [2634, 2650, 2652, 2702, 2703, 2705, 2711, 3415, 3646, 3921, 4171, 4290, 4310, 4316, 4582, 4795, 4816, 4821, 4833, 4884, 4898, 4960, 5243, 6415, 6437, 6497, 6561, 6588, 6594, 6624, 6641, 6667, 6677, 6679, 6724, 6734, 7353, 7384, 7412, 7894, 7898, 7901, 11517, 11547, 11609, 12349, 12395, 12414, 12415, 12423, 12877, 12936, 12952, 12986, 12989, 12996, 13021, 13064, 13065, 70695, 70715, 70727, 91531, 94061, 94074, 94089, 94095, 94249, 94250, 94455, 94752, 94861, 95113, 95239, 99513, 100418, 100619, 100647, 100719, 100723, 100754, 100800, 100820, 100829, 100830, 101492, 101494, 101815, 102104, 102341, 102633, 102641, 102651, 102814, 102884, 102918, 103118, 103138, 103344, 103781, 103852, 103853, 103888, 104323, 104399, 104457, 104504, 104523, 104668, 104814, 104817, 104967, 105062, 105094, 105096, 105255, 105259, 105278, 105420, 105440, 105441, 105442, 105451, 105460, 105468, 105545, 105546, 105661, 105665, 105666, 105675, 105738, 105780, 105782, 105823, 105851, 105867, 105970, 106131, 106273, 106311, 106372, 106471, 106474, 106525, 106631, 106648, 106714, 106802, 106808, 106817, 106822, 106823, 106824, 106867, 106869, 107004, 107008, 107180, 107265, 107360, 107399, 107425, 107440, 107454, 110835, 112242, 113427, 113435, 114038, 114079, 114401, 114913, 115198, 115509, 116662, 116686, 116688, 116782, 116790, 116791, 116800, 116802, 116816, 116825, 116963, 116964, 117079, 117216, 117277, 117306, 117404, 117632, 117727, 117889, 117929, 118037, 118089, 118519, 118612, 118627, 118641, 118665, 118817, 118818, 118850, 119192, 119240, 119401, 119524, 119754, 119946, 120523, 120627, 121048, 122125, 122146, 123610, 123667, 125702, 125960, 141336, 142738, 150462, 150465, 150572, 154576, 154622, 154624, 154891, 155095, 155100, 155198, 155201, 155250, 155262, 155273, 155322, 155323, 155363, 155398, 155403, 155425, 155428, 155472, 155477, 157160, 157193, 157262, 157264, 157312, 157315, 157328, 157347, 157479, 157565, 157576, 157640, 200651, 203319, 238165, 410597, 873683]
# print('Running updateRecordsInList() method for Poles')
# myUpdatesCompletedDict = poletable.updateRecordsInList(recordidlist=reviewed_updates_oidlist_poles)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Poles')
# poletable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                              outfilename='PoleUpdatesMade_ByOIDlist')

#=======================================================================##
#============================Cross Arms=================================##
"""
PREVIOULSY RUN ON: 1/5/17; 1/6/17; 1/11/17
RECONCILED & POSTED ON: 1/11/17
EXECUTION NOTES: 1/5/17=>ServerOID was not included in the extract for the storm app. The STRUCTUREOBJECTID is the OID for the pole & I'll check for all duplicates in the file gdb; take those OIDs & check them manually. in the 8,211 crossarm units that were included in the storm response project, 178 have duplicate STRUCTUREOBJECTIDS meaning there are more than 1 cross arm for a pole. When exporting the records, they were probably exported in the same order of the of OIDs. Maybe I can use the order of OBJECTIDs in the file gdb to find the same order in the CrossArms in the SDE to get the order of crossarms for each pole.
"""
##=======================================================================##
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_crossarms.sde'
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_Poles_v5_11212016\StormAssessment_Demo_Poles_v5_11212016.gdb\Crossarm_Unit'
# desttable = sde_path + r'\GISADM.CrossArms'
# sourcefields = ["STRUCTUREOBJECTID", "DATEMODIFIED", "LASTUSER", "INSTALLYEAR", "NUMBERINSTALLED"]
# destfields = ["STRUCTUREOBJECTID", "DATEMODIFIED", "LASTUSER", "INSTALLYEAR", "NUMBERINSTALLED"]
# crossarmstable = GDBDataTableChanges.TableChanges(tablename='crossarms',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
# #
# print('Running findUpdatedRecords() method for Cross Arms')
# myPotentialUpdatesDict = crossarmstable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Cross Arms')
# crossarmstable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                              outfilename='CrossArms_AllPotentialUpdates')

# officialupdates_oidlist_crossarms = [2665, 93933, 94095, 94249, 102651, 104399, 104457, 104523, 105545, 105675, 123667]
# print('Running updateRecordsInList() method for Cross Arms')
# myUpdatesCompletedDict = crossarmstable.updateRecordsInList(recordidlist=officialupdates_oidlist_crossarms)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Cross Arms')
# crossarmstable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                   outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                   outfilename='CrossArmsUpdatesMade_ByOIDlist')


##=======================================================================##
##=================================Cutouts===============================##
""" PREVIOULSY RUN ON: 1/1/17; 1/11/17--still didn't work since the geometric network causes issues.
SUCCESSFULLY COMPLETED, RECONCILED & POSTED ON:
EXECUTION NOTES: not completing correctly. With error "RuntimeError: The modified geometry must be a different geometry instance from the feature's original geometry (e.g., a copy or new instance). [class name = GISADM.CutOut, object id = 471106]"
Either update locations manually or use reference here to edit geometric network: http://support.esri.com/technical-article/000010000

OIDs 1011 and 2008 were updated manually and didn't actually have any location change.
OIDs 2611 and 292541 were moved to odd locations & I'm awaiting Brandon's, Marj's, or Paula's review to see if those are valid moves.
"""
##=======================================================================##
# officialupdates_oidlist_cutouts = [1011, 2008, 2611, 292541]
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_cutouts.sde'
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Cutout'
# desttable = sde_path + r'\GISADM.Electric\GISADM.CutOut'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'SUBTYPECD', 'INSTALLYEAR']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'SHAPE@XY', 'SUBTYPECD', 'INSTALLYEAR']
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
##print('Exporting updates using exportUpdatesToCsv() method for Cutouts')
##cutouttable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
##                                             outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
##                                             outfilename='Cutouts_AllPotentialUpdates')

# print('Running updateRecordsInList() method for Cutouts')
# myUpdatesCompletedDict = cutouttable.updateRecordsInList(recordidlist=officialupdates_oidlist_cutouts)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Cross Arms')
# cutouttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                   outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                   outfilename='CutoutsUpdatesMade_ByOIDlist')
# ##=======================================================================##
# ##========================Pole Attachments===============================##
"""
PREVIOULSY RUN ON:
SUCCESSFULLY COMPLETED, RECONCILED & POSTED ON:
EXECUTION NOTES:
"""
##=======================================================================##
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_Poles_v5_11212016\StormAssessment_Demo_Poles_v5_11212016.gdb\Pole_Attachments_'
# desttable = sde_path + r'\GISADM.INSP_POLE_ATTACHMENTS'
# sourcefields = ['ServerOID', 'DATEMODIFIED', 'LASTUSER', 'INSPECTIONDATE', 'PHYSICALTYPE', 'FUNCTIONTYPE', 'ATTACHING_COMPANY', 'USEFORBILLING']
# destfields = ['OBJECTID', 'DATEMODIFIED', 'LASTUSER', 'INSPECTIONDATE', 'PHYSICALTYPE', 'FUNCTIONTYPE', 'ATTACHING_COMPANY', 'USEFORBILLING']
# poleattachtable = GDBDataTableChanges.TableChanges(tablename='cutouts',
#                        sourcetablepath=sourcetable,
#                        desttablepath=desttable,
#                        sourcefieldlist=sourcefields,
#                        destfieldlist=destfields,
#                        sdeConnection=sde_path)
#
# # print('Running findUpdatedRecords() method for Pole Attachments')
# # myPotentialUpdatesDict = poleattachtable.findUpdatedRecords()
# # for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Pole Attachments')
# poleattachtable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                              outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                              outfilename='PoleAttachments_AllPotentialUpdates')

# officialupdates_oidlist_poleattachments = [71838, 228497, 250806, 277743, 384897, 385989, 418353, 527705, 594623, 699063, 780400, 804869, 845405, 1198181, 1217489, 1242387, 1264821, 1274801, 1275516, 1276499, 1284862, 1299209, 1434909, 1442589, 1442590, 1442591, 1451577]
# print('Running updateRecordsInList() method for Pole Attachments')
# myUpdatesCompletedDict = crossarmstable.updateRecordsInList(recordidlist=officialupdates_oidlist_poleattachments)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Cross Arms')
# crossarmstable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                   outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                   outfilename='CrossArmsUpdatesMade_ByOIDlist')


##=======================================================================##
##===============================Anchor Units============================##
"""
PREVIOULSY RUN ON:
SUCCESSFULLY COMPLETED:
RECONCILED & POSTED ON:
EXECUTION NOTES:
"""
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

# print('Running findUpdatedRecords() method for Anchor_Unit')
# myPotentialUpdatesDict = anchorunittable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Anchor_Unit')
# anchorunittable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='AnchorUnits_AllPotentialUpdates')

## print('Running updateRecordsInList() method for Anchor Units')
## myUpdatesCompletedDict = anchorunittable.updateRecordsInList(recordidlist=officialupdates_oidlist_anchornit)
##  for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
##
## print('Exporting updates using exportUpdatesToCsv() method for Anchor Units')
## anchorunittable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
##                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
##                                    outfilename='AnchorUnits_UpdatesMade_ByOIDlist')

##=======================================================================##
##===============================Down Guys===============================##
"""
PREVIOULSY RUN ON: 1/9/2017
SUCCESSFULLY COMPLETED: 1/9/17
RECONCILED & POSTED ON: 1/9/17 - only one change in geometry. All other changes were recorded from the previous updates, when reverting the changes. I had already made the changes from the file gdb, but then didn't revert the changes that were "official changes". I ran this to simply check that all the "official changes" were successfully made.
EXECUTION NOTES: need to redo these changes
"""
##=======================================================================##
# officialupdates_oidlist_downguys = [66235, 72071, 84111, 90161, 90162, 90167, 90544, 90547, 100374, 109845, 622449]
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_downguys.sde'
# sourcetable = r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\AGOL_Downloads\StormAssessment_Demo_DatabaseFeatures_11212016\StormAssessment_Demo_DatabaseFeatures_11212016.gdb\Down_Guys'
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
# # print('Running updateRecords() method for DownGuy')
# # myPotentialUpdatesDict = downguytable.findUpdatedRecords()
# # for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
# #
# print('Exporting updates using exportUpdatesToCsv() method for Anchor_Unit')
# downguytable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                 outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                 outfilename='DownGuys_AllPotentialUpdates')
#
# print('Running updateRecordsInList() method for Down Guys')
# myUpdatesCompletedDict = downguytable.updateRecordsInList(recordidlist=officialupdates_oidlist_downguys)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Down Guys')
# downguytable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                 outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                 outfilename='OfficialUpdatesList_DownGuys_UpdatedByOIDList')

##=======================================================================##
##============================Line_Cutout_Unit===========================##
"""
PREVIOULSY RUN ON: 1/10/17-run for update in OID list; 1/10/17-run for findUpdates to see if there are additional updates outside of the OID list.
SUCCESSFULLY COMPLETED: 1/10/17; findUpdates results showed no additional changes.
RECONCILED & POSTED ON: review sent 1/11/17-awaiting Marj's & Paula's review.
"""
##=======================================================================##
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_linecutout.sde'
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
# # # #
# print('Running findUpdatedRecords() method for Line Cutout Unit')
# myPotentialUpdatesDict = linecutoutunittable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# print('Exporting potential updates using exportUpdatesToCsv() method for Line Cutout Unit')
# linecutoutunittable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                        outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                        outfilename='LineCutoutUnit_AllPotentialUpdatesMade')
# #
# officialupdates_oidlist_cutouts = [110, 1228, 2509, 3492, 206740, 294181]
# print('Running updateRecords() method for Line Cutout Unit')
# myUpdatesCompletedDict = linecutoutunittable.updateRecordsInList(recordidlist=officialupdates_oidlist_cutouts)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
# ##
# print('Exporting updates using exportUpdatesToCsv() method for Line Cutout Unit')
# linecutoutunittable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                        outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                        outfilename='LineCutoutUnit_UpdatesMade')


##=======================================================================##
##=================================Pedestals=============================##
"""No updates found in this feature class as of 1/10/17
PREVIOULSY RUN ON:
SUCCESSFULLY COMPLETED:
RECONCILED & POSTED ON:
EXECUTION NOTES:
"""
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
# myPotentialUpdatesDict = pedestalsttable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# pedestalsttable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Pedestals_AllPotentialUpdates')

# print('Running updateRecords() method for Pedestals')
# myUpdatesCompletedDict = pedestalsttable.updateRecordsInList(recordidlist=officialupdates_oidlist_transformers)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Pedestals')
# pedestalsttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Pedestals_UpdatesMade')


##=======================================================================##
##================================Transformers===========================##
"""
PREVIOULSY RUN ON: 1/10/17
SUCCESSFULLY COMPLETED: 1/10/17
RECONCILED & POSTED ON: no need to since all record changes were actually their related records.
EXECUTION NOTES: still have the geometry issues. Not running through full list of oids.
"""
##=======================================================================##
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM.sde'
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
# myPotentialUpdatesDict = transformerttable.findUpdatedRecords()
# for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
#
# transformerttable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Transformer_AllPotentialUpdates')

#
# officialupdates_oidlist_transformers = [22489, 33173, 37528, 4474, 6147, 6486, 6815, 9181, 11104]
# print('Running updateRecordsInList() method for Transformers using an OID list')
# myUpdatesCompletedDict = transformerttable.updateRecordsInList(recordidlist=officialupdates_oidlist_transformers,
#                                                                distancethreshold=10)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Transformers')
# transformerttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='Transfomer_UpdatesMade_fromOIDList')


##=======================================================================##
##============================Transformer Unit===========================##
"""
PREVIOULSY RUN ON: 1/10/17 for oidlist; 1/11/17
SUCCESSFULLY COMPLETED: 1/10/17; 1/11/17
RECONCILED & POSTED ON: awaiting Paula's & Marjorie's review; removed oid 151129 since Marj & Paula noticed the update year was 0.
EXECUTION NOTES:
"""
##=======================================================================##
# sde_path = r'Database Connections\gisarcfmprod.world_ksundeen_KIM_txunit.sde'
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
#
##print('Running findUpdatedRecords() method for Transformer Unit')
##myPotentialUpdatesDict = txunitttable.findUpdatedRecords(distancethreshold=10)
##
##for key, vals in myPotentialUpdatesDict.iteritems(): print(key,vals)
##txunitttable.exportUpdatesToCsv(tableDictionary=myPotentialUpdatesDict,
##                                outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
##                                outfilename='TxUnit_AllPotentialUpdates')

# officialupdates_oidlist_txunit = [26150, 7061, 7688, 7761, 7762, 7764, 7863, 7867, 7868, 7912, 8121, 10492, 10891, 10963, 11367, 11377, 11552, 11599, 11871, 12035, 12045, 12049, 12054, 12061, 12066, 12100, 12386, 12395, 12481, 13330, 13532, 13894, 13936, 13981, 14313, 14556, 17468, 17519, 17617, 17945, 18688, 18775, 18874, 22738, 22749, 23391, 26150, 26168, 26173, 26219, 26222, 26237, 26238, 26466, 26504, 26512, 26527, 26601, 35639, 36640, 37719]
# print('Running updateRecordsInList() method for Transformer Unit')
# myUpdatesCompletedDict = txunitttable.updateRecordsInList(recordidlist=officialupdates_oidlist_txunit,
#                                                     distancethreshold=5)
# for key, vals in myUpdatesCompletedDict.iteritems(): print(key,vals)
#
# print('Exporting updates using exportUpdatesToCsv() method for Transformer Units')
# txunitttable.exportUpdatesToCsv(tableDictionary=myUpdatesCompletedDict,
#                                    outputFolder=r'C:\code\trunk\Projects_Python\DataCompareAndUpdate\UpdatesOutputFiles',
#                                    outfilename='TxUnit_UpdatesMadeFromOIDList')
