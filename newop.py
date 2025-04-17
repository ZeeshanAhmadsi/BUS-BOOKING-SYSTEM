from tkinter import *
from tkinter import messagebox
import subprocess
import bus_booking_system
root=Tk()
root.title("new operator")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
root.state("zoomed")
root.configure(bg='peach puff')
def add_op():
    op_id = id_entry.get()
    op_name = name_entry.get()
    op_address = address_entry.get()
    op_phone = phone.get()
    op_email = email_entry.get()

    if not (op_address and op_id and op_email and op_phone and op_name):
        messagebox.showwarning("Warning", "All entries should be filled.")
        return

    existing_operators = bus_booking_system.read_operators()
    
    if any(operator[0] == op_id for operator in existing_operators):
        messagebox.showerror("Error", f"Operator with ID {op_id} already exists.")
        return
    
    

    if len(op_phone) != 10 or op_phone.isalpha():
        messagebox.showerror("Error", "Mobile No. should be of ten digits Integer")
        return

    operator_data = (op_id, op_name, op_address, op_phone, op_email)

    bus_booking_system.add_operator(operator_data)

    messagebox.showinfo("Successful", "Operator added successfully: Thank you")

    show_details = Label(frame4, text=f"{op_id}  {op_name}  {op_address}  {op_phone}  {op_email}")
    show_details.grid(row=4, column=5)


    id_entry.delete(0,END)
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    phone.delete(0,END)
    email_entry.delete(0,END)






def edit_op():
    op_id_edit=id_entry.get()
    op_name=name_entry.get()
    op_address=address_entry.get()
    op_phone=phone.get()
    op_email=email_entry.get()

    existing_operators=bus_booking_system.read_operators()
    operator_edit=None
    
    for op in existing_operators:
        if op[0]==op_id_edit:
            operator_edit=op
            break

    if operator_edit is None:
        messagebox.showerror("Error",f" Operator with Id { op_id_edit} not found.")
        return 

    if not (op_address and op_id_edit and op_email and op_phone and op_name):
        messagebox.showwarning("Warning","All entries should be filled.")
        return
    
    
    if len(op_phone) != 10 or op_phone.isalpha():
        messagebox.showerror("Error", "Mobile No. should be of ten digits Integer")
        return

    

    response=messagebox.askyesno("message","Are you Sure You want to edit ?")

    if response==1:
        operator_data=(op_id_edit,op_name,op_address,op_phone,op_email)
        bus_booking_system.edit_operator(op_id_edit,operator_data)
        messagebox.showinfo("successful",'''Operator Edited successfully : Thank you''')

    else:

        return 
    
   

    show_details=Label(frame4,text=f"{op_id_edit}  {op_name}  {op_address}  {op_phone}  {op_email}")
    show_details.grid(row=4,column=5)

    id_entry.delete(0,END)
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    phone.delete(0,END)
    email_entry.delete(0,END)
 


def home():
    root.destroy()
    subprocess.run(["python","homepage.py"])
    

frame=Frame(root,bd=0,bg='peach puff')
frame.grid(row=1,column=1,columnspan=6,padx=130)
frame1=Frame(root,bd=0,bg='peach puff')
frame1.grid(row=2,column=1,columnspan=6,padx=130)
frame2=Frame(root,bd=0,bg='peach puff')
frame2.grid(row=3,column=6,columnspan=6,padx=130)
frame4=Frame(root,bd=0,bg='peach puff')
frame4.grid(row=4,column=6,columnspan=6,padx=130)
bus=PhotoImage(file='star.png')
buzz=PhotoImage(file='home.png')
Label(frame,image=bus).grid(row=1,column=1,padx=130)
Label(frame,text=' Online Bus Booking System',font="Times 28 bold",bg='chartreuse',fg='grey22').grid(row=2,column=1,padx=130,pady=10)
Label(frame,text=' Add Bus Operator Details',font="Times 22 bold",bg='pale green',fg='grey22').grid(row=3,column=1,padx=130,pady=10)
Label(frame1,text=' Opertor id',font="Times 15 bold",bg='hot pink',fg='grey22').grid(row=4,column=0,padx=5,pady=10)
Label(frame1,text=' Name',font="Times 15 bold",bg='hot pink',fg='grey22').grid(row=4,column=2,padx=5,pady=10)
Label(frame1,text=' Address',font="Times 15 bold",bg='hot pink',fg='grey22').grid(row=4,column=4,padx=5,pady=10)
Label(frame1,text=' Phone',font="Times 15 bold",bg='hot pink',fg='grey22').grid(row=4,column=6,padx=5,pady=10)
Label(frame1,text=' Email',font="Times 15 bold",bg='hot pink',fg='grey22').grid(row=4,column=8,padx=5,pady=10)
id_entry=Entry(frame1)
id_entry.grid(row=4,column=1,padx=5,pady=10)
name_entry=Entry(frame1)
name_entry.grid(row=4,column=3,padx=5,pady=10)
address_entry=Entry(frame1)
address_entry.grid(row=4,column=5,padx=5,pady=10)
phone=Entry(frame1)
phone.grid(row=4,column=7,padx=5,pady=10)
email_entry=Entry(frame1)
email_entry.grid(row=4,column=9,padx=5,pady=10)
Button(frame1,text=' Add',font="Times 15 bold",bg='firebrick1',fg='grey22',command=add_op).grid(row=4,column=10,padx=5,pady=10)
Button(frame1,text=' Edit',font="Times 15 bold",bg='firebrick2',fg='grey22',command=edit_op).grid(row=4,column=11,padx=5,pady=10)
Button(frame2,image=buzz,font="Times 15 bold",bg='firebrick2',fg='grey22',command=home).grid(row=4,column=15,padx=5,pady=10)

root.mainloop()
