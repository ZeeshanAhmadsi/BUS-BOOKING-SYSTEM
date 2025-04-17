from tkinter import *
import subprocess
root=Tk()
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
def newop():
      subprocess.run(["python","newop.py"])
      root.destroy()
      

    


def newbus():
      subprocess.run(["python","newbus.py"])
      root.destroy()
    
    


def newroute():
      subprocess.run(["python","newroute.py"])
      root.destroy()
      
    
    


def newrun():
      subprocess.run(["python","newrun.py"])
      root.destroy()

root.title("checkbookedseat")    

frame=Frame(root,bd=0,bg='peach puff')
frame.grid(row=1,column=1,columnspan=6,padx=240)
root.state('zoomed')
bus=PhotoImage(file='star.png')
root.configure(bg='peach puff')
Label(frame,image=bus).grid(row=1,column=1,padx=16,pady=16)
Label(frame,text=' Online Bus Booking System',font='Times 28 bold',bg='chartreuse',fg='grey22').grid(row=2,column=1,padx=240,pady=5)
Label(frame,text=' Add New Details To Database',font='Times 22 bold',bg='springgreen2',fg='grey22').grid(row=3,column=1,padx=240,pady=5)

Button(root,text=' New Operator',font='Times 15',bg='violet red',fg='grey22',command=newop,relief="raised").grid(row=4,column=1,padx=80,pady=10)
Button(root,text=' New bus',font='Times 15',bg='sandy brown',fg='grey22',command=newbus,relief="raised").grid(row=4,column=2,padx=80,pady=10)
Button(root,text=' New Route',font='Times 15',bg='tomato',fg='grey22',command=newroute,relief="raised").grid(row=4,column=3,padx=80,pady=10)
Button(root,text=' New Run',font='Times 15',bg='dodgerblue2',fg='grey22',command=newrun,relief="raised").grid(row=4,column=4,padx=80,pady=10)
root.mainloop()
