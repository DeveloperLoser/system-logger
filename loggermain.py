from keyboard import record
import ctypes #Funny C in Py
import os


#Applications infact do not get left alone by UAC if launched as admin. Screw you dude on stack overflow thread from 7 years ago, its you and not 7 years
def Log():
    output = open(('C:/Users/' + str(os.getlogin()) + '/Desktop/log.txt'), 'w') # TODO getlogin might retun the user who elevated it
    r = record(until='`')
    r = str(r)
    r = r.replace("KeyboardEvent(", '')
    r = r.replace(',', '')
    r = r.replace("down)", ',')
    r = r.replace("up)", '\'')
    output.write(r)

if __name__ == "__main__":
    Log()