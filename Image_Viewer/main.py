from tkinter import *
from PIL import ImageTk,Image

win=Tk()
win.title('Image Viewer')
win.iconbitmap('Image_Viewer/icon.ico')

img_1=Image.open('Image_Viewer/1.png').resize((250,250))
img_2=Image.open('Image_Viewer/2.png').resize((250,250))
img_3=Image.open('Image_Viewer/3.jpg').resize((250,250))
img_4=Image.open('Image_Viewer/4.png').resize((250,250))
img_5=Image.open('Image_Viewer/5.png').resize((250,250))
img_6=Image.open('Image_Viewer/6.png').resize((250,250))

image_1=ImageTk.PhotoImage(img_1)
image_2=ImageTk.PhotoImage(img_2)
image_3=ImageTk.PhotoImage(img_3)
image_4=ImageTk.PhotoImage(img_4)
image_5=ImageTk.PhotoImage(img_5)
image_6=ImageTk.PhotoImage(img_6)

image_list=[image_1,image_2,image_3,image_4,image_5,image_6]



#function of buttons
def forward(position):
    # u need to define label as global to use in function
    #//ly for other variables
    global label
    global button_forward
    #use to format grid
    label.grid_forget()
    label=Label(win,image=image_list[position])
    label.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    button_forward=Button(win,text='->',bg='green',borderwidth=5,padx=10,pady=10,command=lambda:forward(position+1))
    button_forward.grid(row=1,column=2)
    #here button_backward tells button_forward it's position
    button_backward=Button(win,text='<-',bg='green',borderwidth=5,padx=10,pady=10,command=lambda:backward(position-1))
    button_backward.grid(row=1,column=0)
    label=Label(win,text='Made by Pukhraj',fg='blue')
    label.grid(row=2,column=2)
    if position==5:
        button_forward=Button(win,text='->',bg='green',borderwidth=5,padx=10,pady=10,state=DISABLED)
        button_forward.grid(row=1,column=2)
    status=Label(win,text=f'Image {str(position+1)} of {str(len(image_list))}',bd=1,relief=SUNKEN,anchor=E,pady=2)
    status.grid(row=3,columnspan=3,sticky=W+E)
    
    

def backward(position):
    # u need to define label as global to use in function
    #//ly for other variables
    global label
    global button_backward
    #use to format grid
    label.grid_forget()
    label=Label(win,image=image_list[position])
    label.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    #here button_forward tells button_backward it's position
    button_forward=Button(win,text='->',bg='green',borderwidth=5,padx=10,pady=10,command=lambda:forward(position+1))
    button_forward.grid(row=1,column=2)
    button_backward=Button(win,text='<-',bg='green',borderwidth=5,padx=10,pady=10,command=lambda:backward(position-1))
    button_backward.grid(row=1,column=0)
    label=Label(win,text='Made by Pukhraj',fg='blue')
    label.grid(row=2,column=2)
    if position==0:
        button_backward=Button(win,text='<-',bg='green',borderwidth=5,padx=10,pady=10,state=DISABLED)
        button_backward.grid(row=1,column=0)
    status=Label(win,text=f'Image {str(position+1)} of {str(len(image_list))}',bd=1,relief=SUNKEN,anchor=E,pady=2)
    status.grid(row=3,columnspan=3,sticky=W+E)

#Note:-Here button(_forward and _backward) acts first time and
#then button(_forward and _backward) of functions comes in play
#because function activates.


button_exit=Button(win,text='Exit',bg='green',borderwidth=5,pady=10,padx=10,command=win.quit)
button_forward=Button(win,text='->',bg='green',borderwidth=5,padx=10,pady=10,command=lambda:forward(1))
button_backward=Button(win,text='<-',bg='green',borderwidth=5,padx=10,pady=10,command=lambda :backward(1))

button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
button_backward.grid(row=1,column=0)

label=Label(win,image=image_1)
label.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

label=Label(win,text='Made by Pukhraj',fg='blue')
label.grid(row=2,column=1)

#bd=borderdepth,anchor=positin in W or E,relief=state(SUNKEN),sticky=extend line(W+E)
status=Label(win,text=f'Image 1 of {str(len(image_list))}',bd=1,relief=SUNKEN,anchor=E,pady=2)
status.grid(row=3,columnspan=3,sticky=W+E)


win.mainloop()