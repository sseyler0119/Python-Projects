from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk
import webbrowser as wb
import os

class ParentWindow(Frame):

    def __init__(self, master):
        Frame.__init__(self) # initialize frame

        self.filename = StringVar()
        self.fileText = StringVar()
            
        
        def createPage(self):
            self.filename = self.filename.get() + ".html" # append .html file extension to filename
            
            if os.path.exists("{}".format(self.filename)): # filename already exists, clear file
                os.remove("{}".format(self.filename))
            else:
                pass
            file = open("{}".format(self.filename), "a") # create new file
            # write text extracted from textbox (fileText) to filename with HTML appended
            file.write("<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>".format(self.fileText.get()))
            file.close() # close file
            file = open("{}".format(self.filename), "r") # open file as read only
            wb.open_new_tab(self.filename) # open file in a tab in web browser


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(560, 190))
        self.master.title('Create WebPage')


        # labels
        self.lblFilename = tk.Label(self.master, text='Enter Filename: ')
        self.lblFilename.grid(row=0, column=0, padx=(30, 20), pady=(10, 10), sticky=N+W)
        self.lblFileText = tk.Label(self.master, text='Enter Webpage Text: ')
        self.lblFileText.grid(row=1, column=0, padx=(30, 20), pady=(10, 10), sticky=N+W)

        # textboxes
        self.txtFilename = tk.Entry(self.master, width=50, text=self.filename)
        self.txtFilename.grid(row=0, column=1, columnspan=4, padx=(30, 20), pady=(10, 10), sticky=N+E+W)
        self.txtFileText = tk.Entry(self.master, width=50,text=self.fileText)
        self.txtFileText.grid(row=1, column=1, columnspan=4, padx=(30, 20), pady=(10, 10), sticky=N+E+W)
        

        #buttons
        self.btn_submit = tk.Button(self.master, width=12, height=2, text='Submit', command=lambda: createPage(self))
        self.btn_submit.grid(row=2, column=0, padx=(30, 20), pady=(10, 10), sticky=N+E+W)

# main driver
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
