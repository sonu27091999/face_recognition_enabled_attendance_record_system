from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import os


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500+465+200")
        self.root.title("Face Scan")
        # Make the window resizable false
        self.root.resizable(False, False)

        # ==========Background Image==========
        bg_img = Image.open(
            r"Images\face_scan.png")
        bg_img = bg_img.resize((500, 500), Image.ANTIALIAS)
        self.bg_img_label = ImageTk.PhotoImage(bg_img)

        bg_img = Label(self.root, image=self.bg_img_label)
        bg_img.place(x=0, y=0, width=500, height=500)

        '''
        img = Image.open("images/login_btn.png")
        img = img.resize((150, 50), Image.ANTIALIAS)

        self.login_img = ImageTk.PhotoImage(img)
        b1 = Button(self.root, image=self.login_img,
                    borderwidth=0, cursor="hand2", bg="#bbeaf6", activebackground='#bbeaf6')
        b1.place(x=1145, y=560, width=150)'''

        img = Image.open("images/face_scan_btn.png")
        img = img.resize((170, 40), Image.ANTIALIAS)
        self.face_scan_btn = ImageTk.PhotoImage(img)
        button = Button(self.root, command=self.face_recog, image=self.face_scan_btn,
                        borderwidth=0, cursor="hand2", bg="white", activebackground='white')
        button.place(x=165, y=375)

    # ==========Face Recognition==========
    def mark_attendance(self, i, r, n, d):
        now = datetime.now()

        if not os.path.isfile(os.getcwd() + f'/attendance/{now.strftime("%d-%m-%Y")}.csv'):
            with open(os.getcwd()+f'/attendance/{now.strftime("%d-%m-%Y")}.csv', 'w') as creating_new_csv_file:
                pass

        with open(os.getcwd()+ f'/attendance/{now.strftime("%d-%m-%Y")}.csv', "r+", newline="\n") as f:
            myDataList = f.readlines()
            # print(myDataList)
            name_list = []
            for line in myDataList:
                entry = line.split(',')
                name_list.append(entry[0])

            # print("$$$$$$$$$$$$$$$$$$$$$", name_list)

            # if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
            if (i not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")

    # ==========Face Recognition==========
    def face_recog(self):
        def draw_boundray(img, classifier, scale_factor, minNeighbors, color, text, clf):
            # print("draw_boundray$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scale_factor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Student_id, Dep, Name, Roll_no from student where Student_id="+str(id))
                data = my_cursor.fetchone()
                # print(data)

                if confidence > 77:
                    cv2.putText(
                        img, f"Id:{data[0]}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(
                        img, f"Roll:{data[3]}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(
                        img, f"Name:{data[2]}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(
                        img, f"Department:{data[1]}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    self.mark_attendance(data[0], data[3], data[2], data[1])
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            # print("Recognize Function$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            coord = draw_boundray(img, faceCascade, 1.1,
                                  10, (255, 25, 255), 'Face', clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            print("Error: Could not open Camera.")
            exit()

        while True:
            ret, img = video_cap.read()
            if ret == True:
                cv2.namedWindow("Welcome to face Recognition",
                                cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Welcome to face Recognition",
                                      cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to face Recognition", img)

                if cv2.waitKey(1) == 13:
                    break
            else:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("Images/rtu_logo.ico")
    obj = Face_Recognition(root)
    root.mainloop()


# import cv2
# face_cascascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # load the file
# # img = cv2.imread('sonu.jpg')        # read the static image

# video_cap = cv2.VideoCapture(0)        # read through camera
# ret, img = video_cap.read()

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # convert rgb -> gray
# faces = face_cascascade.detectMultiScale(gray, 1.3, 5)  # detect all faces in images
# for (x, y, w, h) in faces:  # draw rectangle for each face
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     cv2.imshow('img', img)
#     if cv2.waitKey(0) == 13:
#         break
# cv2.destroyAllWindows()
