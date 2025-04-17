from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox
root=Tk()
root.title("checkbookedseat")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
def homepage():
    subprocess.run(["python","homepage.py"])
    root.destroy()




def checkticket():
    mobile = mobile_no.get()

    if not mobile:
        messagebox.showwarning("Warning", "All entries should be filled.")
        return
    if (len(mobile) != 10) or not mobile.isdigit():
        messagebox.showerror("Error", "Mobile No. should be of ten digit Integer")
        return

    bookings = bus_booking_system.show_tickets_from_mobile(mobile)

    if not bookings:
        response = messagebox.askyesno("No Records Found", "Do you want to Book a Seat?")
        if response == 1:
            subprocess.run(["python", "bookbus.py"])
        return
    k=0
    l=0
    for i, booking in enumerate(bookings):
        new_frame = LabelFrame(frame3, padx=10, pady=10, borderwidth=3, relief="sunken")
        new_frame.grid(row=k,column=l,padx=10, pady=10)

        Label(new_frame, text=f'Passenger:  {booking[5]}', font=('Poppins', 10, 'bold')).grid(row=0, column=0, padx=2,
                                                                                                pady=2)
        Label(new_frame, text=f'Gender:  {booking[6]}', font=('Poppins', 10, 'bold')).grid(row=0, column=1, padx=2,
                                                                                             pady=2)
        Label(new_frame, text=f'Total Seats :  {booking[7]}', font=('Poppins', 10, 'bold')).grid(row=1, column=0, padx=2,
                                                                                                  pady=2)
        Label(new_frame, text=f'Phone No:  {booking[8]}', font=('Poppins', 10, 'bold')).grid(row=1, column=1, padx=2,
                                                                                              pady=2)
        Label(new_frame, text=f'Age:  {booking[9]}', font=('Poppins', 10, 'bold')).grid(row=2, column=0, padx=2,
                                                                                        pady=2)
        Label(new_frame, text=f'Booking Ref.:  {booking[0]}', font=('Poppins', 10, 'bold')).grid(row=2, column=1,
                                                                                                padx=2, pady=2)
        Label(new_frame, text=f'Traveling Date :  {booking[4]}', font=('Poppins', 10, 'bold')).grid(row=3, column=0,
                                                                                                    padx=2, pady=2)
        Label(new_frame, text=f'Booked On:  {booking[3]}', font=('Poppins', 10, 'bold')).grid(row=3, column=1, padx=2,
                                                                                            pady=2)
        Label(new_frame, text=f'Boarding point :  {booking[1]}', font=('Poppins', 10, 'bold')).grid(row=4, column=0,
                                                                                                    padx=2, pady=2)
        Label(new_frame, text=f'Dropping point :  {booking[2]}', font=('Poppins', 10, 'bold')).grid(row=4, column=1,
                                                                                                    padx=2, pady=2)
        bus_fare = bus_booking_system.show_bus_fare(booking[10])
        total_fare = int(bus_fare[0]) * int(booking[7])
        Label(new_frame, text=f'Total_Fare:  Rs {total_fare}', font=('Poppins', 10, 'bold'), fg="blue").grid(row=5,
                                                                                                             column=0,
                                                                                                             padx=2,
                                                                                                             pady=2)
        bus_name = bus_booking_system.show_operator(booking[10])
        Label(new_frame, text=f"Bus Details:  {bus_name[0]}", font=('Poppins', 10, 'bold')).grid(row=5, column=1,
                                                                                                  padx=2, pady=2)
        l+=1


root.state("zoomed")
root.configure(bg='peach puff')
frame=Frame(root,bd=0,bg='peach puff')
frame.grid(row=1,column=0,columnspan=6,padx=240)

bus=PhotoImage(file='star.png')
buzz=PhotoImage(file='home.png')
Label(frame,image=bus).grid(row=1,column=0,padx=240)
Label(frame,text=' Online Bus Booking System',font="Times 28 bold",bg='chartreuse',fg='grey22').grid(row=2,column=0,padx=240)
Label(frame,text=' Check Your Booking',font="Times 22 bold",bg='pale green',fg='grey22').grid(row=3,column=0,padx=240)
frame1=Frame(root,bd=0,bg='peach puff')
frame1.grid(row=2,column=0,columnspan=6,padx=150)
Label(frame1,text='Enter Your Mobile Number',bg='tomato',font='Times 12',fg='gray22').grid(row=2,column=0,padx=2)

mobile_no=Entry(frame1)
mobile_no.grid(row=2,column=1,padx=10,pady=10)

Button(frame1,text="Check Booking",command=checkticket,bg='tomato',fg="grey22").grid(row=2,column=5,padx=20)
frame2=Frame(root,bd=0,bg='peach puff')
frame2.grid(row=3,column=0,columnspan=6,padx=210)
frame3=Frame(root,bd=0,bg='peach puff')
frame3.grid(row=4,column=0,columnspan=6,padx=210)
Button(frame2,image=buzz,bg='aquamarine',command=homepage).grid(row=2,column=6

                                                                )
root.mainloop()
