from tkinter import *
from sqlite3 import *
win=Tk()
win.title('DataBase')
#configure(background) is used to set background color
win.configure(background='skyblue',borderwidth=5)




def Submit():
    #DataBase
    database=connect('address_book.db')
    c=database.cursor()

    #Inserting in table
    #INSERT INTO tablename VALUES(:anyvariable,:anyvariable...) is used to insert data into table
    # and then create dictionary
    c.execute('INSERT INTO Addresses VALUES(:first_name,:last_name,:address,:city,:state,:zip)',
                {'first_name':first_name_entry.get(),
                 'last_name':last_name_entry.get(),
                 'address':address_entry.get(),
                 'city':city_entry.get(),
                 'state':state_entry.get(),
                 'zip':zip_entry.get()})
            
    database.commit()
    database.close()
    #(ccecc)->connect-cursor-execute-commit-close

    #Deleting the written entry after submittion
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    zip_entry.delete(0,END)

def ShowRecords():
    #DataBase
    database=connect('address_book.db')
    c=database.cursor()

    #Show the dataBase
    # SELECT *(everything),oid(ID) FROM (TableName) is used to select table from *.db file
    c.execute('SELECT *,oid FROM Addresses')
    #fetchall()->fetch all the records,fetchone()->fetch one record,fetchmany(no.)->fetch no. of records
    records=c.fetchall()
    

    #Creating loop to show results
    print_record=''
    for record in records:
        print_record+=str(record[6])+' '+str(record[0])+' '+str(record[1])+"\n"

    show_records=Label(win,text=print_record,bg='yellow',fg='purple')
    show_records.grid(row=8,column=0,columnspan=3)

    database.commit()
    database.close()
    #(ccecc)->connect-cursor-execute-commit-close

# Create function to delete a record


def Delete():
    #DataBase
    database=connect('address_book.db')
    c=database.cursor()

    c.execute('DELETE from Addresses WHERE oid='+delete_entry.get())

    database.commit()
    database.close()
    #(ccecc)->connect-cursor-execute-commit-close

#save button function
def Save():
    global editor
    #DataBase
    database=connect('address_book.db')
    c=database.cursor()
    
    record_id=delete_entry.get()
    c.execute('''UPDATE Addresses SET
                first_name=:first,
                last_name=:last,
                address=:address,
                state=:state,
                city=:city,
                zip=:zip
                WHERE oid=:oid''',
                {
                    'first':first_editor_name_entry.get(),
                    'last':last_editor_name_entry.get(),
                    'address':address_editor_entry.get(),
                    'state':state_editor_entry.get(),
                    'city':city_editor_entry.get(),
                    'zip':zip_editor_entry.get(),
                    'oid':record_id
                }
            )

    database.commit()
    database.close()
    #(ccecc)->connect-cursor-execute-commit-close

    editor.destroy()

#Creating a function to update the record
def Update():
    global editor
    editor=Tk()
    editor.title('Update a database')
    #configure(background) is used to set background color
    editor.configure(background='skyblue',borderwidth=5)
    global records
    global record_id
    #Create global variable for entry
    global first_editor_name_entry
    global last_editor_name_entry
    global address_editor_entry
    global state_editor_entry
    global city_editor_entry
    global zip_editor_entry

    #DataBase
    database=connect('address_book.db')
    c=database.cursor()

    record_id=delete_entry.get()
    #Show the dataBase
    # SELECT *(everything),oid(ID) FROM (TableName) is used to select table from *.db file
    c.execute('SELECT * FROM Addresses WHERE oid=' + record_id)
    #fetchall()->fetch all the records,fetchone()->fetch one record,fetchmany(no.)->fetch no. of records
    records=c.fetchall()


    # Creating a Entry
    first_editor_name_entry=Entry(editor,width=30,borderwidth=5,fg='red')
    last_editor_name_entry=Entry(editor,width=30,borderwidth=5,fg='red')
    address_editor_entry=Entry(editor,width=30,borderwidth=5,fg='red')
    city_editor_entry=Entry(editor,width=30,borderwidth=5,fg='red')
    state_editor_entry=Entry(editor,width=30,borderwidth=5,fg='red')
    zip_editor_entry=Entry(editor,width=30,borderwidth=5,fg='red')

    # Displaying an Entry
    first_editor_name_entry.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
    last_editor_name_entry.grid(row=1,column=1,columnspan=3,padx=10,pady=10)
    address_editor_entry.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
    city_editor_entry.grid(row=3,column=1,columnspan=3,padx=10,pady=10)
    state_editor_entry.grid(row=4,column=1,columnspan=3,padx=10,pady=10)
    zip_editor_entry.grid(row=5,column=1,columnspan=3,padx=10,pady=10)

    # creating label
    first_editor_name_label=Label(editor,text='First Name :-',fg='blue',bg='skyblue')
    last_editor_name_label=Label(editor,text='Last Name :-',fg='blue',bg='skyblue')
    address_editor_label=Label(editor,text='Address :-',fg='blue',bg='skyblue')
    city_editor_label=Label(editor,text='City :-',fg='blue',bg='skyblue')
    state_editor_label=Label(editor,text='State :-',fg='blue',bg='skyblue')
    zip_editor_label=Label(editor,text='Zip :-',fg='blue',bg='skyblue')

    # Displaying a label
    first_editor_name_label.grid(row=0,column=0,padx=10,pady=10)
    last_editor_name_label.grid(row=1,column=0,padx=10,pady=10)
    address_editor_label.grid(row=2,column=0,padx=10,pady=10)
    city_editor_label.grid(row=3,column=0,padx=10,pady=10)
    state_editor_label.grid(row=4,column=0,padx=10,pady=10)
    zip_editor_label.grid(row=5,column=0,padx=10,pady=10)

    #Insert the results
    for record in records:
        first_editor_name_entry.insert(0,record[0])
        last_editor_name_entry.insert(0,record[1])
        address_editor_entry.insert(0,record[2])
        state_editor_entry.insert(0,record[3])
        city_editor_entry.insert(0,record[4])
        zip_editor_entry.insert(0,record[5])

    #Save Button
    saveButton=Button(editor,text='Save',borderwidth=5,padx=50,pady=20,bg='green',command=Save)
    saveButton.grid(row=6,column=0,columnspan=3,padx=10,ipadx=80,pady=10)

    # Creater mark
    label_creater=Label(editor,text='Made by Pukhraj',bg='skyblue',fg='green').grid(row=7,column=3)

    

# creating label
first_name_label=Label(win,text='First Name :-',fg='blue',bg='skyblue')
last_name_label=Label(win,text='Last Name :-',fg='blue',bg='skyblue')
address_label=Label(win,text='Address :-',fg='blue',bg='skyblue')
city_label=Label(win,text='City :-',fg='blue',bg='skyblue')
state_label=Label(win,text='State :-',fg='blue',bg='skyblue')
zip_label=Label(win,text='Zip :-',fg='blue',bg='skyblue')

delete_label=Label(win,text='ID Number->',fg='blue',bg='skyblue')

# Displaying a label
first_name_label.grid(row=0,column=0,padx=10,pady=10)
last_name_label.grid(row=1,column=0,padx=10,pady=10)
address_label.grid(row=2,column=0,padx=10,pady=10)
city_label.grid(row=3,column=0,padx=10,pady=10)
state_label.grid(row=4,column=0,padx=10,pady=10)
zip_label.grid(row=5,column=0,padx=10,pady=10)

delete_label.grid(row=7,column=1)

# Creater mark
label_creater=Label(win,text='Made by Pukhraj',bg='skyblue',fg='red').grid(row=9,column=3)

# Creating a Entry
first_name_entry=Entry(win,width=30,borderwidth=5,fg='red')
last_name_entry=Entry(win,width=30,borderwidth=5,fg='red')
address_entry=Entry(win,width=30,borderwidth=5,fg='red')
city_entry=Entry(win,width=30,borderwidth=5,fg='red')
state_entry=Entry(win,width=30,borderwidth=5,fg='red')
zip_entry=Entry(win,width=30,borderwidth=5,fg='red')

delete_entry=Entry(win,width=20,borderwidth=5,fg='red')

# Displaying an Entry
first_name_entry.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
last_name_entry.grid(row=1,column=1,columnspan=3,padx=10,pady=10)
address_entry.grid(row=2,column=1,columnspan=3,padx=10,pady=10)
city_entry.grid(row=3,column=1,columnspan=3,padx=10,pady=10)
state_entry.grid(row=4,column=1,columnspan=3,padx=10,pady=10)
zip_entry.grid(row=5,column=1,columnspan=3,padx=10,pady=10)

delete_entry.grid(row=7,column=2,padx=10,pady=10)

#Submit button
submit=Button(win,text='Submit',borderwidth=5,padx=40,pady=20,bg='green',command=Submit)
submit.grid(row=6,column=3,padx=10,pady=10)

#Show Button
showRecords=Button(win,text='Show',borderwidth=5,padx=50,pady=20,bg='green',command=ShowRecords)
showRecords.grid(row=6,column=2,padx=10,pady=10)

#Exit Button
# ipadx is used to extend the button length
exitButton=Button(win,text='Exit',borderwidth=5,padx=50,pady=20,bg='green',command=win.quit)
exitButton.grid(row=6,column=0,padx=10,pady=10)

#Delete Button
deleteButton=Button(win,text='Delete',borderwidth=5,padx=50,pady=20,bg='green',command=Delete)
deleteButton.grid(row=7,column=0,padx=10,pady=10)

#Update Button
updateButton=Button(win,text='Edit',borderwidth=5,padx=50,pady=20,bg='green',command=Update)
updateButton.grid(row=7,column=3,padx=10,pady=10)

win.mainloop()