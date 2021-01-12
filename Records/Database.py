from tkinter import *
from sqlite3 import *
win=Tk()
win.title('DataBase')
win.geometry('500x500')

#DataBase

#Creating a data base or connect to it
database=connect('address_book.db')

# Create cursor for using sqlite commands
c=database.cursor()

# create table using execute() to execute some sql commands in quatation marks
# CREATE TABLE tableName(name of columns) to create columns of table
# DataType in sqlite=text,integer,wholenumbers,blob(for storing images)
# You need to create the table one type
c.execute("""
CREATE TABLE Addresses(
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zip integer
                    )
                        """)
# only needed one time                        

# commit to save changes
database.commit()

# close connection
database.close()

win.mainloop()


#EXECUTE OPTIONS:-
#1->CREATE TABLE tablename(name of columns)
#2->INSERT INTO tablename VALUE(:anyvariable,:anyvariable...),
# { 'anyvariable same as in values':ENTRY,...}
#3->SELECT *,oid FROM tablename
#4->fetchall
#5->'DELETE from tablename WHERE oid=' + (entryButton).get()
#6->'SELECT * FROM tablename WHERE oid='+record_id 
#7->UPDATE Addresses SET samevariable as in step 2:anyvariable,...
                #WHERE oid=:oid
                # { 'anyvariable same as in values':ENTRY,...}