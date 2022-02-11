

import shutil
import os

# set where the source files are contained
source = 'C:\\Users\\sseyl\\OneDrive\\Documents\\The Tech Academy\\python\\fileTransfer\\folderA\\'

# set destination path
destination = 'C:\\Users\\sseyl\\OneDrive\\Documents\\The Tech Academy\\python\\fileTransfer\\folderB\\'
files = os.listdir(source)

for i in files:
    # move the files represented by 'i' to new destination folder
    shutil.move(source+i, destination)
    
