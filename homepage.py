from tkinter import *
import subprocess
root=Tk()
root.state("zoomed")
root.title("homepage")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
root.configure(bg='peach puff')
bus=PhotoImage(file="star.png")
Label(root,image=bus).grid(row=1,column=2,padx=100)
Label(root,text=' Online Bus Booking System',font = 'Times 28 bold',bg='chartreuse',fg='gray22').grid(row=2,column=2,padx=100,pady=3)
def bookbus():
    subprocess.run(["python","bookbus.py"])
    root.destroy()
 
    
def checkbus():
    subprocess.run(["python","checkbookseat.py"])
    root.destroy()
   

def admin():
    subprocess.run(["python","admin_use.py"])
    root.destroy()
    
   
    

Button(root,text=' Seat Booking',font='Times 20 bold',relief="ridge",bg='firebrick1',fg='gray9',command=bookbus).grid(row=8,column=1,padx=100,pady=80)
Button(root,text=' Check Booked Seats',font='Times 20 bold',relief="ridge",bg='magenta2',fg='gray9',command=checkbus).grid(row=8,column=2,padx=95,pady=80)
Button(root,text=' Add Bus Details',font='Times 20 bold',relief="ridge",bg='seagreen1',fg='gray9',command=admin).grid(row=8,column=3,padx=75,pady=80)

Label(root,text=' For Admins Only',font='Times 20 bold',fg='salmon1').grid(row=9,column=3,padx=75,pady=5)
root.mainloop()
