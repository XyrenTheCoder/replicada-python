'''
THIS CODE COPIES ITSELF AND WILL CREATE NEW DIRECTORIES,
PLEASE MIND THAT THIS WOULD PROBABLY DESTORY (maybe) UR NICE DIRECTORY AND MAKING IT MESSY.
DO NOT RUN THIS FILE IN ANY IMPORTANT DIRECTORIES

self-replicating python file by archisha69
'''

import os, shutil, time, random, string

sep = "\\" if os.name == "nt" else "/"
cwd = os.getcwd()

count = 0

while count < 10: #change value to whatever amount of directories you want it to create, beware of this could lag your devices
    time.sleep(1) #cooldown, lower the value to make the process faster, higher the value to make the process slower (prevent lags)
    os.mkdir(f"{cwd}{sep}{name}{count}") #created directory name will be random printable characters
    count += 1
    
if count == 10:
    all = os.listdir(cwd) #returns a list of all current directories
    for dir in all:
        name = ''.join(random.choice(string.printable)
        if dir == "main.py": pass #skip existed (this file) main.py in current directory, if you already have 1 file named "main.py" in current working directory (cwd), please change the name of this file and change "main.py" in this line to this file's name after changes
        else:
            time.sleep(1) #cooldown, as same as the previous one
            shutil.copy(f"{cwd}{sep}main.py", dir) #copies itself to all directories in cwd
