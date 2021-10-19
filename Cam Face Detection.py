import cv2
import sys
from tkinter import *
import tkinter.font
import PIL.Image, PIL.ImageTk

p = Tk()
p.title("THE TAMMED")
img = PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\tammed.png")
p.iconphoto(False, img)
fontStyle = tkinter.font.Font(family="Times New Roman (Times)", size=25, weight="bold", slant="italic")
f = Label(p, text="REAL-TIME FACE RECOGNITION", anchor=NW, font=fontStyle, bg="dodgerblue", fg="white")
f.pack(fill=X, expand=True, ipady=10, anchor=NW)


cascPath = sys.argv[0]
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
       # flags=cv2.cv2.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Printing text on image
    font = cv2.FONT_HERSHEY_SIMPLEX
    LeftCornerOfText = (2, 40)
    fontScale = 1
    fontColor = (255, 0, 255)
    lineType = 2
    cv2.putText(frame, 'Number of Faces found :' + str(len(faces)), LeftCornerOfText, font, fontScale, fontColor,lineType)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
height, width, no_channels = frame.shape

# Create a canvas that can fit the above image
canvas = tkinter.Canvas(p, width = width, height = height)
canvas.pack()

#Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(im))

# Add a PhotoImage to the Canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
p.mainloop()