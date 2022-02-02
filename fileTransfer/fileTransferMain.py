

from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk


# import modules
import fileTransferGui
import fileTransferFunc

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master frame configuration
        self.master = master
        self.master.minsize(500, 200) # height, width
        self.master.maxsize(500,200)
        self.master.title("Copy Files")

        arg = self.master

        # load GUI
        fileTransferGui.loadGui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
