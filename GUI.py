from tkinter import *
import tkinter.font
import os
import sys

def new():
    n=Toplevel()
    n.title("THE TAMMED")
    img=PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\tammed.png")
    background_image = PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\bg-removebg-preview.png")
    n.iconphoto(False,img)
    text_1="The Tammed is a tool which is made by two students from NED University:Muhammad Masood ur Rehman and Umair Shakeel.This\n application made from Python and Opencv can detect people,count them in the case of a crowd, & can even recognise a particular person.\n The Tammed is made for situations like:security & to assist visually impared people. It can perhaps replace the CCTV cameras."
    text_2="There are three features in The Tammed: face detection, real-time population counter, and cam face recognition.All three of them helps to\n highlight the faces of humans. However, real-time and cam face counts the number of people it sees.Also, the real-time feature identifies the\n whole body of a person. This application can be extremely useful in banks and in important industries which requires security,as you can not\n only recognise but also count the number of culprits in case of a crime"
    fontStyle = tkinter.font.Font(family="Times New Roman (Times)", size=25, weight="bold", slant="italic")
    fontStyle_1 = tkinter.font.Font(family="Aerial", size=15, slant="italic")
    d=Label(n, text="ABOUT & HELP",anchor=NW, font=fontStyle,bg="dodgerblue", fg="white")
    d.pack(fill=X, expand=True, ipady=10, anchor=NW)
    e=Label(n, text=text_1, anchor=NW,font=fontStyle_1, bg="midnightblue", fg="SpringGreen2")
    e.place(relx=0.0,rely=0.1, anchor=NW)
    f = Label(n, text=text_2, anchor=NW, font=fontStyle_1, bg="midnightblue", fg="SpringGreen2")
    f.place(relx=0.0, rely=0.3, anchor=NW)
    background_label=Label(n,image=background_image, bg="midnightblue")
    background_label.place(relx=1.0,rely=0.5,anchor=NE)
    n.configure(bg="midnightblue")
    n.mainloop()

def new_1():
    os.system('python FaceRecognition.py')

def new_2():
    os.system('python CamFaceRecognition.py')

def new_3():
    os.system('python RealTimeObjectDetection.py')

m=Tk()
image= PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\logo_circle(bgless).png")
m.title("THE TAMMED")
fontStyle=tkinter.font.Font(family="Times New Roman (Times)", size=25, weight="bold", slant="italic")
fontStyle_1=tkinter.font.Font(family="Calibiri", size=25, weight="bold")
a=Label(m, text = "Instrument Designed to Catch U-Bolts!!",font=fontStyle, fg="goldenrod2", bg="seashell4",anchor=W)
b=Menubutton(m, text=".:",font=fontStyle_1,  fg="yellow2", bg="seashell4")
c=Label(m,image=image, height=500, width=700, bg="khaki1")
a.pack(fill=X, expand=True, ipady=10,anchor=NW)
b.place(in_=a,relx=1, x=-2, y=2, anchor=NE)
c.place(relx=0.5, rely=0.5, anchor=CENTER)
options= Menu(b)
b.config(menu=options)
options.add_command(label='ABOUT & HELP',command=new)
options.add_command(label='FACE RECOGNITION', command=new_1)
options.add_command(label='REAL-TIME FACE RECOGNITION', command=new_2)
options.add_command(label='REAL-TIME POPULATION COUNTER', command=new_3)

m.configure(bg="khaki1")
m.mainloop()