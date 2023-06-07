from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

'''
#Add a canvas widget
canvas = Canvas(win, width= 350)

#Add a Label widget in the Canvas
label = Label(canvas, text= "Click the Button to Exit", font= ('Helvetica 17 bold'))
label.pack(pady= 30)

#Create a button in canvas widget
ttk.Button(canvas, text= "Exit", command= exit_program).pack()
canvas.pack()
'''


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x400+200+200")
        self.root.title("Train Data")
        # Make the window resizable false
        self.root.resizable(False, False)

        # ==========Background Image==========
        bg_img = Image.open(
            r"Images\train_data.jpeg")
        bg_img = bg_img.resize((800, 400), Image.ANTIALIAS)
        self.bg_img_label = ImageTk.PhotoImage(bg_img)

        bg_img = Label(self.root, image=self.bg_img_label)
        bg_img.place(x=0, y=0, width=800, height=400)

        save_btn = Button(self.root, command=self.train_classifier, text="Train Data", width=13, font=(
            'times new roman', 13, 'bold'), bg="blue", fg='white')
        save_btn.place(x=600,y=300)
       

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        print(path)

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')     # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # ==================Train the classifier and save==================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Training Dataset Completed.", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("Images/rtu_logo.ico")
    obj = Train(root)
    root.mainloop()
