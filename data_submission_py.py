import sqlite3

conn=sqlite3.connect('data1.db')

with conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_script TEXT)")
    conn.commit()

conn=sqlite3.connect('data1.db')

#tuple of files
fileList=('information.docx','Hello.txt','myImage.png', \
          'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#loop through each object in tuple to find files that are "txt"
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur=conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_script) VALUES (?)", (x,))
            print(x)

conn.close()
