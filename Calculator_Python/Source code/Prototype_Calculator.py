from tkinter import *
win=Tk()
win.title('Calculator')

# Display Screen
e=Entry(width=40,borderwidth=5)
e.grid(row=0,columnspan=3,padx=10,pady=10)


#padx=width/2 of button and pady=width/2 of button

#Assigning function
def Button_Click(number):
    #getting current result on some variable(box)
    current=e.get()
    #deleting the previous result
    e.delete(0,END)
    #displaying the result
    e.insert(0,current+str(number)) #get-delete-insert(gdi)

def Button_Clear():
    e.delete(0,END) 

def Button_add():
    #create a global
    global math
    global first_number
    math="addition"
    #insert in memory(box)
    first_number=int(e.get())
    #delete on screen
    e.delete(0,END) #(gd)

def button_subtract():
    #create a global
    global math
    global first_number
    math = "subtraction"
    #insert in memory(box)
    first_number=int(e.get())
    #delete on screen
    e.delete(0,END) #(gd)

def Button_multiply():
    #create a global
    global math
    global first_number
    math="multiplication"
    #insert in memory(box)
    first_number=int(e.get())
    #delete on screen
    e.delete(0,END) #(gd)

def Button_divide():
    #create a global
    global math
    global first_number
    math="division"
    #insert in memory(box)
    first_number=int(e.get())
    #delete on screen
    e.delete(0,END) #(gd)

def Answer(): #(gdi)
    second_number=int(e.get())
    e.delete(0,END)

    if math=="addition":
        e.insert(0,first_number + second_number)
    
    if math=="subtraction":
        e.insert(0,first_number - second_number)
    
    if math=="multiplication":
        e.insert(0,first_number * second_number)

    if math=="division":
        e.insert(0,first_number / second_number)

    
    

# Create buttons
button_0=Button(win,borderwidth=5,text='0',padx=40,pady=20,bg='red',command=lambda:Button_Click(0))
button_1=Button(win,borderwidth=5,text='1',padx=40,pady=20,bg='red',command=lambda:Button_Click(1))
button_2=Button(win,borderwidth=5,text='2',padx=40,pady=20,bg='red',command=lambda:Button_Click(2))
button_3=Button(win,borderwidth=5,text='3',padx=40,pady=20,bg='red',command=lambda:Button_Click(3))
button_4=Button(win,borderwidth=5,text='4',padx=40,pady=20,bg='red',command=lambda:Button_Click(4))
button_5=Button(win,borderwidth=5,text='5',padx=40,pady=20,bg='red',command=lambda:Button_Click(5))
button_6=Button(win,borderwidth=5,text='6',padx=40,pady=20,bg='red',command=lambda:Button_Click(6))
button_7=Button(win,borderwidth=5,text='7',padx=40,pady=20,bg='red',command=lambda:Button_Click(7))
button_8=Button(win,borderwidth=5,text='8',padx=40,pady=20,bg='red',command=lambda:Button_Click(8))
button_9=Button(win,borderwidth=5,text='9',padx=40,pady=20,bg='red',command=lambda:Button_Click(9))
button_clear=Button(win,borderwidth=5,text='Clear',padx=80,pady=20,bg='orange',command=Button_Clear)
button_Add=Button(win,borderwidth=5,text='+',padx=40,pady=20,bg='blue',fg='white',command=Button_add)
button_Subtract=Button(win,borderwidth=5,text='-',padx=40,pady=20,bg='blue',fg='white',command=button_subtract)
button_Multiply=Button(win,borderwidth=5,text='*',padx=40,pady=20,bg='blue',fg='white',command=Button_multiply)
button_Divide=Button(win,borderwidth=5,text='/',padx=40,pady=20,bg='blue',fg='white',command=Button_divide)
button_Equal=Button(win,borderwidth=5,text='=',padx=90,pady=20,bg='green',command=Answer)

# Display the button
button_1.grid(row=5,column=0)
button_2.grid(row=5,column=1)
button_3.grid(row=5,column=2)

button_4.grid(row=4,column=0)
button_5.grid(row=4,column=1)
button_6.grid(row=4,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=6,column=0)
button_clear.grid(row=6,column=1,columnspan=2)

button_Add.grid(row=1,column=0)
button_Subtract.grid(row=1,column=1)
button_Multiply.grid(row=1,column=2)

button_Divide.grid(row=2,column=0)
button_Equal.grid(row=2,column=1,columnspan=2)

# Creater mark
label_creater=Label(win,text='Made by Pukhraj').grid(row=7,column=2)


win.mainloop()