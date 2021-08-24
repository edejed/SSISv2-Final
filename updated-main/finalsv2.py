from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="beige",fg="black")
        title.pack(side=TOP,fill=X)
#-----all variables
        self.Student_ID_var=StringVar()
        self.Name_var=StringVar()
        self.Gender_var=StringVar()
        self.Year_Level_var=StringVar()
        self.Course_Code_var=StringVar()
        self.Course_var=StringVar()
        self.search_by_var = StringVar()
        self.search_txt_var = StringVar()
        self.manage_course = StringVar()
        self.course_name = StringVar()
        self.search_course_var = StringVar()


#----------manage frame

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="beige")
        Manage_Frame.place(x=20,y=100,width=450,height=300)

        m_title=Label(Manage_Frame,text="Manage Students",bg="beige",fg="black",font=("times new roman",18,"bold"))
        m_title.grid(row=0,columnspan=1,pady=20)

        lbl_studentID=Label(Manage_Frame,text="Student ID",bg="beige",fg="black",font=("times new roman",15,"bold"))
        lbl_studentID.grid(row=1,column=0,pady=0,padx=5,sticky="w")

        txt_studentID=Entry(Manage_Frame,textvariable=self.Student_ID_var,font=("times new roman",12,"bold"),bd=5, relief=GROOVE)
        txt_studentID.grid(row=1,column=1,pady=0,padx=0,sticky="w")

        lbl_name= Label(Manage_Frame, text="Name", bg="beige", fg="black",font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=0, padx=5, sticky="w")

        txt_name= Entry(Manage_Frame,textvariable=self.Name_var, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=0, padx=0, sticky="w")

        lbl_gender= Label(Manage_Frame, text="Gender", bg="beige", fg="black", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=3, column=0, pady=0, padx=5, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",12,"bold"), state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=3,column=1,pady=0,padx=0,sticky="w")

        lbl_yearLevel= Label(Manage_Frame, text="Year Level", bg="beige", fg="black", font=("times new roman", 15, "bold"))
        lbl_yearLevel.grid(row=4, column=0, pady=0, padx=5, sticky="w")

        txt_yearLevel= Entry(Manage_Frame,textvariable=self.Year_Level_var, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        txt_yearLevel.grid(row=4, column=1, pady=0, padx=0, sticky="w")

        lbl_courseCode = Label(Manage_Frame, text="Course Code", bg="beige", fg="black", font=("times new roman", 15, "bold"))
        lbl_courseCode.grid(row=5, column=0, pady=0, padx=5, sticky="w")

        combo_courseCode = ttk.Combobox(Manage_Frame, textvariable=self.Course_Code_var,font=("times new roman", 12, "bold"),state='readonly')
        combo_courseCode['values'] = self.course_list()
        combo_courseCode.grid(row=5, column=1, pady=0, padx=5,sticky="w")

        #-------button frame
        bttn_Frame = Frame(Manage_Frame, bd=2, relief=RIDGE, bg="beige")
        bttn_Frame.place(x=5, y=230, width=430)

        Addbtn = Button(bttn_Frame,text="Add",width=10,command=self.add_students)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)
        Updatebtn = Button(bttn_Frame, text="Update", width=10,command=self.update_data)
        Updatebtn.grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(bttn_Frame, text="Delete", width=10,command=self.delete_data)
        Deletebtn.grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(bttn_Frame, text="Clear", width=10,command=self.clear)
        Clearbtn.grid(row=0, column=3, padx=10, pady=10)

#-----frame2
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="beige")
        Manage_Frame.place(x=20, y=400, width=450, height=220)

        m_title = Label(Manage_Frame, text="Manage Course", bg="beige", fg="black",font=("times new roman", 18, "bold"))
        m_title.grid(row=0, columnspan=1, pady=20)

        lbl_course1 = Label(Manage_Frame, text="Course Code", bg="beige", fg="black",font=("times new roman", 15, "bold"))
        lbl_course1.grid(row=4, column=0, pady=0, padx=5, sticky="w")

        txt_course1 = Entry(Manage_Frame, textvariable=self.manage_course, font=("times new roman", 12, "bold"),bd=5, relief=GROOVE)
        txt_course1.grid(row=4, column=1, pady=0, padx=0, sticky="w")

        lbl_courseCode = Label(Manage_Frame, text="Course", bg="beige", fg="black",font=("times new roman", 15, "bold"))
        lbl_courseCode.grid(row=5, column=0, pady=0, padx=5, sticky="w")

        txt_course2 = Entry(Manage_Frame, textvariable=self.course_name, font=("times new roman", 12, "bold"), bd=5,
                            relief=GROOVE)
        txt_course2.grid(row=5, column=1, pady=0, padx=0, sticky="w")

        #--botton frame

        bttn_Frame = Frame(Manage_Frame, bd=2, relief=RIDGE, bg="beige")
        bttn_Frame.place(x=5, y=150, width=430)

        #course
        Addbtn = Button(bttn_Frame, text="Add", width=10, command=self.add_course)
        Addbtn.grid(row=0, column=0, padx=10, pady=10)
        Updaters = Button(bttn_Frame, text="Update", width=10, command=self.update_course)
        Updaters.grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(bttn_Frame, text="Delete", width=10, command=self.delete_course)
        Deletebtn.grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(bttn_Frame, text="Clear", width=10, command=self.clears)
        Clearbtn.grid(row=0, column=3, padx=10, pady=10)



        #--------detail frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="beige")
        Detail_Frame.place(x=500,y=100,width=750,height=300)

        lbl_search=Label(Detail_Frame,text="Search By Students", bg="beige",fg="black",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")



        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt_var, width=15, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", width=10,pady=5,command=self.search_data)
        Searchbtn.grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Detail_Frame, text="Show All", width=10,pady=5,command=self.fetch_data)
        Showallbtn.grid(row=0, column=4, padx=10, pady=10)

#-----table frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=GROOVE,bg="beige")
        Table_Frame.place(x=10,y=60,width=725,height=220)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_tables=ttk.Treeview(Table_Frame,columns=("Student ID","Name","Gender","Year Level","Course Code"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_tables.xview)
        scroll_y.config(command=self.Student_tables.yview)
        self.Student_tables.heading("Student ID", text="Student ID")
        self.Student_tables.heading("Name", text="Name")
        self.Student_tables.heading("Gender", text="Gender")
        self.Student_tables.heading("Year Level", text="Year Level")
        self.Student_tables.heading("Course Code", text="Course Code")
        self.Student_tables['show']="headings"
        self.Student_tables.column("Student ID",width=100)
        self.Student_tables.column("Name", width=100)
        self.Student_tables.column("Gender", width=100)
        self.Student_tables.column("Year Level", width=100)
        self.Student_tables.column("Course Code", width=100)
        self.Student_tables.pack(fill=BOTH,expand=1)
        self.Student_tables.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # ---frame2 search

    # --------detail frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="beige")
        Detail_Frame.place(x=500, y=390, width=750, height=230)

        lbl_search = Label(Detail_Frame, text="Search By Course", bg="beige", fg="black",
                       font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")


        course_Search = Entry(Detail_Frame, textvariable=self.search_course_var, width=15,
                       font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        course_Search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        Searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_course)
        Searchbtn.grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_course)
        Showallbtn.grid(row=0, column=4, padx=10, pady=10)

        # -----table frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=GROOVE, bg="beige")
        Table_Frame.place(x=10, y=50, width=725, height=170)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Course_table = ttk.Treeview(Table_Frame, columns=(
            "Course Code", "Course"), xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Course_table.xview)
        scroll_y.config(command=self.Course_table.yview)
        self.Course_table.heading("Course Code", text="Course Code")
        self.Course_table.heading("Course", text="Course")
        self.Course_table['show'] = "headings"
        self.Course_table.column("Course Code", width=100)
        self.Course_table.column("Course", width=200)
        self.Course_table.pack(fill=BOTH, expand=1)
        self.Course_table.bind("<ButtonRelease-1>", self.get_cursors)

        self.fetch_course()


    def course_list(self):
        connection = sqlite3.connect('students.db')
        cur = connection.cursor()
        cur.execute("SELECT course_code FROM courses")
        rows = cur.fetchall()
        rows = [list(i) for i in rows]
        for i in range(len(rows)):
            rows[i] = rows[i][0]
        return rows


    def add_course(self):
        if self.manage_course.get()=="" or self.course_name.get()=="":
                messagebox.showerror("Error", "All fields are required!!")
        else:

            con = sqlite3.connect('students.db')
            cur = con.cursor()
            cur.execute("INSERT INTO courses values(?,?)", (self.manage_course.get(), self.course_name.get()))
            con.commit()
            self.fetch_course()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Student Added Successfully")

    def add_students(self):
        if self.Student_ID_var.get()==""or self.Name_var.get()=="":
                messagebox.showerror("Error","All fields are required!!")
        else:

            con=sqlite3.connect('students.db')
            cur=con.cursor()
            cur.execute("insert into information values(?,?,?,?,?)",(self.Student_ID_var.get(),
                                                                              self.Name_var.get(),
                                                                              self.Gender_var.get(),
                                                                              self.Year_Level_var.get(),
                                                                              self.Course_Code_var.get(),
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Student Added Successfully")

    def fetch_data(self):
        connection = sqlite3.connect('students.db')
        cur = connection.cursor()
        cur.execute("SELECT * FROM information")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_tables.delete(*self.Student_tables.get_children())
                for row in rows:
                    self.Student_tables.insert('',END,values=row)
                connection.commit()
        connection.close()

    def fetch_course(self):
        connection = sqlite3.connect('students.db')
        cur = connection.cursor()
        cur.execute("SELECT * FROM courses")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Course_table.delete(*self.Course_table.get_children())
                for row in rows:
                    self.Course_table.insert('',END,values=row)
                connection.commit()
        connection.close()

    def clear(self):
        self.Student_ID_var.set("")
        self.Name_var.set("")
        self.Gender_var.set("")
        self.Year_Level_var.set("")
        self.Course_Code_var.set("")
        self.Course_var.set("")

    def clears(self):
        self.manage_course.set("")
        self.course_name.set("")

    def get_cursor(self,row):
        curosor_row=self.Student_tables.focus()
        contents=self.Student_tables.item(curosor_row)
        row=contents['values']
        self.Student_ID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Gender_var.set(row[2])
        self.Year_Level_var.set(row[3])
        self.Course_Code_var.set(row[4])

    def get_cursors(self,row):
        curosor_row=self.Course_table.focus()
        contents=self.Course_table.item(curosor_row)
        row=contents['values']
        self.manage_course.set(row[0])
        self.course_name.set(row[1])

    def update_data(self):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        data1 = self.Student_ID_var.get()
        data2 = self.Name_var.get()
        data3 = self.Gender_var.get()
        data4 = self.Year_Level_var.get()
        data5 = self.Course_Code_var.get()

        selected = self.Student_tables.selection()
        self.Student_tables.item(selected, values=(data1, data2, data3, data4, data5))
        c.execute(
            "UPDATE information set  student_id=?, name=?, Gender=?, Year_Level=?, Course=?  WHERE student_id=? ",
            (data1, data2, data3, data4, data5, data1))

        conn.commit()
        conn.close()

        self.del_data()
        self.fetch_data()

    def update_course(self):
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        data1 = self.manage_course.get()
        data2 = self.course_name.get()

        selected = self.Course_table.selection()
        self.Course_table.item(selected, values=(data1, data2))
        c.execute(
            "UPDATE courses set  course_code=?, course=? WHERE course_code=? ",
            (data1, data2, data1))

        conn.commit()
        conn.close()

        self.del_data()
        self.fetch_course()


    def del_data(self):
        for record in self.Student_tables.get_children():
            self.Student_tables.delete(record)

    def del_course(self):
        for record in self.Course_table.get_children():
            self.Course_table.delete(record)

    def delete_data(self):
        if messagebox.askyesno("Delete Confirmation", "Are you sure?") == False:
            return
        else:
            conn = sqlite3.connect("Students.db")
            c = conn.cursor()
            selected = self.Student_tables.focus()
            values = self.Student_tables.item(selected, 'values')

            c.execute("DELETE from information WHERE student_id=?", (values[0],))

            conn.commit()
            conn.close()

        self.del_course()
        self.displaydata()

    def delete_course(self):
        if messagebox.askyesno("Delete Confirmation", "Are you sure?") == False:
            return
        else:
            conn = sqlite3.connect("Students.db")
            c = conn.cursor()
            selected = self.Course_table.focus()
            values = self.Course_table.item(selected, 'values')

            c.execute("DELETE from courses WHERE course_code=?", (values[0],))

            conn.commit()
            conn.close()

        self.del_course()
        self.displaydata2()


    def displaydata(self):
        conn = sqlite3.connect('students.db')

        c = conn.cursor()

        c.execute("SELECT * FROM information")
        records = c.fetchall()

        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                self.Student_table.insert(parent='', index='end', iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
            else:
                self.Student_table.insert(parent='', index='end', iid=count, text='',
                            values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
            count += 1

        return

    def displaydata2(self):
        conn = sqlite3.connect('students.db')

        c = conn.cursor()

        c.execute("SELECT * FROM courses")
        records = c.fetchall()

        global count2
        count2 = 0

        for record in records:
            if count2 % 2 == 0:
                self.Course_table.insert(parent='', index='end', iid=count2, text='', values=(record[0], record[1]),
                             tags=('evenrow',))
            else:
                self.Course_table.insert(parent='', index='end', iid=count2, text='', values=(record[0], record[1]),
                             tags=('oddrow',))
            count2 += 1

        return

    def search_data(self):
        for record in self.Student_tables.get_children():
            self.Student_tables.delete(record)

        conn = sqlite3.connect('students.db')
        c = conn.cursor()

        c.execute("SELECT * FROM information WHERE student_id=? ", (self.search_txt_var.get(),))
        records = c.fetchall()

        for i in records:
            self.Student_tables.insert('', 'end', value=i)

        if self.search_txt_var.get() == '':
            self.del_data()
            self.displaydata()
        return

    def searchb(self):
        for record in self.Student_tables.get_children():
            Student_tables.delete(record)

        conn = sqlite3.connect('students.db')
        c = conn.cursor()

        c.execute("SELECT * FROM information WHERE student_id=? ", (self.search_txt_var.get(),))
        records = c.fetchall()

        for i in records:
            self.Student_tables.insert('', 'end', value=i)

        if self.search_txt_var.get() == '':
            self.del_data()
            self.displaydata()
        return

    def search_course(self):
        for record in self.Course_table.get_children():
            self.Course_table.delete(record)

        conn = sqlite3.connect('students.db')
        c = conn.cursor()

        c.execute("SELECT * FROM courses WHERE course_code=? ", (self.search_course_var.get(),))
        records = c.fetchall()

        for i in records:
            self.Course_table.insert('', 'end', value=i)

        if self.search_course_var.get() == '':
            self.del_course()
            self.displaydata2()
        return

    def searcha(self):
        for record in self.Student_tables.get_children():
            Student_tables.delete(record)

        conn = sqlite3.connect('students.db')
        c = conn.cursor()

        c.execute("SELECT * FROM courses WHERE course_code=? ", (self.search_course_var.get(),))
        records = c.fetchall()

        for i in records:
            self.Course_table.insert('', 'end', value=i)

        if self.search_course_var.get() == '':
            self.del_course()
            self.displaydata2()
        return

root=Tk()
ob=student(root)
root.mainloop()
