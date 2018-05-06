from Tkinter import *
import tkMessageBox
from ttk import *
import sqlite3
con=sqlite3.Connection('hrdb')
rootp=Tk()
Label(rootp,text="Welcome to Jet Airliance",font="Bold 20").pack()
def fun8():
    rootp.destroy()
    root2=Tk()
    root2.title("Welcome,Customer To our Cancellation System")
    Label(root2,text="Enter your last 4 digit of Adhar card ").grid(row=0,column=0)
    e1=Entry(root2)
    e1.grid(row=0,column=1)
    Label(root2,text="Choose your class").grid(row=1,column=0)
    w2=Combobox(root2,height=5,width=15,values=["common","economic"])
    w2.grid(row=1,column=1)
    Label(root2,text="select boarding").grid(row=2,column=0)
    w3=Combobox(root2,height=5,width=15,values=["chennai","Mumbai","Delhi","Calcutta"])
    w3.grid(row=2,column=1)
    def fun2():
        d=e1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        x=str(d)
        y=str(c)
        con.commit()
        if d=='' or b=='' or c=='':
             tkMessageBox.showerror("Oops","You can't Enter the leave any field empty")
        else:     
             if b=="economic":
                cur.execute("delete from economic2 where adno=(?) and boarding=(?)",(d,b,))
                cur.execute("select * from economic2")
                tkMessageBox.showinfo("your reservation is cancelled",cur.fetchall())
             else:
                    cur.execute("delete from common2 where adno=x and boarding=y")
                    cur.execute("select * from common2")
        
                    
            
    Bc=Button(root2,text="Cancel Reservation",command=fun2).grid(row=4,column=0)
    root2.mainloop()
def fun9():
    rootp.destroy()
    root4=Tk()
    root4.title("Welcome,Search flights")
    Label(root4,text="Enter Boarding").grid(row=0,column=0)
    w1=Combobox(root4,height=5,width=15,values=["chennai","Mumbai","Delhi","Calcutta"])
    w1.grid(row=0,column=1)
    Label(root4,text="select destination").grid(row=1,column=0)
    w2=Combobox(root4,height=5,width=15,values=["chennai","Mumbai","Delhi","Calcutta"])
    w2.grid(row=1,column=1)
    Label(root4,text="Choose day of travel").grid(row=2,column=0)
    w3=Combobox(root4,text="choose day",height=5,width=15,values=["sunday","monday","tuesday","wensday","thursday","friday","saturday"])
    w3.grid(row=2,column=1)
    def fun10():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        if a=='' or b=='' or c=='':
            tkMessageBox.showerror("Error","Cant leave any field empty")
           
                
        else:
             if a!=b:
                 #cur.execute("create table eco(boarding char(20),destination char(20),day char(20),time number,class char(10),fare number)")
                 cur.execute("insert into eco values('Chennai','Mumbai','Sunday',1.00,'Economic',2500)")
                 cur.execute("insert into eco values('Chennai','Delhi','Monday',1.00,'Common',4000)")
                 cur.execute("insert into eco values('Chennai','Calcutta','Tuesday',1.00,'Economic',5500)")
                 cur.execute("insert into eco values('Mumbai','Chennai','Wensday',1.00,'Economic',3500)")
                 cur.execute("insert into eco values('Mumbai','Chennai','Wensday',7.00,'Common',2500)")
                 cur.execute("select * from eco where boarding=? and destination=? and day=?",(a,b,c,))
                 con.commit()
                 e=cur.fetchall()
                 tkMessageBox.showinfo("flights availble are",e)
             else:
                tkMessageBox.showerror("Oops","boarding and destination can't me same")
        
    Bs=Button(root4,text="search",command=fun10).grid(row=3,column=0)
    root4.mainloop()
def fun5():
    rootp.destroy()
    root=Tk()
    root.title('Flight search And booking')
    Label(root,text="Enter Boarding").grid(row=1,column=0)
#e1=Entry(root,width=20,bd=4,justify="right")
#e1.grid(row=1,column=1)
    w=Combobox(root,height=5,width=15,values=["Delhi","Bombay","Chennai","Calcutta"])
    w.grid(row=1,column=1)
    Label(root,text='Enter Destination').grid(row=2,column=0)
#e2=Entry(root,width=20,justify='right')
#e2.grid(row=2,column=1)
    w1=Combobox(root,height=5,width=15,values=["Delhi","Bombay","Chennai","Calcutta"])
    w1.grid(row=2,column=1)
#e3=Entry(root,width=20,justify='right')
#e3.grid(row=3,column=1)
    Label(root,text='Enter your last 4 digit of aadhar card').grid(row=3,column=0)
    e=Entry(root,width=20)
    e.grid(row=3,column=1)
    w2=Combobox(root,text='common',height=5,width=15,values=["common","economic"])
    w2.grid(row=4,column=1)
    Label(root,text='Choose Class').grid(row=4,column=0)
    Label(root,text="Choose day of travel").grid(row=5,column=0)
    w3=Combobox(root,text="choose day",height=5,width=15,values=["sunday","monday","tuesday","wensday","thursday","friday","saturday"])
    w3.grid(row=5,column=1)
    Label(root,text="choose time of your flight").grid(row=6,column=0)
    w4=Combobox(root,height=5,width=15,values=["1:00 AM","7:00 AM","1:00 PM","4:00 PM","9:00 PM"])
    w4.grid(row=6,column=1)
    def fun():
        a=w.get()
        b=w1.get()
        c=e.get()
        d=w2.get()
        f=w3.get()
        g=w4.get()
        x=(a,b,c,f,g)
        cur=con.cursor()
        
        if a=='' or b=='' or c=='' or d=='' or f=='' or g=='':
            tkMessageBox.showerror("OOPS","you can't leave any field empty")
        else :
            if d=='economic':
                
                if a!=b:
                    #cur.execute("create table economic2(boarding char(20),destination char(20),adno number,day char,time number)")
                    cur.execute("insert into economic2 values(?,?,?,?,?)",x)
                    tkMessageBox.showinfo("congrats","your seat has been reserved")
                    con.commit()
                    cur.execute("select * from economic2 where adno=(?)",(c,))
                    tkMessageBox.showinfo("records",cur.fetchall())
                else:
                    tkMessageBox.showerror("Error","you can't choose same city")
            if d=='common':
                cur.execute("create table common2(boarding char(20),destination char(20),adno number,day char,time number)")
                if a!=b:
                    cur.execute("insert into common2 values(?,?,?,?,?)",x)
                    tkMessageBox.showinfo("congrats","your seat has been reserved")
                    con.commit()
                    cur.execute("select * from common2 where adno=(?)",(c,))
                    tkMessageBox.showinfo("records",cur.fetchall())
                else :
                    tkMessageBox.showerror("Error","you can't choose same city")
    Bi=Button(root,text="Insert",command=fun).grid(row=7,column=1)
#Bo=Button(root,text="See Flights",command=dis).grid(row=7,column=1)
#Bf=Button(root,text='Set fair range',command=fun1).grid(row=7,column=2)
    root.mainloop()
    
B1=Button(rootp,text="Cancel Booking",command=fun8).pack()
B2=Button(rootp,text="Search Flight",command=fun9).pack()
B3=Button(rootp,text="Book Flight",command=fun5).pack()
#B2=Button(rootp,text="Cancel Booking",height=4,width=35,font="Bold",bg="gray").pack()
#B3=Button(rootp,text="See flights",height=4,width=35,font="Bold",bg="gray").pack()


rootp.mainloop()
    
