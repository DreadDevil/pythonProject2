import shutil
import os
import sys

if(len(sys.argv) < 4):
    print("Missing arguments!")
    exit(1)

file_name = sys.argv[1]
initialize = int(sys.argv[2])
lognumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size
    logfile_size = logfile_size / 1024
    if(logfile_size >= limitsize):
        if(lognumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                