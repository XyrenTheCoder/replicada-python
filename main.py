'''
<DISCLAIMER>
THIS CODE REPLICATES ITSELF AND WILL CREATE NEW DIRECTORIES
PLEASE MIND THAT THIS WOULD FUCK UP YOUR DIRECTORIES, INCLUDING FILES AND FOLDERS
***DO NOT RUN THIS FILE IN ANY IMPORTANT DIRECTORIES***

self-replicating python file - Replicada by archisha69
'''

import os, shutil, time, random, string

cwd = os.getcwd()

count = 0

while count < 200:
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 32)))
    time.sleep(1) #cooldown, lower the value to make the process faster, higher the value to make the process slower (prevent lags)
    os.mkdir(name)
    os.chdir(name)
    shutil.copy(f"../{sys.argv[0]}", os.getcwd())
    os.chdir(cwd)
    count += 1
    
# if count == 200:
#     all = os.listdir(cwd)
#     for dir in all:
#         if dir == "main.py": pass #skip existed (this file) main.py in current directory, if you already have 1 file named "main.py" in current working directory (cwd), please change the name of this file and change "main.py" in this line to this file's name after changes
#         else:
#             time.sleep(1)
#             shutil.copy(f"{cwd}{sep}main.py", dir) #copies itself (remember to change file name) to all directories in cwd
