import cv2
from tkinter import *
import tkinter.font
import PIL.Image, PIL.ImageTk


o = Tk()
o.title("THE TAMMED")
img = PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\tammed.png")
o.iconphoto(False, img)
fontStyle = tkinter.font.Font(family="Times New Roman (Times)", size=25, weight="bold", slant="italic")
e = Label(o, text="FACE RECOGNITION", anchor=NW, font=fontStyle, bg="dodgerblue", fg="white")
e.pack(fill=X, expand=True, ipady=10, anchor=NW)

faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img= cv2.imread(r"C:\Users\Masood Rehman\Pictures\four faces.jpg")
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=10)

font= cv2.FONT_HERSHEY_SIMPLEX
LeftCornerOfText = (0,20)
fontScale= 0.5
fontColor= (0,0,0)
lineType= 2
cv2.putText(img,'Number of Faces found :'+str(len(faces)), LeftCornerOfText, font, fontScale,fontColor, lineType)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height, width, no_channels = img.shape

# Create a canvas that can fit the above image
canvas = tkinter.Canvas(o, width = width, height = height)
canvas.pack()

#Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(im))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
# Run the window loop
o.mainloop()