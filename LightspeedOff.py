import ctypes
from os import system
from keyboard import add_hotkey, wait

c = (ctypes.windll.shell32)
#Termination of lightspeed apps needs elevated perms
def Kill():
    add_hotkey('ctrl+shift+`', Stop)
    while 1:
        system('taskkill /F /IM \"LSFilter.exe\"')
        system('taskkill /F /IM \"LSProxy.exe\"')
        system('taskkill /F /IM \"LSSASvc.exe\"')
        system('taskkill /F /IM \"LMA.exe\"')
    return

def Stop():
    print("stopping")
    quit()

if __name__ == "__main__":
        Kill()
    