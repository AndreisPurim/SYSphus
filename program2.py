import wmi

known_processes = {
    "windows_necessary": ["System Idle Process", "explorer.exe", "taskmgr.exe", "spoolsv.exe", "lsass.exe", "csrss.exe", "smss.exe", "winlogon.exe", "svchost.exe","services.exe", "System", "Registry", "wininit.exe", "WUDFHost.exe", "MsMpEng.exe", "fontdrvhost.exe", "dwm.exe", "igfxCUIService.exe", "Memory Compression", "CxAudMsg64.exe", "esif_uf.exe", "SearchFilterHost.exe", "SearchProtocolHost.exe","SASrv.exe","dasHost.exe","dllhost.exe","dptf_helper.exe","sihost.exe","taskhostw.exe","PresentationFontCache.exe","ctfmon.exe","igfxEM.exe","igfxHK.exe","igfxTray.exe","StartMenuExperienceHost.exe", "RuntimeBroker.exe","LockApp.exe", "ShellExperienceHost.exe", "CAudioFilterAgent64.exe", "SecurityHealthService.exe","SecurityHealthSystray.exe", "SmartAudio.exe", "SgrmBroker.exe","ApplicationFrameHost.exe","usocoreworker.exe","SystemSettings.exe","ApplicationFrameHost.exe","SystemSettingsBroker.exe","MusNotifyIcon.exe","NisSrv.exe","rundll32.exe","SearchUI.exe","srtasks.exe","OfficeClickToRun.exe","conhost.exe","AppVShNotify.exe","SearchIndexer.exe","pacjsworker.exe","audiodg.exe","WmiPrvSE.exe","backgroundTaskHost.exe"],
    "us": ["python.exe", "cmd.exe"],
    "asus": ["AsusTPLoader.exe", "SgrmBroker.exe","AsusTPHelper.exe","AsusTPCenter.exe"],
    "adobe": ["armsvc.exe"],
    "google": ["GoogleCrashHandler.exe","GoogleCrashHandler64.exe"],
    "onedrive": ["OneDrive.exe"],
    "fingertip_identifier": ["valWBFPolicyService.exe"],
    "calculator": ["Calculator.exe"],
    "Yourphone": ["YourPhone.exe"],
}
not_permitted = {
    "browser": ["brave.exe"],
    "code": ["Code.exe"],
    "entertainement": ["steam.exe","steamwebhelper.exe","SteamService.exe"],
}
delete = {
    
}

known_processes_list = []
not_permitted_list = []
def reemovNestings(l, output):
    for i in l:
        if type(i) == list:
            reemovNestings(i,output)
        else:
            output.append(i)
reemovNestings(known_processes.values(),known_processes_list)
reemovNestings(not_permitted.values(),not_permitted_list)

# Initializing the wmi constructor
f = wmi.WMI()
 
# Printing the header for the later columns
print("pid   Process name")
 
# Iterating through all the running processes
for process in f.Win32_Process():
     
    # Displaying the P_ID and P_Name of the process
    
    if(not process.Name in known_processes_list and not process.Name in not_permitted_list):
       print(f"{process.ProcessId:<10} {process.Name}")
    