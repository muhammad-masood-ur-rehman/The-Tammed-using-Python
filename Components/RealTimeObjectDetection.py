import cv2
import imutils
import numpy as np
import argparse
from tkinter import *
import tkinter.font
import PIL.Image, PIL.ImageTk


def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    #cv2.imshow('output', frame)
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    height, width, no_channels = frame.shape

    # Create a canvas that can fit the above image
    canvas = tkinter.Canvas(root, width=width, height=height)
    canvas.pack()

    # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
    photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(im))

    # Add a PhotoImage to the Canvas
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
    root.mainloop()
    return frame


def detectByPathVideo(path, writer):
    video = cv2.VideoCapture(path)
    check, frame = video.read()

    if check == False:
        print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
        return

    print('Detecting people...')
    while video.isOpened():
        # check is True if reading was successful
        check, frame = video.read()

        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            frame = detect(frame)

            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        else:
            break

    video.release()
    cv2.destroyAllWindows()


def detectByCamera(writer):
    video = cv2.VideoCapture(0)
    print('Detecting people...')

    while True:
        check, frame = video.read()

        frame = detect(frame)
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


def detectByPathImage(path, output_path):
    image = cv2.imread(path)

    image = imutils.resize(image, width=min(800, image.shape[1]))

    result_image = detect(image)

    if output_path is not None:
        cv2.imwrite(root, result_image)





def humanDetector(args):
    image_path = args["image"]
    video_path = args['video']
    camera_path = args['camera']
    if str(args["camera"]) == 'true':
        camera = True
    else:
        camera = False

    writer = None
    #if args['output'] is not None and image_path is None:
    #    writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))

    if camera:
        print('[INFO] Opening Web Cam.')
        detectByCamera(writer)
    elif video_path is not None:
        print('[INFO] Opening Video from path.')
        detectByPathVideo(video_path, writer)
    elif image_path is not None:
        print('[INFO] Opening Image from path.')
        detectByPathImage(image_path, args['output'])




v=1

def choice(value):
    global v
    v=value
    if v==2:

        def argsParser():
            arg_parse = argparse.ArgumentParser()
            arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
            arg_parse.add_argument("-v", "--video", default=r"C:\Users\Masood Rehman\Pictures\Videos_2.mp4", help="path to Video File ")
            arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
            arg_parse.add_argument("-o", "--output", default=str, help="path to optional output video file")
            args = vars(arg_parse.parse_args())

            return args

        if __name__ == "__main__":
            HOGCV = cv2.HOGDescriptor()
            HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            args = argsParser()
            humanDetector(args)

    if v== 3:
        def argsParser():
            arg_parse = argparse.ArgumentParser()
            arg_parse.add_argument("-i", "--image", default=r"C:\Users\Masood Rehman\Pictures\people.jpg", help="path to Image File ")
            arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
            arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
            arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
            args = vars(arg_parse.parse_args())

            return args

        if __name__ == "__main__":
            HOGCV = cv2.HOGDescriptor()
            HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            args = argsParser()
            humanDetector(args)

    if v == 4:

        def argsParser():
            arg_parse = argparse.ArgumentParser()
            arg_parse.add_argument("-i", "--image", default=None, help="path to Image File ")
            arg_parse.add_argument("-v", "--video", default=None, help="path to Video File ")
            arg_parse.add_argument("-c", "--camera", default="true", help="Set true if you want to use the camera.")
            arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
            args = vars(arg_parse.parse_args())

            return args

        if __name__ == "__main__":
            HOGCV = cv2.HOGDescriptor()
            HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
            args = argsParser()
            humanDetector(args)



if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    root = Tk()
    root.title("THE TAMMED")
    img = PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\tammed.png")
    icon = PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\icon_image.png", height=40)
    icon_1 = PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\icon_video (1).png", height=40)
    icon_2 = PhotoImage(file=r"C:\Users\Masood Rehman\Downloads\icon_camera.png", height=40)
    root.iconphoto(False, img)
    fontStyle = tkinter.font.Font(family="Times New Roman (Times)", size=25, weight="bold", slant="italic")
    e = Label(root, text="REAL-TIME POPULATION COUNTER", anchor=NW, font=fontStyle, bg="dodgerblue", fg="white")
    e.pack(fill=X, expand=True, ipady=10, anchor=NW)
    f = Button(root, image=icon, command=lambda *args: choice(3))
    f.place(in_=e, relx=1, x=-158, y=2, anchor=NE)
    h = Button(root, image=icon_1, command=lambda *args: choice(2))
    h.place(in_=e, relx=1, x=-80, y=2, anchor=NE)
    i = Button(root, image=icon_2, command=lambda *args: choice(4))
    i.place(in_=e, relx=1, x=-2, y=2, anchor=NE)



root.mainloop()