import mysql.connector
from tkinter import *
from tkinter import messagebox
# from Modules import CreateTable 
# Windows=Serves as a container to hold or contain widgets
#Widgets=GUI ELEMENTS:buttons,textboxes,labels,images
count=0
def submitentry():
    Entry_1=entry.get()
    # try:
    #     CreateTable(Entry_1)
    #     print(Entry_1+" table has been created")
    #     messagebox.showinfo("Sucess",f"table {Entry_1} has been created")
    # except Exception as e:
    #     print("Error:",e)
    #     messagebox.showerror(f"Error Failed to create table {e}")
def clickresponse():
    global count
    count+=1
    print("YOU clicked the button",count,"times")

#Creating a window
window = Tk()#instanciate an instance of window
def MainWindow():       #main window 
    window.geometry("1280x720")          
    window.title("To do")
    icon = PhotoImage(file='smileythumb.png')
    window.iconphoto(True,icon)
    window.config(background="#292726")
    window.resizable(False,False)
#THIS IS HOW YOU ADD LABELING
def Labeler(picture=None):
    label = Label(window,
              font=('Arial',40,'italic','bold'),fg="#000000",bg="#DF5D1C",relief='flat',bd=9,
              padx=5,pady=5,image=picture if picture is not None else None,
              compound='left')
    label.place(x=640,y=310)
    label.pack()
#THIS IS HOW TO ADD BUTTONS

buttphoto=PhotoImage(file='temp.png')
def button(txt,Command,img=None,fnt='Sans'):
    button = Button(window,text=txt,
                command=Command,
                font=fnt,
                fg="#FF0000",
                bg="#FFEA00",
                activeforeground="#FF0000",
                activebackground="#FFEA00",
                state="active",
                image=img if img is not None else None,
                compound="left" if img is not None else None)   
                # button.place(x=310,y=210)    
    button.pack()
    return button
#entry widget
def ent():

    global entry
    entry = Entry(window,
                font=("Arial",30),
                fg="red",
                bg="blue")
    entry.pack(side='bottom')
check_button_val=IntVar()
def check_button_reaction():
    if check_button_val.get()==1:
        print("you agree")
    else:
        print("you disagree")
def checkbutton(input_text=None):

    check_button=Checkbutton(window,
                             text=str(input_text) if input_text is not None else None,
                             variable=check_button_val,
                             onvalue=1,
                             offvalue=0,
                             command=check_button_reaction,
                             font=("Arial",20,'bold','underline'))
    check_button.pack()
MainWindow()
Labeler()
#button("CLICK ME",clickresponse,buttphoto)
# ent()
# submit_button=button("SUBMIT",submitentry)
# submit_button.pack(side='top')
# checkbutton("ENTER")
window.mainloop()#listen for events and place a window on screen


