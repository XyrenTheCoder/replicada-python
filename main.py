import os, shutil
import time

sep = "\\" if os.name == "nt" else "/"
cwd = os.getcwd()

count = 0

while count < 10:
    time.sleep(1)
    os.mkdir(f"{cwd}{sep}test{count}")
    count += 1
    
if count == 10:
    all = os.listdir(cwd).remove("main.py")
    for dir in all:
        if dir == f"{cwd}{sep}main.py": pass
        else:
            time.sleep(1)
            shutil.copy(f"{cwd}{sep}main.py", dir)
    
