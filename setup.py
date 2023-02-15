#The gateway to the Distutils: do everything your setup script needs
#to do, in a highly flexible and user-driven way. Briefly: create a Distribution instance;
#find and parse config files; parse the command line; run each Distutils command found there
#customized by the options supplied to 'setup()' (as keyword arguments)
#in config files, and on the command line.
from distutils.core import setup 
import py2exe
import keyboard
import ctypes
import sys

setup (console=['loggermain.py'])