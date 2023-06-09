; Script generated by the HM NIS Edit Script Wizard.

; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "Sorting Visualizer"
!define PRODUCT_VERSION "1.0"
!define PRODUCT_PUBLISHER "CLiF and Syeosle"
!define PRODUCT_WEB_SITE "https://github.com/CLiF-1593/SortingVisualizer"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\main.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "..\Icon\Icon.ico"
!define MUI_UNICON "..\Icon\Icon.ico"

; Language Selection Dialog Settings
!define MUI_LANGDLL_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_LANGDLL_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_LANGDLL_REGISTRY_VALUENAME "NSIS:Language"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\main.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "French"
!insertmacro MUI_LANGUAGE "German"
!insertmacro MUI_LANGUAGE "Japanese"
!insertmacro MUI_LANGUAGE "Korean"
!insertmacro MUI_LANGUAGE "Russian"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$PROGRAMFILES\Sorting Visualizer"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Function .onInit
  !insertmacro MUI_LANGDLL_DISPLAY
FunctionEnd

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite try
  File "..\dist\main\base_library.zip"
  SetOutPath "$INSTDIR\icon"
  File "..\dist\main\icon\Icon.png"
  SetOutPath "$INSTDIR\font"
  File "..\dist\main\font\font.ttf"
  SetOutPath "$INSTDIR"
  File "..\dist\main\libcrypto-1_1-x64.dll"
  File "..\dist\main\libopenblas.XWYDX2IKJW2NMTWSFYNGFUWKQU3LYTCZ.gfortran-win_amd64.dll"
  File "..\dist\main\libssl-1_1-x64.dll"
  File "..\dist\main\main.exe"
  CreateDirectory "$SMPROGRAMS\Sorting Visualizer"
  CreateShortCut "$SMPROGRAMS\Sorting Visualizer\Sorting Visualizer.lnk" "$INSTDIR\main.exe"
  CreateShortCut "$DESKTOP\Sorting Visualizer.lnk" "$INSTDIR\main.exe"
  SetOutPath "$INSTDIR\numpy\core"
  File "..\dist\main\numpy\core\_multiarray_tests.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\core\_multiarray_umath.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\numpy\fft"
  File "..\dist\main\numpy\fft\_pocketfft_internal.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\numpy\linalg"
  File "..\dist\main\numpy\linalg\lapack_lite.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\linalg\_umath_linalg.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\numpy\random"
  File "..\dist\main\numpy\random\bit_generator.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\mtrand.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\_bounded_integers.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\_common.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\_generator.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\_mt19937.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\_pcg64.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\_philox.cp37-win_amd64.pyd"
  File "..\dist\main\numpy\random\_sfc64.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR\pyaudio"
  File "..\dist\main\pyaudio\_portaudio.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR"
  File "..\dist\main\pyexpat.pyd"
  SetOutPath "$INSTDIR\PyQt5\Qt5\bin"
  File "..\dist\main\PyQt5\Qt5\bin\d3dcompiler_47.dll"
  File "..\dist\main\PyQt5\Qt5\bin\libegl.dll"
  File "..\dist\main\PyQt5\Qt5\bin\libglesv2.dll"
  File "..\dist\main\PyQt5\Qt5\bin\MSVCP140.dll"
  File "..\dist\main\PyQt5\Qt5\bin\MSVCP140_1.dll"
  File "..\dist\main\PyQt5\Qt5\bin\opengl32sw.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5Core.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5DBus.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5Gui.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5Network.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5Qml.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5QmlModels.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5Quick.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5Svg.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5WebSockets.dll"
  File "..\dist\main\PyQt5\Qt5\bin\Qt5Widgets.dll"
  File "..\dist\main\PyQt5\Qt5\bin\VCRUNTIME140_1.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt5\plugins\generic"
  File "..\dist\main\PyQt5\Qt5\plugins\generic\qtuiotouchplugin.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt5\plugins\iconengines"
  File "..\dist\main\PyQt5\Qt5\plugins\iconengines\qsvgicon.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt5\plugins\imageformats"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qgif.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qicns.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qico.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qjpeg.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qsvg.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qtga.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qtiff.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qwbmp.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\imageformats\qwebp.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt5\plugins\platforms"
  File "..\dist\main\PyQt5\Qt5\plugins\platforms\qminimal.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\platforms\qoffscreen.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\platforms\qwebgl.dll"
  File "..\dist\main\PyQt5\Qt5\plugins\platforms\qwindows.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt5\plugins\platformthemes"
  File "..\dist\main\PyQt5\Qt5\plugins\platformthemes\qxdgdesktopportal.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt5\plugins\styles"
  File "..\dist\main\PyQt5\Qt5\plugins\styles\qwindowsvistastyle.dll"
  SetOutPath "$INSTDIR\PyQt5\Qt5\translations"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_ar.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_bg.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_ca.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_cs.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_da.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_de.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_en.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_es.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_fi.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_fr.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_gd.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_he.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_hu.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_it.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_ja.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_ko.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_lv.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_pl.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_ru.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_sk.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_tr.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_uk.qm"
  File "..\dist\main\PyQt5\Qt5\translations\qtbase_zh_TW.qm"
  SetOutPath "$INSTDIR\PyQt5"
  File "..\dist\main\PyQt5\QtCore.pyd"
  File "..\dist\main\PyQt5\QtGui.pyd"
  File "..\dist\main\PyQt5\QtWidgets.pyd"
  File "..\dist\main\PyQt5\sip.cp37-win_amd64.pyd"
  SetOutPath "$INSTDIR"
  File "..\dist\main\python3.dll"
  File "..\dist\main\python37.dll"
  File "..\dist\main\select.pyd"
  File "..\dist\main\unicodedata.pyd"
  File "..\dist\main\VCRUNTIME140.dll"
  File "..\dist\main\_asyncio.pyd"
  File "..\dist\main\_bz2.pyd"
  File "..\dist\main\_contextvars.pyd"
  File "..\dist\main\_ctypes.pyd"
  File "..\dist\main\_decimal.pyd"
  File "..\dist\main\_hashlib.pyd"
  File "..\dist\main\_lzma.pyd"
  File "..\dist\main\_multiprocessing.pyd"
  File "..\dist\main\_overlapped.pyd"
  File "..\dist\main\_queue.pyd"
  File "..\dist\main\_socket.pyd"
  File "..\dist\main\_ssl.pyd"
SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\Sorting Visualizer\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\Sorting Visualizer\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\main.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\main.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

Function un.onInit
!insertmacro MUI_UNGETLANGUAGE
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\_ssl.pyd"
  Delete "$INSTDIR\_socket.pyd"
  Delete "$INSTDIR\_queue.pyd"
  Delete "$INSTDIR\_overlapped.pyd"
  Delete "$INSTDIR\_multiprocessing.pyd"
  Delete "$INSTDIR\_lzma.pyd"
  Delete "$INSTDIR\_hashlib.pyd"
  Delete "$INSTDIR\_decimal.pyd"
  Delete "$INSTDIR\_ctypes.pyd"
  Delete "$INSTDIR\_contextvars.pyd"
  Delete "$INSTDIR\_bz2.pyd"
  Delete "$INSTDIR\_asyncio.pyd"
  Delete "$INSTDIR\VCRUNTIME140.dll"
  Delete "$INSTDIR\unicodedata.pyd"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\python37.dll"
  Delete "$INSTDIR\python3.dll"
  Delete "$INSTDIR\PyQt5\sip.cp37-win_amd64.pyd"
  Delete "$INSTDIR\PyQt5\QtWidgets.pyd"
  Delete "$INSTDIR\PyQt5\QtGui.pyd"
  Delete "$INSTDIR\PyQt5\QtCore.pyd"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_zh_TW.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_uk.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_tr.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_sk.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_ru.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_pl.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_lv.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_ko.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_ja.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_it.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_hu.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_he.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_gd.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_fr.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_fi.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_es.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_en.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_de.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_da.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_cs.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_ca.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_bg.qm"
  Delete "$INSTDIR\PyQt5\Qt5\translations\qtbase_ar.qm"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\styles\qwindowsvistastyle.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\platformthemes\qxdgdesktopportal.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\platforms\qwindows.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\platforms\qwebgl.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\platforms\qoffscreen.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\platforms\qminimal.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qwebp.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qwbmp.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qtiff.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qtga.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qsvg.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qjpeg.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qico.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qicns.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\imageformats\qgif.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\iconengines\qsvgicon.dll"
  Delete "$INSTDIR\PyQt5\Qt5\plugins\generic\qtuiotouchplugin.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\VCRUNTIME140_1.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5Widgets.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5WebSockets.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5Svg.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5Quick.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5QmlModels.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5Qml.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5Network.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5Gui.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5DBus.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\Qt5Core.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\opengl32sw.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\MSVCP140_1.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\MSVCP140.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\libglesv2.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\libegl.dll"
  Delete "$INSTDIR\PyQt5\Qt5\bin\d3dcompiler_47.dll"
  Delete "$INSTDIR\pyexpat.pyd"
  Delete "$INSTDIR\pyaudio\_portaudio.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\_sfc64.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\_philox.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\_pcg64.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\_mt19937.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\_generator.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\_common.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\_bounded_integers.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\mtrand.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\random\bit_generator.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\linalg\_umath_linalg.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\linalg\lapack_lite.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\fft\_pocketfft_internal.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\core\_multiarray_umath.cp37-win_amd64.pyd"
  Delete "$INSTDIR\numpy\core\_multiarray_tests.cp37-win_amd64.pyd"
  Delete "$INSTDIR\main.exe"
  Delete "$INSTDIR\libssl-1_1-x64.dll"
  Delete "$INSTDIR\libopenblas.XWYDX2IKJW2NMTWSFYNGFUWKQU3LYTCZ.gfortran-win_amd64.dll"
  Delete "$INSTDIR\libcrypto-1_1-x64.dll"
  Delete "$INSTDIR\icon\Icon.png"
  Delete "$INSTDIR\font\font.ttf"
  Delete "$INSTDIR\base_library.zip"

  Delete "$SMPROGRAMS\Sorting Visualizer\Uninstall.lnk"
  Delete "$SMPROGRAMS\Sorting Visualizer\Website.lnk"
  Delete "$DESKTOP\Sorting Visualizer.lnk"
  Delete "$SMPROGRAMS\Sorting Visualizer\Sorting Visualizer.lnk"

  RMDir "$SMPROGRAMS\Sorting Visualizer"
  RMDir "$INSTDIR\PyQt5\Qt5\translations"
  RMDir "$INSTDIR\PyQt5\Qt5\plugins\styles"
  RMDir "$INSTDIR\PyQt5\Qt5\plugins\platformthemes"
  RMDir "$INSTDIR\PyQt5\Qt5\plugins\platforms"
  RMDir "$INSTDIR\PyQt5\Qt5\plugins\imageformats"
  RMDir "$INSTDIR\PyQt5\Qt5\plugins\iconengines"
  RMDir "$INSTDIR\PyQt5\Qt5\plugins\generic"
  RMDir "$INSTDIR\PyQt5\Qt5\bin"
  RMDir "$INSTDIR\PyQt5"
  RMDir "$INSTDIR\pyaudio"
  RMDir "$INSTDIR\numpy\random"
  RMDir "$INSTDIR\numpy\linalg"
  RMDir "$INSTDIR\numpy\fft"
  RMDir "$INSTDIR\numpy\core"
  RMDir "$INSTDIR\icon"
  RMDir "$INSTDIR\font"
  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd