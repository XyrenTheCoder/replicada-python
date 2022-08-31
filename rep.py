import os, shutil
#import time

sep = "\\" if os.name == "nt" else "/"
cwd = os.getcwd()
all = os.listdir()

for dir in all:
  shutil.copy(f"{cwd}{sep}rep.py", dir)
  #time.sleep(0.3)
