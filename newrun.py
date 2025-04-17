from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox
from datetime import datetime
root=Tk()
root.title("New run")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
root.state("zoomed")
root.configure(bg='peach puff')
def add_newrun():
    busid = id_entry.get()
    rundate = date_entry.get()
    seat = seat_entry.get()



    existing_bus=bus_booking_system.read_bus()
    busid_edit=None
    for i in existing_bus:
        if busid ==i[0]:
            busid_edit=busid
            break
    if busid_edit==None:
        messagebox.showerror("Warning", "bus id does not exist .")
        return


    if not (busid and rundate and seat):
        messagebox.showwarning("Warning", "All entries should be filled.")
        return

    try:
        # Validate run date format
        datetime.strptime(rundate, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd/mm/yyyy.")
        return

    if seat.isalpha() and int(seat) <0:
        messagebox.showwarning("Warning", "seat should be  positive Integer")
        return

    capacity=bus_booking_system.show_cap(busid)
    
    if int(seat) > int(capacity[0]):
        messagebox.showwarning("Warning", "seat availbilty cannot be greater than capacity of bus")
        return
  

    
    

    

    newrun_data = (busid, rundate, seat)
    bus_booking_system.add_newrun(newrun_data)

    messagebox.showinfo("Successful", "Route added successfully. Thank you.")

    show_details = Label(frame3, text=f"{busid}  {rundate}  {seat}")
    show_details.grid(row=2, column=5)
    id_entry.delete(0, END)
    date_entry.delete(0, END)
    seat_entry.delete(0, END)


def delete_newrun():
    
    busid=(id_entry.get())
    rundate = date_entry.get()
    seat = seat_entry.get()

    
    newrun_data = (busid, rundate, seat)
    existing_bus=bus_booking_system.read_bus()
    busid_edit=None
    for i in existing_bus:
        if busid ==i[0]:
            busid_edit=busid
            break
    if busid_edit==None:
        messagebox.showerror("Warning", "bus id does not exist .")
        return

    if not (busid and rundate and seat):
        messagebox.showwarning("Warning", "All entries should be filled.")
        return

    try:
        # Validate run date format
        datetime.strptime(rundate, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd/mm/yyyy.")
        return

    if seat.isalpha() and int(seat) <0:
        messagebox.showwarning("Warning", "seat should be  positive Integer")
        return


    capacity=bus_booking_system.show_cap(busid)
    
    if int(seat) > int(capacity[0]):
        messagebox.showwarning("Warning", "seat availbilty cannot be greater than capacity of bus")
        return
     
    existing_run=bus_booking_system.read_newrun()
    edit=None
    for i in existing_run:
        if newrun_data ==i[0]:
            edit=i[0]
            break
    if busid_edit==None:
        messagebox.showerror("Error", "record not found.")
        return
    
    bus_booking_system.delete_newrun(busid,rundate)

    messagebox.showinfo("successful",'''Run deleted successfully : Thank you''')

    show_details = Label(frame3, text=f"{busid}  {rundate}  {seat}")
    show_details.grid(row=4,column=5)
    id_entry.delete(0, END)
    date_entry.delete(0, END)
    seat_entry.delete(0, END)






def home():
    subprocess.run(["python","homepage.py"])
    root.destroy()
frame=Frame(root,bd=0,bg='peach puff')
frame.grid(row=1,column=0,columnspan=6,padx=150)
frame2=Frame(root,bd=0,bg='peach puff')
frame2.grid(row=2,column=0,columnspan=6,padx=150)
bus=PhotoImage(file='star.png')
buzz=PhotoImage(file='home.png')
Label(frame,image=bus).grid(row=1,column=0,padx=150)
Label(frame2,text=' Online Bus Booking System',font="Times 28 bold",bg='chartreuse',fg='grey22').grid(row=2,column=0,padx=150,pady=10)
Label(frame2,text=' Add Bus Running Details',font="Times 22 bold",bg='pale green',fg='grey22').grid(row=3,column=0,padx=150,pady=10)
frame3=Frame(root,bd=0,bg='peach puff')
frame3.grid(row=3,column=0,columnspan=6,padx=150)

Label(frame3,text='Bus id',bg='rosy brown',font='Times 10',fg='gray22').grid(row=3,column=0,padx=15,pady=10)
Label(frame3,text='Running Date(DD/MM/YYYY)',bg='rosy brown',font='Times 10',fg='gray22').grid(row=3,column=2,padx=25,pady=10)
Label(frame3,text='Seat Available',bg='rosy brown',font='Times 10',fg='gray22').grid(row=3,column=4,padx=25,pady=10)

id_entry=Entry(frame3)
id_entry.grid(row=3,column=1,padx=5,pady=10)
date_entry=Entry(frame3)
date_entry.grid(row=3,column=3,padx=2,pady=10)
seat_entry=Entry(frame3)
seat_entry.grid(row=3,column=5,padx=2,pady=10)

Button(frame3,text="Add Route",relief="ridge",bg='yellow',command=add_newrun,font='Times 10',fg='gray22').grid(row=3,column=6,padx=20,pady=10)
Button(frame3,text="Delete Route",bg='gold',relief="ridge",font='Times 10',command=delete_newrun,fg='gray22').grid(row=3,column=7,padx=20,pady=10)
Button(frame3,image=buzz,bg='aquamarine',relief="ridge",command=home).grid(row=3,column=8,padx=20,pady=10)
root.mainloop()
