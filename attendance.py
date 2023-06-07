from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import csv
from tkinter import filedialog
import datetime

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Attendance")

        # ==========Variables==========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ==========Background Image==========
        bg_img = Image.open(
            r"Images\attendance_bg.png")
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
        left_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Student Attendance Details", font=(
            'times new roman', 12, 'bold'))
        left_frame.place(x=10, y=10, width=720, height=580)

        img_left = Image.open(
            r"Images\student_info.jpg")
        img_left = img_left.resize((710, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        img_left = Label(left_frame, image=self.photoimg_left)
        img_left.place(x=5, y=0, width=710, height=130)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg='white')
        left_inside_frame.place(x=5, y=135, width=705, height=415)

        # ==========Attendance id==========
        student_id_label = Label(left_inside_frame, text="StudentID:", font=(
            'times new roman', 13, 'bold'), bg='white')
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        student_id_entry = ttk.Entry(
            left_inside_frame, width=20, textvariable=self.var_atten_id, font=('times new roman', 13))
        student_id_entry.insert(0, 'Ex: 19XXX')
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # ==========URN==========
        univ_roll_label = Label(left_inside_frame, text="URN:", font=(
            'times new roman', 13, 'bold'), bg='white')
        univ_roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        univ_roll_entry = ttk.Entry(
            left_inside_frame, width=20, textvariable=self.var_atten_roll, font=('times new roman', 13))
        univ_roll_entry.insert(0, "Ex: 19EUCCSXXX")
        univ_roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # ==========Name==========
        name_label = Label(left_inside_frame, text="Name:", font=(
            'times new roman', 13, 'bold'), bg='white')
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(
            left_inside_frame, width=20, textvariable=self.var_atten_name, font=('times new roman', 13))
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # ==========Department==========
        dep_label = Label(left_inside_frame, text="Department:", font=(
            'times new roman', 13, 'bold'), bg='white')
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        dep_entry = ttk.Entry(
            left_inside_frame, width=20, textvariable=self.var_atten_dep, font=('times new roman', 13))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # ==========Time==========
        time_label = Label(left_inside_frame, text="Time:", font=(
            'times new roman', 13, 'bold'), bg='white')
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(
            left_inside_frame, width=20, textvariable=self.var_atten_time, font=('times new roman', 13))
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # ==========Date==========
        date_label = Label(left_inside_frame, text="Date:", font=(
            'times new roman', 13, 'bold'), bg='white')
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(
            left_inside_frame, width=20, textvariable=self.var_atten_date, font=('times new roman', 13))
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # ==========Attendance==========
        atten_label = Label(left_inside_frame, text="Attendance Status:", font=(
            'times new roman', 13, 'bold'), bg='white')
        atten_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        atten_combo = ttk.Combobox(left_inside_frame, font=(
            'times new roman', 13), textvariable=self.var_atten_attendance, state='readonly', width=18)
        atten_combo['values'] = ('Status', 'Present', 'Absent')
        atten_combo.current(0)
        atten_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # ==========Button Frame==========
        btn_frame = Frame(left_inside_frame, bd=0, relief=RIDGE, bg='white')
        btn_frame.place(x=10, y=350, width=675, height=35)

        import_btn = Button(btn_frame, command=self.import_csv, text="Import CSV", width=10, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        import_btn.grid(row=0, column=0, padx=27)

        # export_btn = Button(btn_frame, command=self.export_csv, text="Export CSV", width=10, font=(
        #     'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        # export_btn.grid(row=0, column=1, padx=13)

        add_btn = Button(btn_frame, text="Add", command=self.add_data, width=10, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        add_btn.grid(row=0, column=1, padx=27)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=10, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        update_btn.grid(row=0, column=2, padx=27)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=10, font=(
            'times new roman', 13, 'bold'), bg="thistle4", fg='black')
        reset_btn.grid(row=0, column=3, padx=27)

        # ==========Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg='white', relief=RIDGE, text="Attendance Records", font=(
            'times new roman', 13, 'bold'))
        right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg='white')
        table_frame.place(x=5, y=5, width=705, height=550)

        # ==========Scroll bar Table==========
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendaceReportTable = ttk.Treeview(table_frame, columns=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Student_id")
        self.AttendaceReportTable.heading("roll", text="URN")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("attendance", text="Attendance")

        self.AttendaceReportTable['show'] = "headings"

        self.AttendaceReportTable.column("id", width=100, anchor='center')
        self.AttendaceReportTable.column("roll", width=100, anchor='center')
        self.AttendaceReportTable.column("name", width=100, anchor='center')
        self.AttendaceReportTable.column(
            "department", width=100, anchor='center')
        self.AttendaceReportTable.column("time", width=100, anchor='center')
        self.AttendaceReportTable.column("date", width=100, anchor='center')
        self.AttendaceReportTable.column(
            "attendance", width=100, anchor='center')

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ==========Fetch Data==========
    def fetch_data(self, rows):
        self.AttendaceReportTable.delete(
            *self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("", END, values=i)

    # ==========Import CSV Button==========
    def import_csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd()+'/attendance/', title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        # print(fln)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # ==========Export CSV Button==========
    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No data found to export", parent=self.root)
                return False

            now = datetime.datetime.now()

            fln = filedialog.asksaveasfilename(initialdir=os.getcwd()+'/attendance/', initialfile=f'{now.strftime("%d-%m-%Y")}.csv', title="Export CSV", filetypes=(
                ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, "w", newline="\n") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " +
                                    os.path.basename(fln)+" successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendaceReportTable.focus()
        content = self.AttendaceReportTable.item(cursor_row)
        row = content["values"]

        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])

    # ==========Add Button==========
    def add_data(self):
        now = datetime.datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")
        self.update_data([self.var_atten_id.get(),
                          self.var_atten_roll.get(),
                          self.var_atten_name.get(),
                          self.var_atten_dep.get(),
                          dtString,
                          d1,
                          'Present'])

    # ==========Update Button==========
    def update_data(self, data=[]):
        r = csv.reader(open('attendance.csv'))
        lines = list(r)
        # print(lines)
        if data == []:
            for line in lines:
                if line[0] == self.var_atten_id.get():
                    line[4] = self.var_atten_time.get()
                    line[6] = self.var_atten_attendance.get()
                    break
        else:
            flag = 1
            for line in lines:
                if line[0] == self.var_atten_id.get():
                    flag = 0
                    break
            if flag == 1:
                lines.append(data)

        writer = csv.writer(open('attendance.csv', 'w'), lineterminator='\n')
        writer.writerows(lines)
        self.fetch_data(lines)

    # ==========Reset Button==========
    def reset_data(self):
        self.var_atten_id.set("Ex: 19XXX")
        self.var_atten_roll.set("Ex: 19EUCCSXXX")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")


if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("Images/rtu_logo.ico")
    obj = Attendance(root)
    root.mainloop()
