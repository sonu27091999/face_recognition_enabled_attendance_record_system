from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from tkinter import messagebox
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ==========Background Image==========
        bg_img = Image.open(
            r"Images\main_bg.png")
        bg_img = bg_img.resize((1600, 800), Image.ANTIALIAS)
        self.bg_img_label = ImageTk.PhotoImage(bg_img)

        bg_img = Label(self.root, image=self.bg_img_label)
        bg_img.place(x=0, y=0, width=1600, height=800)

        # ==========RTU Banner==========
        # rtu_logo = Image.open(r"Images\rtu.png")
        # rtu_logo = rtu_logo.resize((900, 150), Image.ANTIALIAS)
        # self.rtu_logo_label = ImageTk.PhotoImage(rtu_logo)
        # rtu_logo = Label(image=self.rtu_logo_label, bg="black", borderwidth=0)
        # rtu_logo.place(x=300, y=5, width=900, height=150)

        # ==========Dashboard Image==========
        # dashboard_logo = Image.open(r"Images\dashboard.png")
        # dashboard_logo = dashboard_logo.resize((400, 360), Image.ANTIALIAS)
        # self.dashboard_logo_label = ImageTk.PhotoImage(dashboard_logo)
        # dashboard_logo = Label(
        #     image=self.dashboard_logo_label, bg="black", borderwidth=0)
        # dashboard_logo.place(x=1100, y=300, width=400, height=360)

        # ==========Student Button==========
        student_detail = Image.open(
            r"Images\student_detail.png")
        student_detail = student_detail.resize((220, 220), Image.ANTIALIAS)
        self.student_detail_img = ImageTk.PhotoImage(student_detail)
        student_detail = Button(bg_img, image=self.student_detail_img,
                                command=self.student_details, bd=0, activebackground="#3c3d3c", cursor="hand2")
        student_detail.place(x=100, y=250, width=220, height=220)

        # ==========Detect Face Button==========
        face_recognition = Image.open(
            r"Images\face_recognition.png")
        face_recognition = face_recognition.resize((230, 230), Image.ANTIALIAS)
        self.face_recognition_img = ImageTk.PhotoImage(face_recognition)

        face_recognition = Button(bg_img, image=self.face_recognition_img,
                                  command=self.face_data, bd=0, activebackground="#3c3d3c", cursor="hand2")
        face_recognition.place(x=400, y=245, width=230, height=230)

        # ==========Attendance Button==========
        attendance = Image.open(
            r"Images\attendance.png")
        attendance = attendance.resize((230, 230), Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(attendance)

        attendance = Button(bg_img, image=self.attendance_img,
                            command=self.attendance_data, bd=0, activebackground="#3c3d3c", cursor="hand2")
        attendance.place(x=700, y=245, width=230, height=230)

        # ==========Train Face Button==========
        train_face = Image.open(
            r"Images\train_data.png")
        train_face = train_face.resize((220, 220), Image.ANTIALIAS)
        self.train_data_img = ImageTk.PhotoImage(train_face)

        train_face = Button(bg_img, image=self.train_data_img,
                            command=self.train_data, bd=0,
                            activebackground="#3c3d3c", cursor="hand2")
        train_face.place(x=250, y=500, width=220, height=220)

        # ==========Photos Button==========
        photos = Image.open(
            r"Images\photos.png")
        photos = photos.resize((220, 220), Image.ANTIALIAS)
        self.photos_img = ImageTk.PhotoImage(photos)

        photos = Button(bg_img, image=self.photos_img,
                        cursor="hand2", command=self.open_img, bd=0,
                        activebackground="#3c3d3c")
        photos.place(x=550, y=500, width=220, height=220)

    # =========Functional Button=============

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.new_window.iconbitmap("Images/rtu_logo.ico")
        self.app = Student(self.new_window)

    def train_data(self):
        # self.new_window = Toplevel(self.root)
        # self.app = Train(self.new_window)
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

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

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window.iconbitmap("Images/rtu_logo.ico")
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window.iconbitmap("Images/rtu_logo.ico")
        self.app = Attendance(self.new_window)

    def open_img(self):
        os.startfile("data")

if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("Images/rtu_logo.ico")
    obj = Face_Recognition_System(root)
    root.mainloop()
