from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System
from register import Register


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x800+0+0")

        # Variable
        self.txtuser = StringVar()
        self.txtpass = StringVar()

        # ==========Background Image==========
        img = Image.open(r"Images\login_bg.png")
        img = img.resize((1530, 800), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=800)

        # ==========Username Field==========
        user_btn = ttk.Entry(
            self.root, textvariable=self.txtuser, font=("times new roman", 20))
        user_btn.place(x=1020, y=370, width=400)

        # ==========Password Field==========
        self.txtpassword = ttk.Entry(
            self.root, textvariable=self.txtpass, font=("times new roman", 20))
        self.txtpassword.place(x=1020, y=495, width=400)

        # ==========Login button==========
        img = Image.open("images/login_btn.png")
        img = img.resize((150, 50), Image.ANTIALIAS)

        self.login_img = ImageTk.PhotoImage(img)
        b1 = Button(self.root, image=self.login_img, command=self.login,
                    borderwidth=0, cursor="hand2", bg="#bbeaf6", activebackground='#bbeaf6')
        b1.place(x=1145, y=560, width=150)

        # ==========Register button==========
        registerbtn = Button(self.root, command=self.register_window, text="New User?", font=(
            "Arial", 15, "bold"), bd=3, fg="#d22b32", cursor="hand2", borderwidth=0, relief=RIDGE, bg="#bbeaf6", activeforeground="#d22b32", activebackground="#bbeaf6")
        registerbtn.place(x=1000, y=630, width=128, height=35)

        # ==========Forgot button==========
        forgotbtn = Button(self.root, command=self.forget_password, text="Forgot Password?", font=(
            "Arial", 15, "bold"), bd=3, fg="#360981", cursor="hand2", borderwidth=0, relief=RIDGE, bg="#bbeaf6", activeforeground="#360981", activebackground="#bbeaf6")
        forgotbtn.place(x=1000, y=670, width=200, height=35)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.new_window.iconbitmap("Images/rtu_logo.ico")
        self.app = Register(self.new_window)


    def login(self):
        if self.txtuser.get() == "" or self.txtpassword.get() == "":
            messagebox.showerror(
                "Error", "All Fields Required!!!", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from user where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()
            # print(self.txtuser.get(), self.txtpass.get())
            # print(row)
            if row == None:
                messagebox.showerror(
                    "Error", "Invalid username or password", parent=self.root)
            else:
                self.new_window = Toplevel()
                self.new_window.iconbitmap("Images/rtu_logo.ico")
                self.app = Face_Recognition_System(self.new_window)

            conn.commit()
            conn.close()

    # ============Reset Password============
    def reset_password(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror(
                "Error", "Select Security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the answer", parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror(
                "Error", "Please Enter the new password.", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
            my_cursor = conn.cursor()
            query = (
                "select * from user where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(),
                     self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Please Enter the correct answer.", parent=self.root2)
            else:
                query = ("update user set password=%s where email=%s")
                value = (self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Success", "Your Password has been reset successfully. Please login with new password.", parent=self.root2)
                self.root2.destroy()

    # ============Forget password window============
    def forget_password(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please Enter email address to reset password", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
            my_cursor = conn.cursor()
            query = ("select * from user where email=%s")
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror(
                    "Error", "Please enter the valid email.", parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel(self.root)
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                # Make the window resizable false
                self.root2.resizable(False, False)

                l = Label(self.root2, text="Forget Password", font=(
                    "times new roman", 15, "bold"), fg="red", bg="#f0f0f0")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Question", font=(
                    "times new roman", 15, "bold"), bg="#f0f0f0")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=(
                    "times new roman", 15), state='readonly')
                self.combo_security_Q['values'] = (
                    "Select", "Your Birth Place", "Your Best Book", 'Your Pet Name')
                self.combo_security_Q.place(x=50, y=115, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=(
                    "times new roman", 15, "bold"), bg="#f0f0f0")
                security_A.place(x=50, y=160)

                self.txt_security = ttk.Entry(self.root2, font=(
                    "times new roman", 15))
                self.txt_security.place(x=50, y=195, width=250)

                new_pass = Label(self.root2, text="New Password", font=(
                    "times new roman", 15, "bold"), bg="#f0f0f0")
                new_pass.place(x=50, y=240)

                self.txt_newpass = ttk.Entry(self.root2, font=(
                    "times new roman", 15))
                self.txt_newpass.place(x=50, y=275, width=250)

                btn = Button(self.root2, command=self.reset_password, text="Reset", font=(
                    "times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=135, y=330)


if __name__ == "__main__":
    win = Tk()
    win.iconbitmap("Images/rtu_logo.ico")
    app = Login(win)
    win.mainloop()
