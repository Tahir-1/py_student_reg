import mysql.connector
import tkinter as tk
from tkinter import ttk,messagebox

''' create windoww'''
win = tk.Tk()
win.geometry("500x400")
win.title(" Student Info")
ttk.Label(win, text = " Student Info",font="12").grid(column=0,row=0)

''' Connect database '''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "student_info"
)
mycursor = mydb.cursor()

'''Name entry'''
ttk.Label(win , text = " Name : ",font= "10 ").grid(column=1,row=1,pady=6)
name = tk.StringVar()
name_entry = ttk.Entry(win,width=15,textvariable=name)
name_entry.grid(column=2,row=1)

''' Roll number entry'''
ttk.Label(win , text = " Roll no : ",font= "10 ").grid(column=1,row=2,pady=6)
roll = tk.StringVar()
roll_entry = ttk.Entry(win,width=15,textvariable=roll)
roll_entry.grid(column=2,row=2)

''' Phone number entry'''
ttk.Label(win , text = " Phone no : ",font= "10 ").grid(column=1,row=3,pady=6)
phone = tk.StringVar()
phone_entry = ttk.Entry(win,width=15,textvariable=phone)
phone_entry.grid(column=2,row=3)

''' Submit button '''
def submit():
    if name.get() and phone.get() and roll.get():
        sql = "insert into students(name,roll,phone) Values(%s,%s,%s)"
        val = (name.get(),roll.get(),phone.get())
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.execute("select * from students")
        for x in mycursor:
            print(x)
        messagebox.showinfo(win, message = "Student created")


sub = ttk.Button(win, text = " Submit " , command=submit)
sub.grid(row=4,column=1)

''' fill button '''
def fill():
    if roll.get():
        sqlf = "select * from students where roll="+ str(roll.get()) 
        mycursor.execute(sqlf)
        for x in mycursor:
            name_entry.insert(0,x[1])
            phone_entry.insert(0,x[3])
                    
fil = ttk.Button(win, text = "Fill " , command=fill)
fil.grid(column=3,row=2,padx=4)

'''Update button'''
def update():
    if name.get() and phone.get() and roll.get():
        sqlu  = "update students set phone='"+str(phone.get())+ "',name ='"+str(name.get())+"' where roll="+str(roll.get())
        mycursor.execute(sqlu)
        mydb.commit()
        for x in mycursor:
            print(x)
        messagebox.showinfo(win, message = "Student updated")
        
updat = ttk.Button(win, text = " update " , command=update)
updat.grid(row=4,column=2)


''' Delete button'''
ttk.Label(win,text= "Roll no ").grid(row = 5 , column=0 , sticky="e",pady=10)
delid = tk.StringVar()
del_entry = ttk.Entry(win, textvariable= delid)
del_entry.grid(row=5,column=1,pady=10)
def delete():
    if delid.get():
        sqld = "delete from students where roll=" + str(delid.get())
        mycursor.execute(sqld)
        mydb.commit()
        createlist()
        messagebox.showinfo(win, message = "Student Deleted")
dele = ttk.Button(win, text = " delete " , command=delete)
dele.grid(row=5,column=2,pady=10)

''' Database Output'''
frame1 = ttk.Frame(win)
frame1.grid(column=1,row = 6, pady= 10, columnspan=3)
def createlist():
    mycursor.execute("select * from students")
    for i,x in enumerate(mycursor):
        print(i,x)
        inline = ttk.Frame(frame1)
        inline.grid(column=1,columnspan=3,row = i)
        ttk.Label(inline, text = x[1]).grid(column=0,row = 0,pady=2,padx=4)
        ttk.Label(inline, text = x[2]).grid(column=1, row = 0,pady=2,padx=4)
        ttk.Label(inline, text = x[3]).grid(column=2, row = 0,pady=2,padx=4)
createlist()

win.mainloop()