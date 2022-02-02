from tkinter import *
import tkinter as tk

# import modules
import fileTransferMain
import fileTransferFunc

def loadGui(self):

    # buttons
    self.btnSrc = Button(self.master, text="Browse...", width =13, command=lambda: fileTransferFunc.selectSrc(self))
    self.btnSrc.grid(row = 0, column = 0, padx=(10,0), pady=(30,0), sticky=W)
    self.btnDst = Button(self.master, text="Browse...", width =13, command=lambda: fileTransferFunc.selectDest(self))
    self.btnDst.grid(row = 1, column = 0, padx=(10,0), pady=(30,0), sticky=W)
    self.btnFileCheck = Button(self.master, text="Check Files", width=13, command=lambda: fileTransferFunc.moveFiles(self))
    self.btnFileCheck.grid(row = 2, column = 0, padx=(10,0), pady=(30,10), sticky=W)
    
    # textboxes
    self.txtSrc = Entry(self.master, width = 50)
    self.txtSrc.grid(row = 0, column = 1, rowspan=1, columnspan = 2, padx=(30, 0), pady=(30,0), sticky = N+E+W)
    self.txtDst = Entry(self.master, width = 50)
    self.txtDst.grid(row = 1, column = 1, rowspan=1, columnspan = 2, padx=(30, 0), pady=(30,0), sticky = N+E+W)


if __name__ == "__main__":
    pass
