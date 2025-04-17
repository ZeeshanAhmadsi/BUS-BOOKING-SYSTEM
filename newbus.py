from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox
root=Tk()
root.state("zoomed")
root.title("New Bus")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
root.configure(bg='peach puff')

def add_bus():
    busid=id_entry.get()
    Bustype=click.get()
    capacity=capacity_entry.get()
    fare=fare_entry.get()
    opid=opid_entry.get()
    routeid=routeid_entry.get()

    existing_bus=bus_booking_system.read_bus()
    
    for i in existing_bus:
        if busid ==i[0]:
            messagebox.showerror("Error"," Bus_id  already exists")
            return 


    if not (busid and Bustype and capacity and fare and opid and routeid ):
        messagebox.showwarning("Warning","All entries should be filled.")
        return
    
    if(Bustype=="Bus Type"):
         messagebox.showwarning("Warning","Bus Type should be selected .")
         return

    
    if capacity.isalpha():
         messagebox.showwarning("Warning","Capacity  should be Integer.")
         return

    if int(capacity)<=10 :
         messagebox.showwarning("Warning","Capacity should be greater than 10.")
         return

    if int(capacity)>=60 :
         messagebox.showwarning("Warning","Capacity should be less than 60.")
         return
    
    if fare.isalpha():
         messagebox.showwarning("Warning","fare  should be Integer.")
         return

    if int(fare)<=0 :
         messagebox.showwarning("Warning","fare should be positive integer ")
         return
    
    bus_data=(busid,Bustype,capacity,fare,opid,routeid)
    if bus_booking_system.add_bus(bus_data)==None:
        return
    else:

        bus_booking_system.add_bus(bus_data)
    
        messagebox.showinfo("successful",'''Bus added successfully : Thank you''')

   
        show_details=Label(frame3,text=f"{busid}  {Bustype}  {capacity}  {fare}  {opid}  {routeid}")
        show_details.grid(row=4,column=5)

        id_entry.delete(0,END)
        click.set("Bus Type")
        capacity_entry.delete(0,END)
        fare_entry.delete(0,END)
        opid_entry.delete(0,END)
        routeid_entry.delete(0,END)




def edit_bus():
    busid=id_entry.get()
    Bustype=click.get()
    capacity=capacity_entry.get()
    fare=fare_entry.get()
    opid=opid_entry.get()
    routeid=routeid_entry.get()

    existing_bus=bus_booking_system.read_bus()
    bus_edit=None
    
    for bus in existing_bus:
        if bus[0]==busid:
            bus_edit=bus
            break

    if bus_edit is None:
        messagebox.showerror("Error",f" Bus with Id {busid} not found.")
        return 

    if not (busid and Bustype and capacity and fare and opid and routeid ):
        messagebox.showwarning("Warning","All entries should be filled.")
        return

    
    if(Bustype=="Bus Type"):
         messagebox.showwarning("Warning","Bus Type should be selected .")
         return

    
    if capacity.isalpha():
         messagebox.showwarning("Warning","Capacity  should be Integer.")
         return

    if int(capacity)<10 :
         messagebox.showwarning("Warning","Capacity should be greater than 10.")
         return

    if int(capacity)>60 :
         messagebox.showwarning("Warning","Capacity should be less than 60.")
         return
    
    if fare.isalpha():
         messagebox.showwarning("Warning","fare  should be Integer.")
         return

    if int(fare)<0 :
         messagebox.showwarning("Warning","fare should be positive integer ")
         return
    
    

    response=messagebox.askyesno("message","Are you Sure You want to edit ?")

    if response==1:
            bus_data=(busid,Bustype,capacity,fare,opid,routeid)
  
            bus_booking_system.edit_bus(busid,bus_data)

        
            messagebox.showinfo("successful",'''Bus Edited successfully : Thank you''')
            show_details=Label(frame3,text=f"{busid}  {Bustype}  {capacity}  {fare}  {opid}  {routeid}")
            show_details.grid(row=4,column=5)

            id_entry.delete(0,END)
            click.set("Bus Type")
            capacity_entry.delete(0,END)
            fare_entry.delete(0,END)
            opid_entry.delete(0,END)
            routeid_entry.delete(0,END)

    else:
        return 
    

    


def home():
    subprocess.run(["python","homepage.py"])
    root.destroy()

    
    
frame=Frame(root,bd=0,bg='peach puff')
frame.grid(row=1,column=0,columnspan=6,padx=240)
bus=PhotoImage(file='star.png')
buzz=PhotoImage(file='home.png')
Label(frame,image=bus).grid(row=1,column=0,padx=240)
Label(frame,text=' Online Bus Booking System',font="Times 28 bold",bg='chartreuse',fg='grey22').grid(row=2,column=0,padx=240,pady=10)
Label(frame,text=' Add Bus Details',font="Times 22 bold",bg='pale green',fg='grey22').grid(row=3,column=0,padx=240,pady=10)
frame1=Frame(root,bd=0,bg='peach puff')
frame1.grid(row=2,column=1,columnspan=6,padx=120)
Label(frame1,text='Bus id',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=0,padx=2,pady=10)
Label(frame1,text='Bus Type',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=2,padx=2,pady=10)
Label(frame1,text='Capacity',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=5,padx=2,pady=10)
Label(frame1,text='Fare Rs',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=7,padx=2,pady=10)
Label(frame1,text='Operator id',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=9,padx=2,pady=10)
Label(frame1,text='Route id',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=11,padx=2,pady=10)
id_entry=Entry(frame1)
id_entry.grid(row=2,column=1,padx=5,pady=10)
click=StringVar()
click.set("Bus Type")
busoptions=(" AC 2x2","AC 3x2","Non Ac 2x2","Non Ac 3x2"," Ac-Sleeper 2x1"," Non-Ac Sleeper 2x1")
OptionMenu(frame1,click,*busoptions).grid(row=2,column=4,columnspan=1,padx=5,pady=10)
capacity_entry=Entry(frame1)
capacity_entry.grid(row=2,column=6,padx=2,pady=10)
fare_entry=Entry(frame1)
fare_entry.grid(row=2,column=8,padx=2,pady=10)
opid_entry=Entry(frame1)
opid_entry.grid(row=2,column=10,padx=2,pady=10)
routeid_entry=Entry(frame1)
routeid_entry.grid(row=2,column=12,padx=2,pady=10)

frame2=Frame(root,bd=0,bg='peach puff')
frame2.grid(row=3,column=0,columnspan=6,padx=100)
frame3=Frame(root,bd=0,bg='peach puff')
frame3.grid(row=4,column=0,columnspan=6,padx=100)
Button(frame2,text="Add Bus",command=add_bus,bg='aquamarine',font='Times 10',fg='gray22').grid(row=2,column=3,padx=10,pady=10)
Button(frame2,text="Edit Bus",command=edit_bus,bg='violet red',font='Times 10',fg='gray22').grid(row=2,column=4,padx=10,pady=10)
Button(frame2,image=buzz,bg='aquamarine',command=home).grid(row=2,column=5,padx=10,pady=10)
root.mainloop()
