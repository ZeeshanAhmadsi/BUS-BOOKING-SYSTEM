from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox
root=Tk()
root.title("New route")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
def add_route():
    
    routeid=id_entry.get()
    station=station_entry.get()
    station=station.capitalize()
    
    id_stat=id_stat_entry.get()
    route_data=(routeid,station,id_stat)
    route_data=(routeid,station,id_stat)
    data=(routeid,station)

    if not (routeid and station and id_stat):

        messagebox.showwarning("Warning","All entries should be filled.")
   
        return

    if not (station.isalpha()):
        messagebox.showwarning("Warning","Station Name should be Alphabetical")
        return

    existing_route=bus_booking_system.read_route()
    
    for i in existing_route:
        if data ==i[:2]:
            messagebox.showerror("Error","Route Details already exists")
            return 
    
    bus_booking_system.add_route(route_data)

    
    messagebox.showinfo("successful",'''Route added successfully : Thank you''')

    show_details=Label(frame3,text=f"{routeid}  {station}  {id_stat} ")
    show_details.grid(row=4,column=5)

    id_entry.delete(0,END)
    station_entry.delete(0,END)
    id_stat_entry.delete(0,END)

def delete_route():
    
    

    routeid=id_entry.get()
    station=station_entry.get()
    station=station.capitalize()
    id_stat=id_stat_entry.get()
    route_data=(routeid,station,id_stat)

    if not (routeid and station and id_stat):

        messagebox.showwarning("Warning","All entries should be filled.")
   
        return

    existing_route=bus_booking_system.read_route()
    check=None
    for i in existing_route:
        if route_data ==i:
           
           check=i
    if check==None:
        messagebox.showerror("Error","route details does not exist.")
        return
    
    bus_booking_system.delete_route(routeid,station)
     
    messagebox.showinfo("successful",'''Route deleted  successfully : Thank you''')

    show_details=Label(frame3,text=f"{routeid}  {station}  {id_stat} ")
    show_details.grid(row=4,column=5)

    id_entry.delete(0,END)
    station_entry.delete(0,END)
    id_stat_entry.delete(0,END)
    



def home():
    subprocess.run(["python","homepage.py"])
    root.destroy()

root.state("zoomed")
root.configure(bg='peach puff')
frame=Frame(root,bd=0,bg='peach puff')
frame.grid(row=1,column=1,columnspan=6,padx=180)
bus=PhotoImage(file='star.png')
buzz=PhotoImage(file='home.png')
Label(frame,image=bus).grid(row=1,column=0,padx=180)
Label(frame,text=' Online Bus Booking System',font="Times 28 bold",bg='chartreuse',fg='grey22').grid(row=2,column=0,padx=180,pady=10)
Label(frame,text=' Add Bus Route Details',font="Times 22 bold",bg='pale green',fg='grey22').grid(row=3,column=0,padx=180,pady=10)
frame1=Frame(root,bd=0,bg='peach puff')
frame1.grid(row=2,column=1,columnspan=6,padx=150)
Label(frame1,text='Route id',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=0,padx=2,pady=10)
Label(frame1,text='Starting Station',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=2,padx=2,pady=10)
Label(frame1,text='Station id',bg='cadetBlue1',font='Times 10',fg='gray22').grid(row=2,column=6,padx=2,pady=10)

id_entry=Entry(frame1)
id_entry.grid(row=2,column=1,padx=5,pady=10)
station_entry=Entry(frame1)
station_entry.grid(row=2,column=5,padx=2,pady=10)
id_stat_entry=Entry(frame1)
id_stat_entry.grid(row=2,column=7,padx=2,pady=10)

frame2=Frame(root,bd=0,bg='peach puff')
frame2.grid(row=3,column=1,columnspan=6,padx=180)
frame3=Frame(root,bd=0,bg='peach puff')
frame3.grid(row=4,column=1,columnspan=6,padx=180)
Button(frame2,text="Add Route",command=add_route,bg='aquamarine',font='Times 10',fg='gray22').grid(row=2,column=3,padx=20,pady=10)
Button(frame2,text="Delete Route",command=delete_route,bg='violet red',font='Times 10',fg='gray22').grid(row=2,column=4,padx=20,pady=10)
Button(frame2,image=buzz,bg='aquamarine',command=home).grid(row=2,column=5,padx=20,pady=10)
root.mainloop()
