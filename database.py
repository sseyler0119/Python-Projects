#
# Python: 3.10.1
#
# Author: Serena Seyler
#
# Purpose: The Tech Academy, Database python script using sqlite3

import sqlite3

# declare fileLIst var, and populate with file names
fileList = ('information.docx','Hello.txt', 'myImage.png', \
            'myMovie.mpg','World.txt', 'data.pdf', 'myPhoto.jpg')


def createTable():
    #connect to database, create if does not already exist
    conn = sqlite3.connect('filename.db')
    
    # while conn is open, do the following
    with conn:
        cur = conn.cursor() # cursor
        # create table if it does not already exist, two columns one integer primary key,
        #   second column is text datatype 'col_filename'
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_textfiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT \
            )") # end of statement
        conn.commit() #commit to database
    conn.close() #close connection


# function to add selected files to database
def addFiles():
    conn = sqlite3.connect('filename.db')
      # while conn is open, do the following
    with conn:
        cur = conn.cursor() # cursor
        for i in fileList: # iterate through list
            if i.endswith('.txt'): # just the text files
                cur.execute("INSERT INTO tbl_textfiles(col_filename) VALUES (?)",[i]) # insert into table
                conn.commit() # commit to database
    conn.close() # close connection

# print result
def printResult():
    conn = sqlite3.connect('filename.db')
    # while conn is open, do the following
    with conn:
        cur = conn.cursor() # cursor
        cur.execute("SELECT col_filename FROM tbl_textfiles")
        result = cur.fetchall()

        for item in result:
            msg = "Filename: {}".format(item[0])
            print(msg)
            
        
if __name__ == "__main__":
    createTable()
    addFiles()
    printResult()
