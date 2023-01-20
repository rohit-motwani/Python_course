from tkinter import *
import mysql.connector as m
conn = m.connect(user='root', password='Kishan@1072', host='localhost',
database='student')
cursor = conn.cursor()
def insert():
    sqlformula = "insert into details(id, name, year, dept) values (%s, %s, %s, %s)"
    info = (int(e0.get()), e1.get(), val.get(), lb.get(lb.curselection()))
    cursor.execute(sqlformula, info) 
    conn.commit()
    e0.delete(0, END)
    e1.delete(0, END)
    lb.selection_clear(0, END)
def delete():
    if e0.get():
        sqlformula = "delete from details where id = %s"
        name = (e0.get(),)
        cursor.execute(sqlformula, name)
        conn.commit()
    elif e1.get():
        sqlformula = "delete from details where name = %s"
        name = (e1.get(),)
        cursor.execute(sqlformula, name)
        conn.commit()
    elif lb.curselection():
        sqlformula = "delete from details where dept = %s"
        dept = (lb.get(lb.cureselection()),)
        cursor.execute(sqlformula, dept)
        conn.commit()
        lb.selection_clear(0, END)
    else:
        sqlformula = "delete from details where year = %s"
        year = (val.get(),)
        cursor.execute(sqlformula, year)
        conn.commit()
    e0.delete(0, END)
    e1.delete(0, END)
    lb.selection_clear(0, END)

def update():
    sqlformula = "update details set year = %s, dept = %s where id = %s"
    info = (val.get(), lb.get(lb.cureselection()), e0.get())
    cursor.execute(sqlformula, info)
    conn.commit()
    e0.delete(0, END)
    e1.delete(0, END)
    lb.selection_clear(0, END)

def show():
    cursor.execute("select * from details")
    for i in cursor:
        print(i)
    print('*'*20, end="\n")
    e0.delete(0, END)
    e1.delete(0, END)
    lb.selection_clear(0, END)

root = Tk()
root.geometry("300x300")
f1 = Frame(root, height = 300, width = 300)
f1.propagate(0)
f1.pack()
l0 = Label(f1, text="ID: ")
l0.place(x=10, y=10)
l1 = Label(f1, text="Name:")
l1.place(x=10, y=60)
l2 = Label(f1, text="Year: ")
l2.place(x=10, y=110)
l3 = Label(f1, text="Dept: ")
l3.place(x=10, y=170)
e0 = Entry(f1, width=10)
e0.place(x=60, y=10)
e1 = Entry(f1, width=10)
e1.place(x=60, y=60)
val = StringVar()
s1 = Spinbox(f1, values = ('SE', 'TE', 'BE'), textvariable=val, width = 10)
s1.place(x=60, y=110)
lb = Listbox(f1, height = 2, width = 20, selectmode = SINGLE)
lb.place(x=60, y=170)
list1 = ['COMP','IT','EXTC','CHEM']
for i in list1: 
    lb.insert(END, i)
b1=Button(f1,text="INSERT",width=7,command=insert)
b2=Button(f1,text="DELETE",width=7,command=delete)
b3=Button(f1,text="UPDATE",width=7,command=update)
b4=Button(f1,text="SHOW",width=7,command=show)
b5=Button(f1,text="EXIT",width=7,command=root.destroy)
b1.place(x=10,y=220)
b2.place(x=80,y=220)
b3.place(x=150,y=220)
b4.place(x=50,y=270)
b5.place(x=120,y=270)
root.mainloop()