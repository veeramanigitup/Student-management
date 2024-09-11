from tkinter import*
from tkinter import ttk
from  db import Database
from tkinter import messagebox

db=Database("Employee.db")

root=Tk()
root.title("Employee Management System")
root.geometry("1250x600+50+50")
root.config(bg="#C9C3E3")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()
address=StringVar()

#
entries_frame=Frame(root,bg="violet")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Emplyee Management System",font=("Calibri",18,"bold"),bg="violet",fg="white" )
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblName=Label(entries_frame,text="Name",font=("Calibri",12),bg="violet",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10)
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",12 ),width="30")
txtName.grid(row=1,column=1,padx=10,sticky="W")

lblAge=Label(entries_frame,text="Age",font=("Calibri",12),bg="violet",fg="white")
lblAge.grid(row=1,column=3 ,padx=10,pady=10)
txtAge=Entry(entries_frame,textvariable=age,font=("Calibri",12 ),width="30")
txtAge.grid(row=1,column=4,padx=10,sticky="W")

lblDoj=Label(entries_frame,text="Date of Joining",font=("Calibri",12),bg="violet",fg="white")
lblDoj.grid(row=2,column=0,padx=10,pady=10)
txtDoj=Entry(entries_frame,textvariable=doj,font=("Calibri",12 ),width="30")
txtDoj.grid(row=2,column=1,padx=10,sticky="W")

lblGender=Label(entries_frame,text="Gender",font=("Calibri",12),bg="violet",fg="white")
lblGender.grid(row=2,column=3,padx=10,pady=10)
comboGender=ttk.Combobox(entries_frame,font=("Calibri",12),width="28",textvariable=gender ,state="readonly")
comboGender['values']=("Male","Female")
comboGender.grid(row=2,column=4,padx=10,sticky="W")

lblEmail=Label(entries_frame,text="Email Id",font=("Calibri",12),bg="violet",fg="white")
lblEmail.grid(row=3,column=0,padx=10,pady=10)
txtEmail=Entry(entries_frame,textvariable=email,font=("Calibri",12 ),width="30")
txtEmail.grid(row=3,column=1,padx=10,sticky="W")

lblContact=Label(entries_frame,text="Conatct",font=("Calibri",12),bg="violet",fg="white")
lblContact.grid(row=3,column=3,padx=10,pady=10)
txtContact=Entry(entries_frame,textvariable=contact,font=("Calibri",12 ),width="30")
txtContact.grid(row=3,column=4,padx=10,sticky="W")

lblAddress=Label(entries_frame,text="Address",font=("Calibri",12),bg="violet",fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10  )
txtAddress=Text(entries_frame,width=50,height=2,font=("Calibri",12))
txtAddress.grid(row=4,column=1,padx=10,columnspan=4,sticky="W")



#Function
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END,row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)


def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error in Input","please fill all the details")
        return
    db.insert(txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtAddress.get(1.0,END))
    messagebox.showinfo("Success ", "Record Inserted")
    clearAll()
    displayAll()


def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "please fill all the details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(1.0, END))
    messagebox.showinfo("Success ", "Record Updated")
    clearAll()
    displayAll()

def delete_employee():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)



btn_frame=Frame(entries_frame,bg="violet")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="W")
btnAdd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("Calibri",12,"bold"),bg="#16a085",fg="white",bd=0).grid(row=0,column=0,padx=10)

btnEdit=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("Calibri",12,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=2,padx=20)

btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("Calibri",12,"bold"),bg="red",fg="white",bd=0).grid(row=0,column=4,padx=20)

btnClear=Button(btn_frame,command=clearAll,text="Clear Details",width=15,font=("Calibri",12,"bold"),bg="#f39c12",fg="white",bd=0).grid(row=0,column=6,padx=20)


#tree alighn
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=5,y=310,width=1240,height=280)

style=ttk.Style()
style.configure("mystyle.Treeview",font=("Calibri",11),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("Calibri",12) )

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")

tv.heading("1",text="ID")
tv.column("1",width=3)
tv.heading("2",text="Name")
#tv.column("2",width=15)
tv.heading("3",text="Age")
tv.column("3",width=2)
tv.heading("4",text="D.O.J.")
tv.column("4",width=5)
tv.heading("5",text="Email")
#tv.column("5",width=8)
tv.heading("6",text="Gender")
tv.column("6",width=6)
tv.heading("7",text="Contact")
tv.column("7",width=12)
tv.heading("8",text="Address")
#tv.column("8",width=8)

tv.bind("<ButtonRelease-1>",getData)
tv['show']='headings'
tv.pack(fill=X)


displayAll()
root.mainloop()



