from tkinter import *
import math
win=Tk()
win.title('Trigonometric Calculator')

# Creating functions
def sin():
    current=e.get()
    e.delete(0,END)
    a=float(current)*3.14/180
    e.insert(0,f'{math.sin(a)} Ans😁')


def cos():
    current=e.get()
    e.delete(0,END)
    a=float(current)*3.14/180
    e.insert(0,f'{math.cos(a)} Ans😁')

def tan():
    current=e.get()
    e.delete(0,END)
    a=float(current)*3.14/180
    e.insert(0,f'{math.tan(a)} Ans😁')

def cot():
    current=e.get()
    e.delete(0,END)
    a=float(current)*3.14/180
    e.insert(0,f'{math.cot(a)} Ans😁')

def sec():
    current=e.get()
    e.delete(0,END)
    a=float(current)*3.14/180
    e.insert(0,f'{math.sec(a)} Ans😁')

def cosec():
    current=e.get()
    e.delete(0,END)
    a=float(current)*3.14/180
    e.insert(0,f'{math.cosec(a)} Ans😁')

# Creating ENTRY
e=Entry(win,width=40,borderwidth=5,fg='green')
e.insert(0,"Type Angle in degree")
e.grid(row=0,column=0,columnspan=2,padx=10,pady=10)


# Creating Button
button_sin=Button(win,text='Sin',bg='blue',padx=40,pady=20,borderwidth=5,command=sin)
button_cos=Button(win,text='Cos',bg='blue',padx=40,pady=20,borderwidth=5,command=cos)
button_tan=Button(win,text='Tan',bg='blue',padx=40,pady=20,borderwidth=5,command=tan)
button_cot=Button(win,text='Cot',bg='blue',padx=40,pady=20,borderwidth=5,command=cot)
button_sec=Button(win,text='Sec',bg='blue',padx=40,pady=20,borderwidth=5,command=sec)
button_cosec=Button(win,text='Cosec',bg='blue',padx=33,pady=20,borderwidth=5,command=cosec)

button_sin.grid(row=1,column=0)
button_cos.grid(row=1,column=1,padx=10)
button_tan.grid(row=2,column=0,padx=10)
button_cot.grid(row=2,column=1,pady=20,padx=10)
button_sec.grid(row=3,column=0,pady=5)
button_cosec.grid(row=3,column=1,pady=5,padx=10)

label=Label(win,text='Made by Pukhraj',fg='blue').grid(row=4,column=1)

win.mainloop()