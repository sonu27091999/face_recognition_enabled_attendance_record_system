from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        # ==================Variables==================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_batch = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

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

        # ==========Main Frame==========
        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=20, y=180, width=1480, height=600)

        # ==========Left Frame==========
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Student Details", font=(
            'times new roman', 12, 'bold'))
        left_frame.place(x=10, y=10, width=720, height=580)

        img_left = Image.open(
            r"Images\student_info.jpg")
        img_left = img_left.resize((710, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        img_left = Label(left_frame, image=self.photoimg_left)
        img_left.place(x=5, y=0, width=710, height=130)

        # ==========Current Course Frame==========
        current_course_frame = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Current Course", font=(
            'times new roman', 13, 'bold'))
        current_course_frame.place(x=5, y=135, width=710, height=125)

        # ==========Department==========
        dep_label = Label(current_course_frame, text="Departement", font=(
            'times new roman', 13, 'bold'), bg='white')
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            'times new roman', 13), state='readonly', width=20)
        dep_combo['values'] = ('Select Department',
                               'Computer Science', 'Information Technology', 'Civil', 'Mechanical', 'Electrical', 'Petroleum')
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # ==========Course==========
        course_label = Label(current_course_frame, text="Course", font=(
            'times new roman', 13, 'bold'), bg='white')
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            'times new roman', 13), state='readonly', width=20)
        course_combo['values'] = ('Select Course', 'B.Tech', 'M.Tech')
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # ==========Year==========
        year_label = Label(current_course_frame, text="Year", font=(
            'times new roman', 13, 'bold'), bg='white')
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            'times new roman', 13), state='readonly', width=20)
        year_combo['values'] = ('Select Year', '2019-20',
                                '2020-21', '2021-22', '2022-23')
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # ==========Semester==========
        semester_label = Label(current_course_frame, text="Semester", font=(
            'times new roman', 13, 'bold'), bg='white')
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            'times new roman', 13), state='readonly', width=20)
        semester_combo['values'] = (
            'Select Semester', 'Even', 'Odd')
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # ==========Class Student Information==========
        class_student_frame = LabelFrame(left_frame, bd=2, bg='white', relief=RIDGE, text="Class Student Information", font=(
            'times new roman', 13, 'bold'))
        class_student_frame.place(x=5, y=260, width=710, height=300)

        # ==========Student id==========
        student_id_label = Label(class_student_frame, text="StudentID:", font=(
            'times new roman', 13, 'bold'), bg='white')
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        student_id_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_id, width=20, font=('times new roman', 13))
        student_id_entry.insert(0, "Ex: 19XXX")
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # ==========Student Name==========
        student_name_label = Label(class_student_frame, text="Student Name:", font=(
            'times new roman', 13, 'bold'), bg='white')
        student_name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        student_name_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_name, width=20, font=('times new roman', 13))
        student_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # ==========Batch==========
        batch_label = Label(class_student_frame, text="Batch:", font=(
            'times new roman', 13, 'bold'), bg='white')
        batch_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        batch_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_batch, width=20, font=('times new roman', 13))
        batch_entry.insert(0, "Ex: 8CSE4")
        batch_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # ==========Roll No==========
        univ_roll_no_label = Label(class_student_frame, text="URN:", font=(
            'times new roman', 13, 'bold'), bg='white')
        univ_roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        univ_roll_no_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_roll, width=20, font=('times new roman', 13))
        univ_roll_no_entry.insert(0, "Ex: 19EUCCSXXX")
        univ_roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # ==========Gender==========
        gender_label = Label(class_student_frame, text="Gender:", font=(
            'times new roman', 13, 'bold'), bg='white')
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            'times new roman', 13), state='readonly', width=18)
        gender_combo['values'] = ('Select Gender', 'Male', 'Female', 'Other')
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # ==========Date of Birth==========
        dob_label = Label(class_student_frame, text="DOB:", font=(
            'times new roman', 13, 'bold'), bg='white')
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,
                              font=('times new roman', 13))
        dob_entry.insert(0, "dd/mm/yy")
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # ==========Email==========
        email_label = Label(class_student_frame, text="Email:", font=(
            'times new roman', 13, 'bold'), bg='white')
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            'times new roman', 13))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ==========Phone No.==========
        phone_label = Label(class_student_frame, text="Phone No:", font=(
            'times new roman', 13, 'bold'), bg='white')
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            'times new roman', 13))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # ==========Address.==========
        address_label = Label(class_student_frame, text="Address:", font=(
            'times new roman', 13, 'bold'), bg='white')
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_address, width=20, font=('times new roman', 13))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # ==========Teacher name==========
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=(
            'times new roman', 13, 'bold'), bg='white')
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_teacher, width=20, font=('times new roman', 13))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # ==========Radio Buttons==========
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Don't take Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # ==========Button Frame==========
        btn_frame = Frame(class_student_frame, bd=0, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=200, width=705, height=35)

        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=13, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        save_btn.grid(row=0, column=0, padx=19)

        update_btn = Button(btn_frame, command=self.update_data, text="Update", width=13, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        update_btn.grid(row=0, column=1, padx=19)

        delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=13, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        delete_btn.grid(row=0, column=2, padx=19)

        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=13, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        reset_btn.grid(row=0, column=3, padx=19)

        btn_frame1 = Frame(class_student_frame, bd=0, relief=RIDGE, bg='white')
        btn_frame1.place(x=0, y=240, width=705, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_or_update_dataset, text="Take Photo Sample", width=30, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        take_photo_btn.grid(row=0, column=0, padx=21)

        update_photo_btn = Button(btn_frame1, command=self.generate_or_update_dataset, text="Update Photo Sample", width=30, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        update_photo_btn.grid(row=0, column=1, padx=21)

        # ==========Right label frame==========
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Student Records", font=(
            'times new roman', 13, 'bold'))
        right_frame.place(x=750, y=10, width=720, height=580)

        # img_right = Image.open(
        #     r"Images\student_info.jpg")
        # img_right = img_right.resize((710, 130), Image.ANTIALIAS)
        # self.photoimg_right = ImageTk.PhotoImage(img_right)

        # img_right = Label(right_frame, image=self.photoimg_right)
        # img_right.place(x=5, y=0, width=710, height=130)

        # =========Search System============
        search_frame = LabelFrame(right_frame, bd=2, bg='white', relief=RIDGE,
                                  text="Search System", font=('times new roman', 13, 'bold'))
        search_frame.place(x=5, y=0, width=710, height=70)

        search_label = Label(search_frame, text="Search By:", font=(
            'times new roman', 15, 'bold'), bg='white')
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.var_search_combo = StringVar()
        search_combo = ttk.Combobox(search_frame, font=(
            'times new roman', 13), textvariable=self.var_search_combo, state='readonly', width=15)
        search_combo['values'] = ('Student_id', 'Roll_no', 'Phone', 'Email', 'Name')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(
            search_frame, width=15, textvariable=self.var_search, font=('times new roman', 13))
        # search_entry.insert(0, f"Enter {self.var_search_combo.get()}")
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, command=self.search, text="Search", width=10, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        search_btn.grid(row=0, column=3, padx=4)

        searchAll_btn = Button(search_frame, command=self.fetch_data, text="Search All", width=10, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        searchAll_btn.grid(row=0, column=4, padx=4)

        # =========Table Frame============
        table_frame = Frame(right_frame, bd=2, bg='white', relief=RIDGE)
        table_frame.place(x=5, y=80, width=710, height=475)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", 'name', "batch", "roll", "gender",
                                          "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("roll", text="URN")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100, anchor=CENTER)
        self.student_table.column("course", width=100, anchor=CENTER)
        self.student_table.column("year", width=100, anchor=CENTER)
        self.student_table.column("sem", width=100, anchor=CENTER)
        self.student_table.column("id", width=100, anchor=CENTER)
        self.student_table.column("name", width=100, anchor=CENTER)
        self.student_table.column("batch", width=100, anchor=CENTER)
        self.student_table.column("roll", width=100, anchor=CENTER)
        self.student_table.column("dob", width=100, anchor=CENTER)
        self.student_table.column("email", width=100, anchor=CENTER)
        self.student_table.column("gender", width=100, anchor=CENTER)
        self.student_table.column("phone", width=100, anchor=CENTER)
        self.student_table.column("address", width=100, anchor=CENTER)
        self.student_table.column("teacher", width=100, anchor=CENTER)
        self.student_table.column("photo", width=100, anchor=CENTER)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============Functional Declaration============

    # ============Add Data into Database============
    def add_data(self):
        if self.all_field_required() == False:
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_batch.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student Details has been added Successfully.", parent=self.root)

                if self.var_radio1.get() == "Yes":
                    take_img = messagebox.askyesno(
                        "Message", "Are you ready for pictures.", parent=self.root)
                    if take_img > 0:
                        self.generate_or_update_dataset(self.var_std_id.get())
                        # pass

                self.reset_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ============Fetch Data============
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        all_students = my_cursor.fetchall()

        if len(all_students) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for student in all_students:
                self.student_table.insert("", END, values=student)
            conn.commit()
        conn.close()

    # ============Populate Fields with selected record in database============
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        # print('Get Cursor Function called')

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_batch.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # ============Update Function============
    def update_data(self):
        if self.all_field_required() == False:
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to update this student details", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
                    my_cursor = conn.cursor()

                    query = "select * from student where Student_id=%s"
                    value = (self.var_std_id.get(),)

                    my_cursor.execute(query, value)
                    data = my_cursor.fetchone()

                    # print(data)
                    if data == None:
                        messagebox.showerror(
                            "Error", f"No Student with id {self.var_std_id.get()} found.", parent=self.root)
                        return

                    my_cursor.execute("update student set Dep=%s,Course=%s, Year=%s,Semester=%s,Name=%s,Batch=%s,Roll_no=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_batch.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                elif not update:
                    return
                messagebox.showinfo(
                    "Success", "Student details successfully updated.", parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ============Delete Function============
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student data.", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
                    my_cursor = conn.cursor()

                    query = "select * from student where Student_id=%s"
                    value = (self.var_std_id.get(),)

                    my_cursor.execute(query, value)
                    data = my_cursor.fetchone()

                    # print(data)
                    if data == None:
                        messagebox.showerror(
                            "Error", f"No Student with id {self.var_std_id.get()} found.", parent=self.root)
                        return

                    query = "delete from student where Student_id=%s"
                    value = (self.var_std_id.get(),)
                    my_cursor.execute(query, value)
                elif not delete:
                    return

                conn.commit()
                self.fetch_data()

                try:
                    for i in range(1, 11):
                        os.remove(f'data/student.{self.var_std_id.get()}.{i}.jpg')
                except OSError:
                    pass

                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root)
                self.reset_data()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ============Reset Function============
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set("19530"),
        self.var_std_name.set(""),
        self.var_batch.set("8CSE4"),
        self.var_roll.set("19EUCCS060"),
        self.var_gender.set("Male"),
        self.var_dob.set("dd/mm/yy"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        self.var_search_combo.set("Student_Id")
        self.var_search.set("")

    # ============Generate data set or Take photo sample============
    def generate_or_update_dataset(self, Id=''):
        if Id == "":
            if self.all_field_required() == False:
                messagebox.showerror(
                    "Error", "All Fields are required", parent=self.root)
            else:
                try:
                    if self.var_radio1.get() != "Yes":
                        messagebox.showerror(
                            "Error", "Please Check the 'Take Photo Sample' Radio Button", parent=self.root)
                        return

                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student")
                    data = my_cursor.fetchall()
                    # print(data)

                    id = "-1"
                    for row in data:
                        # print(row[4], type(self.var_std_id.get()))
                        if row[4] == self.var_std_id.get():
                            id = row[4]
                            break

                    # print(id)
                    if id == "-1":
                        messagebox.showerror(
                            "Error", f"No Student with id {self.var_std_id.get()} found.", parent=self.root)
                        return

                    my_cursor.execute("update student set Dep=%s,Course=%s, Year=%s,Semester=%s,Name=%s,Batch=%s,Roll_no=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosample=%s where Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_batch.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        id
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    self.helper_generate_dataset(id)
                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Due To :{str(es)}", parent=self.root)
        else:
            self.helper_generate_dataset(Id)

    # ============Helper function for generate_dataset funciton============
    def helper_generate_dataset(self, id):
        # ============== Load predefined data on face frontals from opencv==============
        face_classifier = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            # scaling factor=1.3
            # Minimum Neighbour=5

            for (x, y, w, h) in faces:
                face_cropped = img[y:y+h, x:x+w]
                return face_cropped

        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, my_frame = cap.read()
            if face_cropped(my_frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(my_frame), (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = "data/student." + \
                    str(id)+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(img_id), (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 13 or int(img_id) == 5:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Result", "Generating data sets completed", parent=self.root)

    # ============Validity Function============
    def all_field_required(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_batch.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "dd/mm/yy" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "" or self.var_radio1.get() == "":
            return False
        else:
            return True

    # ============Search Function============
    def search(self):
        if self.var_search.get() == "":
            messagebox.showerror(
                "Error", f"Please Enter {self.var_search_combo.get()}.", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Mysql@2023", database="face_recognition_enabled_attendance_system")
            my_cursor = conn.cursor()

            query = f"select * from student where {self.var_search_combo.get()}=%s"
            value = (self.var_search.get(),)

            my_cursor.execute(query, value)
            all_results = my_cursor.fetchall()

            if len(all_results) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for student in all_results:
                    self.student_table.insert("", END, values=student)
                conn.commit()
                conn.close()
            else:
                messagebox.showerror(
                    "Error", f"No Student with {self.var_search_combo.get()} {self.var_search.get()} found.", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("Images/rtu_logo.ico")
    obj = Student(root)
    root.mainloop()
