from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x800+0+0")

        # ============Variable============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ============Background Image============
        img = Image.open(r"Images\register_bg.png")
        img = img.resize((1530, 800), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=800)

        # ============Labels and Entry============
        # ============Row--1============
        self.fname_entry = ttk.Entry(self.root, textvariable=self.var_fname, font=(
            "Calibri", 15))
        self.fname_entry.place(x=70, y=250, width=250)

        self.lname_entry = ttk.Entry(self.root, textvariable=self.var_lname, font=(
            "Calibri", 15))
        self.lname_entry.place(x=580, y=250, width=250)

        # ============Row--2============
        self.contact_entry = ttk.Entry(self.root, textvariable=self.var_contact, font=(
            "Calibri", 15))
        self.contact_entry.place(x=70, y=335, width=250)

        self.email_entry = ttk.Entry(self.root, textvariable=self.var_email, font=(
            "Calibri", 15))
        self.email_entry.place(x=580, y=335, width=250)

        # ============Row--3============
        self.combo_security_Q = ttk.Combobox(self.root, textvariable=self.var_securityQ, font=(
            "Calibri", 15), state='readonly')
        self.combo_security_Q['values'] = (
            "Select", "Your Birth Place", "Your Best Book", 'Your Pet Name')
        self.combo_security_Q.place(x=70, y=420, width=250)
        self.combo_security_Q.current(0)

        self.txt_security = ttk.Entry(self.root, textvariable=self.var_securityA, font=(
            "Calibri", 15))
        self.txt_security.place(x=580, y=420, width=250)

        # ============Row--4============
        self.txt_pswd = ttk.Entry(self.root, textvariable=self.var_pass, font=(
            "Calibri", 15))
        self.txt_pswd.place(x=70, y=505, width=250)

        self.txt_confirm_pswd = ttk.Entry(self.root, textvariable=self.var_confpass, font=(
            "Calibri", 15))
        self.txt_confirm_pswd.place(x=580, y=505, width=250)

        # ============CheckButton============
        self.var_check = IntVar()
        checkbtn = Checkbutton(self.root, variable=self.var_check, text="I Agree with the terms & Condition", fg='#8d3a64', font=(
            "Calibri", 15, 'bold'), bg="#E0B6CC", onvalue=1, offvalue=0)
        checkbtn.place(x=70, y=570)

        # # ============Button============
        img = Image.open("images/register_btn.png")
        img = img.resize((150, 50), Image.ANTIALIAS)

        self.loginimg = ImageTk.PhotoImage(img)
        b1 = Button(self.root, image=self.loginimg, command=self.register_button,
                    borderwidth=0,cursor="hand2", bg="#f2e2eb")
        b1.place(x=70, y=630, width=150)

        img = Image.open("images/login_btn.png")
        img = img.resize((150, 50), Image.ANTIALIAS)

        self.registerimg = ImageTk.PhotoImage(img)
        b1 = Button(self.root, image=self.registerimg, command=self.login_button,
                    borderwidth=0, cursor="hand2", bg="#f2e2eb")
        b1.place(x=300, y=630, width=150)

    # ============Function Button============
    def register_button(self):
        if self.all_field_required() == False:
            messagebox.showerror(
                "Error", "All fields are Required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error", "Please agree our terms and condition", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
            my_cursor = conn.cursor()
            query = ("select * from user where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showinfo(
                    "Error", "User already exists, please try with another email", parent=self.root)
            else:
                my_cursor.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User added succesfully")
            self.reset_field()

    def login_button(self):
        self.root.destroy()

    def all_field_required(self):
        if self.var_fname.get() == '' or self.var_lname.get() == '' or self.var_contact.get() == '' or self.var_email.get() == '' or self.var_securityQ.get() == 'Select' or self.var_securityA.get() == '' or self.var_pass.get() == '' or self.var_confpass.get() == '':
            return False
        else:
            return True

    def reset_field(self):
        self.var_fname.set('')
        self.var_lname.set('')
        self.var_contact.set('')
        self.var_email.set('')
        self.var_securityQ.set('Select')
        self.var_securityA.set('')
        self.var_pass.set('')
        self.var_confpass.set('')
        self.var_check.set(0)


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("Images/rtu_logo.ico")
    app = Register(root)
    root.mainloop()
