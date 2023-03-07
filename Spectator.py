from os import system
from time import sleep
from tkinter import messagebox
from multiprocessing import Process

# Seperate file due to multi processing being required
def Watcher():
    watcherProcess = Process(target=Watcher)
    watcherProcess.start()
    while 1:
        if not (system("tasklist /fi \"IMAGENAME eq notepad.exe\"") == "INFO: No tasks are running which match the specified criteria."):
            print("kill")
            system("taskkill /IM notepad.exe")


if __name__ == "__main__":
    Watcher()