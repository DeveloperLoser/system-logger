from os import system, getlogin
from keyboard import record
from ctypes import windll
from sys import executable, argv

c = (windll.shell32)
def Elevate():
    if not windll.shell32.IsUserAnAdmin():
        windll.shell32.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None)
        quit()

