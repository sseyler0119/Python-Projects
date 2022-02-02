

from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk
import os
import time
import shutil

# import modules
import fileTransferGui
import fileTransferMain

# select source folder
def selectSrc(self):
    name = fd.askdirectory()
    self.txtSrc.delete(0,END)
    self.txtSrc.insert(END, name)
    return name

# select destination folder
def selectDest(self):
    name = fd.askdirectory()
    self.txtDst.delete(0, END)
    self.txtDst.insert(END, name)
    return name

# get modification time of passed in filename
def getModificationTime(filename):
    modTime = os.path.getmtime(filename) 
    return modTime

# move modified files from source folder to destination folder
def moveFiles(self):
    src = self.txtSrc.get() # get source folder location from textbox
    dst = self.txtDst.get() # get destination folder location from textbox

    currentTime = time.time() # get current time
    SECONDS_IN_DAY = 24*60*60 # total seconds in full day
    olderFiles = currentTime - SECONDS_IN_DAY # files older than 24 hours

    # iterate through directory, check each file
    for filename in os.listdir(src):
        srcFile = os.path.join(src, filename) # join filename to path
        if getModificationTime(srcFile) > olderFiles: # only files that are newer than olderFiles
            dstFile = os.path.join(dst, filename) # join filename to path
            shutil.move(srcFile, dstFile) # move files


            
if __name__ == "__main__":
    pass
