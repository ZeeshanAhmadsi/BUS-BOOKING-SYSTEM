from tkinter import*
import subprocess
import bus_booking_system
from tkinter import messagebox
from datetime import datetime
import random
root=Tk()
root.title("bookbus")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
current_date=datetime.now().strftime("%d/%m/%Y")
root.configure(bg='peach puff')
def generate_booking_reference():
    while True:
        reference_number = random.randint(1, 100)  
        existing_bookings=bus_booking_system.read_booking()
        booking_edit=None
        for op in existing_bookings:
            if op[0]==reference_number:
                booking_edit=op[0]
                break
        if reference_number != booking_edit:
            return reference_number
       

def book_bus():
     if(selected_bus.get()=="None"):

        
        messagebox.showerror("error","bus is not selected ")
        return
     else:
        print("Zeeshan")



     Label(frame3, text="Fill Passenger details to book the Bus ticket", fg="red", relief="ridge", bg="cyan3",font=('poppins 15 bold')).grid(row=0, column=1, padx=10, pady=20, columnspan=10)

    
     Label(frame3, text="Full Name : ", font=('Helvetica 10 bold')).grid(row=3, column=0)
     global name_entry
     name_entry = Entry(frame3)
     name_entry.grid(row=3, column=1)

    
     Label(frame3, text="Gender : ", font=('Helvetica 10 bold')).grid(row=3, column=2)
     gender_options = ["Male", "Female", "Other"]
     global click
     click = StringVar()
     click.set("Select")
     OptionMenu(frame3, click, *gender_options).grid(row=3, column=3)


    
     Label(frame3, text="Total Seats: ", font=('Helvetica 10 bold')).grid(row=3, column=4)
     global seat_entry
     seat_entry = Entry(frame3)
     seat_entry.grid(row=3, column=5)


    
     Label(frame3, text="Mobile no. : ", font=('Helvetica 10 bold')).grid(row=3, column=6)
     global mobile_entry
     mobile_entry = Entry(frame3)
     mobile_entry.grid(row=3, column=7)

    
     Label(frame3, text="Age : ", font=('Helvetica 10 bold')).grid(row=3, column=8)
     global age_entry
     age_entry = Entry(frame3)
     age_entry.grid(row=3, column=9, padx=10)


     Button(frame3, text="Book Seat", fg="red", bg="cyan3", font=('Helvetica 10 bold'),command=passenger_data).grid(row=3, column=10)



def passenger_data():
    
    name = name_entry.get()
    gender = click.get()
    global total_seat
    total_seat = seat_entry.get()
    mobile_no = mobile_entry.get()
    age = age_entry.get()
    bus_id = selected_bus.get()
    
    
    if (not ( total_seat and mobile_no and age)):
            messagebox.showwarning("Warning", "All entries should be filled.")
            return
    if(name.isdigit()):
        messagebox.showwarning("Warning", " Name should  be Alphabatical .")
        return
        
    if(click.get()=="Select"):
        messagebox.showwarning("Warning", " Gender Should Be Selected .")
        return
        
    
    if not ((len(mobile_no)==10)and mobile_no.isdigit()) :
                messagebox.showerror("Error","Mobile No. should be Ten digit Integer. ")
                return
    if  (age.isalpha()) :
        messagebox.showerror("error"," Age Should be Integer ")
        return
            
    if int(age)>110 :
        messagebox.showerror("error"," Age Should be less than 110")
        return

    if int(age)<18 :
        messagebox.showerror("error"," Age Should be aleast 18")
        return
    
    if not(total_seat.isdigit()) :
        messagebox.showerror("error"," seat should be Integer")
        return 
    if(int(total_seat)>7) :
        messagebox.showerror("error"," max seat 6 seat can be booked")
        return
    if(int(total_seat)<=0) :
        messagebox.showerror("error"," min seat 1 seat can be booked")
        return
        

    
    bus_fare=bus_booking_system.show_fare(bus_id)            
    total_fare=(int(total_seat)*int(bus_fare[0]))

   

    data=generate_booking_reference(), start_station, end_station, current_date, Journey_date,name, gender, total_seat, mobile_no, age, bus_id

    response=messagebox.askyesno("Seat Confirm",f'''Total amount to be paid is {total_fare}
                                                     Do you want to Book? ''')
    if response==1:
            messagebox.showinfo("congrats", "your bus booked successfully")
            
            bus_booking_system.add_booking_details(data)
            
            bus_booking_system.edit_avail(bus_id,total_seat,Journey_date)
            root.destroy()
            subprocess.run(["python", "show_ticket.py"])
                        
    else:

        return
                 

   
   

def show_bus():

    global start_station
    global end_station
    global Journey_date

    start_station=start.get()
    end_station=finish.get()
    Journey_date=date.get()
    

    if not (start_station and end_station and Journey_date ):
        messagebox.showwarning("Warning","All entries should be filled.")
        return
    try:
        
        datetime.strptime(Journey_date, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd/mm/yyyy.")
        return
    

    if start_station.isalpha() and end_station.isalpha():
        
        if not Journey_date=="":
           

            start_station=start_station.capitalize()
            end_station=end_station.capitalize()
           
            route = bus_booking_system.show_route(start_station,end_station)

            
            if len(route)==0:
                messagebox.showerror("No route found","No route found")
                return
            else:
               

                buses=bus_booking_system.show_bus(route[0])
                
                
            if(len(buses)==0):
                messagebox.showerror("No Bus found","No Bus found")
                return

            else:
                
                buses_running=[]
                for i in buses:
                    if(i in bus_booking_system.show_run(i[0],Journey_date)):
                        buses_running.append(i[0])
                if(len(buses_running)==0):
                        messagebox.showerror("NOT RUNNING",f'BUS is not running at {Journey_date} , Change Date ')
                        return
    
    Label(frame2,text="Select Bus",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=1,padx=10)
    
    Label(frame2,text="Operator",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=2,padx=10)
    
    Label(frame2,text="Bus Type",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=3,padx=10)

    Label(frame2,text="Available/Capacity",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=4,padx=10)

    Label(frame2,text="Fare",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=5,padx=10)
    

    display_buses(buses_running)
    
    start.delete(0,END)
    finish.delete(0,END)
    date.delete(0,END)
    


selected_bus = StringVar()
selected_bus.set("None")
def display_buses(buses_running):
    k = 6
    l = 1

    def on_radio_click(bus_id):
        selected_bus.set(bus_id)
        

    for i in range(len(buses_running)):
        bus_id = buses_running[i]  # Assuming buses_running contains unique bus identifiers
        Radiobutton(frame2, text=f'Bus {i + 1}', bg="light blue", font=('Helvetica 10 bold'),
                    relief="ridge", variable=selected_bus, value=bus_id, command=lambda bus_id=bus_id: on_radio_click(bus_id)).grid(row=k,column=l,pady=10,padx=10)
        operator_name = bus_booking_system.show_operator(bus_id)
        l = l + 1
        Label(frame2, text=operator_name[0], fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l, padx=10)
        bus_type = bus_booking_system.show_bus_type(bus_id)
        l = l + 1
        Label(frame2, text=bus_type[0], fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l, padx=10)
        available = bus_booking_system.show_avail(bus_id,Journey_date)
        cap = bus_booking_system.show_cap(bus_id)
        l = l + 1
        Label(frame2, text=f'{available}/{cap[0]}', fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l,
                                                                                                       padx=10)
        l = l + 1
        fare = bus_booking_system.show_fare(bus_id)
        Label(frame2, text=fare[0], fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l, padx=10)
        k = k + 1
        l = 1
    

    Button(frame2, text="Proceed to Book", bg="red", font=('Helvetica 10 bold'), command=book_bus).grid(row=k-1, column=7)


def homepage():
    subprocess.run(["python","homepage.py"])




frame=Frame(root,bd=0,bg='peach puff')
frame.grid(row=1,column=1,columnspan=8,padx=16)
frame2=Frame(root,bd=0,bg='peach puff')
frame2.grid(row=2,column=1,columnspan=8,padx=16)
frame3=Frame(root,bd=0,bg='peach puff')
frame3.grid(row=3,column=1,columnspan=8,padx=16)

root.state('zoomed')
bus=PhotoImage(file='star.png')
buzz=PhotoImage(file='home.png')
Label(frame,image=bus).grid(row=1,column=2,padx=490)
Label(frame,text=' Online Bus Booking Systems',font='Times 28 bold',bg='chartreuse',fg='grey22').grid(row=2,column=2,padx=490)
Label(frame,text=' Enter Journey Details',font='Times 28 bold',bg='indianred1',fg='grey22').grid(row=3,column=2,padx=100)
Label(frame2,text=' To',font='Times 17',bg='light cyan',fg='grey22').grid(row=2,column=1)
Label(frame2,text=' From',font='Times 17',bg='light cyan',fg='grey22').grid(row=2,column=3,padx=10)
Label(frame2,text=' Journey Date(DD/MM/YYYY)',font='Times 17',bg='light cyan',fg='grey22').grid(row=2,padx=10,column=5)

start=Entry(frame2,bd=3)
start.grid(row=2,column=2,padx=10)
finish=Entry(frame2,bd=3)
finish.grid(row=2,column=4,padx=10)
date=Entry(frame2,bd=3)
date.grid(row=2,column=6,padx=10)

Button(frame2,text=' Show Buses',font='Times 15',bg='medium orchid',fg='grey22',command=show_bus).grid(row=2,column=7,padx=10)
Button(frame2,image=buzz,font='Times 23',bg='lightgoldenrod1',fg='grey22',command=homepage).grid(row=2,column=8,padx=10)
root.mainloop()


