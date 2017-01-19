class mmLicenseStatus:
    mmLicenseAlreadyInitialized   =0x32       # from enum mmLicenseStatus
    mmLicenseAvailable            =0xa        # from enum mmLicenseStatus
    mmLicenseCheckedIn            =0x50       # from enum mmLicenseStatus
    mmLicenseCheckedOut           =0x46       # from enum mmLicenseStatus
    mmLicenseFailure              =0x28       # from enum mmLicenseStatus
    mmLicenseNotInitialized       =0x3c       # from enum mmLicenseStatus
    mmLicenseNotLicensed          =0x14       # from enum mmLicenseStatus
    mmLicenseRetired              =0x5a       # from enum mmLicenseStatus
    mmLicenseUnavailable          =0x1e       # from enum mmLicenseStatus

class mmLicensedProductCode:
    mmLPAll                       =0x64       # from enum mmLicensedProductCode
    mmLPArcFM                     =0x5        # from enum mmLicensedProductCode
    mmLPArcFMViewer               =0x3        # from enum mmLicensedProductCode
    mmLPDesigner                  =0x6        # from enum mmLicensedProductCode
    mmLPDesignerExpress           =0xe        # from enum mmLicensedProductCode
    mmLPDesignerStaker            =0xd        # from enum mmLicensedProductCode
    mmLPEngine                    =0x1        # from enum mmLicensedProductCode
    mmLPEngineViewer              =0x2        # from enum mmLicensedProductCode
    mmLPEnterprise                =0x64       # from enum mmLicensedProductCode
    mmLPError                     =0x3e8      # from enum mmLicensedProductCode
    mmLPGeodatabaseManager        =0xc        # from enum mmLicensedProductCode
    mmLPNone                      =0x0        # from enum mmLicensedProductCode
    mmLPResponderDataServices     =0x8        # from enum mmLicensedProductCode
    mmLPResponderDispatch         =0x4        # from enum mmLicensedProductCode
    mmLPResponderPrediction       =0x9        # from enum mmLicensedProductCode
    mmLPServer                    =0x7        # from enum mmLicensedProductCode
    mmLPServerAdvanced            =0xb        # from enum mmLicensedProductCode
    mmLPServerReader              =0xa        # from enum mmLicensedProductCode

class mmLicensedExtensionCode:
    mmLXEngineEditor              =0x1        # from enum mmLicensedExtensionCode
    mmLXInspector                 =0x3        # from enum mmLicensedExtensionCode
    mmLXNetworkAdapter            =0x4        # from enum mmLicensedExtensionCode
    mmLXNone                      =0x0        # from enum mmLicensedExtensionCode
    mmLXRedliner                  =0x2        # from enum mmLicensedExtensionCode

class mmAutoUpdaterMode:
    mmAUMNotSet                   =0x0        # from enum mmAutoUpdaterMode
    mmAUMArcMap                   =0x1        # from enum mmAutoUpdaterMode
    mmAUMArcCatalog               =0x2        # from enum mmAutoUpdaterMode
    mmAUMStandAlone               =0x4        # from enum mmAutoUpdaterMode
    mmAUMNoEvents                 =0x8        # from enum mmAutoUpdaterMode
    mmAUMFeederManager            =0x10       # from enum mmAutoUpdaterMode
    mmConflictResolution          =0x20       # from enum mmAutoUpdaterMode
    mmAUMMobileImport             =0x40       # from enum mmAutoUpdaterMode
    mmAUMMobileExtract            =0x80       # from enum mmAutoUpdaterMode
    mmAUMPhaseSwap                =0x100      # from enum mmAutoUpdaterMode
    mmAUMRemoveFromDesign         =0x200      # from enum mmAutoUpdaterMode
    
class mmRuntimeMode:
    mmRuntimeModeUnknown 	  =-0x1	      # from enum mmRuntimeMode
    mmRuntimeModeNone 		  =0x0	      # from enum mmRuntimeMode
    mmRuntimeModeArcMap 	  =0x1	      # from enum mmRuntimeMode
    mmRuntimeModeArcCatalog 	  =0x2	      # from enum mmRuntimeMode
    mmRuntimeModeArcEngine 	  =0x3	      # from enum mmRuntimeMode
    mmRuntimeModeArcServer 	  =0x4	      # from enum mmRuntimeMode
    mmRuntimeModeEngineViewer 	  =0x5	      # from enum mmRuntimeMode
    mmRuntimeModeDesignerStaker   =0x6	      # from enum mmRuntimeMode