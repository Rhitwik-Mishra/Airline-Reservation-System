# Importing required modules
from tkinter import*
import mysql.connector
import tkinter.font as font
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


# Taking sql's password as input
passw=input("Enter your sql's password")
#passw="coding"


def airline():
       # Create GUI
       root =tk.Toplevel()
       root.title('SSDEC')
       w = 1200
       h = 650
       sw = root.winfo_screenwidth()
       sh = root.winfo_screenheight()
       x = (sw - w) / 2
       y = (sh - h) / 2 - 40
       root.geometry( '%dx%d+%d+%d' % (w, h, x, y))
       #root.config(bg="#6FAFE7")
       photo = tk.PhotoImage(file = "plane.png")
       root.iconphoto(False,photo)
       img = ImageTk.PhotoImage(file="aeroplane.png")
       label = Label(root,image=img)
       label.place(x=0, y=0)


       # Create fonts
       
       fnt1 = ("Italic", 45, "bold")
       fnt2 = ("Italic", 25, "bold")
       fnt3 = ("Italic", 20, "bold")
       fnt4 = ("Italic", 18, "bold")
       fnt5 = ("Italic", 14, "bold")
       fnt6 = ("Italic", 10, "bold")
       
       # Create String Var
       name = StringVar()
       address = StringVar()
       mobile = StringVar()
       date_fly = StringVar()
       time_fly = StringVar()
       from1 = StringVar()
       destination = StringVar()
       passeneger = StringVar()
       price = StringVar()



       # Create DataBase
       def creat_database():
              db = mysql.connector.connect(
                user='root',
                passwd=passw,
                host='localhost'

              )
              cursor = db.cursor()
              cursor.execute('CREATE DATABASE IF NOT EXISTS air_ticket28')
              cursor.close()
              db.close()


       creat_database()

       # Create Table
       def creat_table():
              db = mysql.connector.connect(
                  user='root',
                  passwd=passw,
                  host='localhost',
                  database='air_ticket28'
       )    
              cursor = db.cursor()
              cursor.execute('CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255),address VARCHAR(255),mobile VARCHAR(255),from1 VARCHAR(255),destination VARCHAR(255),date_fly VARCHAR(255),time_fly VARCHAR(255),price VARCHAR(255))')
              db.commit()
              cursor.close()
              db.close()
       creat_table()


       # Create function to check the field it is empty or not,if not empty start to add the information in the table in database
       def get_info_new_frame():
           

           if name.get()== '' :
               messagebox.showinfo('Error empty field','Please enter your name')
           elif address.get() == '':
                  messagebox.showinfo('Error empty field','Please enter your address')
           elif mobile.get() == '':
                  messagebox.showinfo('Error empty field','Please enter your mobile number')
           elif date_fly.get() == '':
                  messagebox.showinfo('Error empty field','Please enter date trip')
           elif time_fly.get() not in["9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00"]:
                  messagebox.showinfo('Flight not available','Please enter correct time')
           elif time_fly.get() == '':
                  messagebox.showinfo('Error empty field','Please enter time trip')
           elif e_from.get() == '':
                  messagebox.showinfo('Error empty field','Please enter your Airport')           
           elif e_from.get() in ["Las Vegas","France","Dubai","Washington DC"]:
                  messagebox.showinfo('Flight not available','Flights going out of India avaiable.........Please enter correct boarding')
           elif e_to.get() == '':
                  messagebox.showinfo('Error empty field','Please enter your destination')           
           elif price.get() == '':
                  messagebox.showinfo('Error empty field','Please enter price trip')
           else:           
                  db = mysql.connector.connect(
           user='root',
           passwd=passw,
           host='localhost',
           database='air_ticket28'
)
                  global cursor
                  cursor = db.cursor()
                  sql = "INSERT INTO customers(name, address , mobile , from1 , destination,date_fly,time_fly,price) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                  

                  val = (name.get(), address.get(),mobile.get(),e_from.get(),e_to.get(),date_fly.get(),time_fly.get(),price.get())
                  
                  
                  cursor.execute(sql, val)
                  db.commit()
                  
                  print(cursor.rowcount, 'record(s) inserted')
                  cursor.close()
                  db.close()
                  name.set('')
                  address.set('')
                  mobile.set('')
                  date_fly.set('')
                  time_fly.set('')
                  from1.set('')
                  destination.set('')
                  passeneger.set('')
                  price.set('')
                  messagebox.showinfo('Add Passeneger','Passenger added successfully')
                  
                      


       #Create new GUI    
       def show_data():
           
           window2= tk.Toplevel()
           w = 1200
           h = 500
           sw = window2.winfo_screenwidth()
           sh = window2.winfo_screenheight()
           x = (sw - w) / 2
           y = (sh - h) / 2 - 60
           window2.geometry( '%dx%d+%d+%d' % (w, h, x, y))
           photo = tk.PhotoImage(file = "plane.png")
           window2.iconphoto(False,photo)
           imga = ImageTk.PhotoImage(file="aeroplane.png")
           label = Label(window2,image=imga)
           label.place(x=0, y=0)
           passeneger = StringVar()
           window2.title("SSDEC")

           db = mysql.connector.connect(
           user='root',
           passwd=passw,
           host='localhost',
           database='air_ticket28'
           )
           cursor = db.cursor()  
           cursor.execute('SELECT * FROM customers')
           result = cursor.fetchall()
           #Create treeview
           my_tree = ttk.Treeview(window2)
           my_tree['columns'] = ('Name','Address','Mobile','From','To','Date','Time','Price')

           my_tree.column('#0',width=0,stretch=NO)
           my_tree.column('Name',anchor=W,width=120,minwidth=25)
           my_tree.column('Address',anchor=W,width=120,minwidth=25)
           my_tree.column('Mobile',anchor=W,width=120,minwidth=25)
           my_tree.column('From',anchor=W,width=120,minwidth=25)
           my_tree.column('To',anchor=W,width=120,minwidth=25)
           my_tree.column('Date',anchor=W,width=120,minwidth=25)
           my_tree.column('Time',anchor=W,width=120,minwidth=25)
           my_tree.column('Price',anchor=W,width=120,minwidth=25)

           #my_tree.heading('#0',text='Label',anchor=W)
           my_tree.heading('Name',text='Name',anchor=W)
           my_tree.heading('Address',text='Address',anchor=W)
           my_tree.heading('Mobile',text='Mobile',anchor=W)
           my_tree.heading('From',text='From',anchor=W)
           my_tree.heading('To',text='To',anchor=W)
           my_tree.heading('Date',text='Date',anchor=W)
           my_tree.heading('Time',text='Time',anchor=W)
           my_tree.heading('Price',text='Price',anchor=W)

           cursor.execute('SELECT * FROM customers')
           result = cursor.fetchall()

           #Create function to display all passenger 
           def check_all_passenger():
                  i = 0
                  for row in result:
                         my_tree.insert('',index='end',iid=i,text='Parent',value=(row[1:]))
                         pass
           #print(row)
                         i += 1      
           #Create function to search about one passneger by his name
           def search_single():
                  cursor = db.cursor()
                  i = 0
                  for row in result:
                         i += 1
                         global name_from_user
                         name_from_user = name.get()
                         if name_from_user in row[1:2]:
                                print(row[1:2])
                                my_tree.insert('',index='end',iid=i,text='Parent',value=(row[1:]))
                                name.delete(0, 'end')
           #Create function to delete all passenger from treeview
           def delete_all():
                  for row in my_tree.get_children():
                         my_tree.delete(row)                         
           #Create function modfiy the price ticket by the price and the name
           def modify_price_passenger():
                  cursor = db.cursor()
                  i = 0
                  cursor.execute('SELECT * FROM customers')
                  result = cursor.fetchall()
                  for row in result:
                         i += 1
                         if old_price1 in row[-3]:
                                sql = "UPDATE customers SET date_fly = %s WHERE name = %s"
                                val = (modify.get(), name.get())
                                cursor.execute(sql, val)
                                db.commit()
                         btn5.after(1000,window2.destroy)
                         messagebox.showinfo('Update Date field','Succesfully Updated Date')
                         show_data()
                         
                         delete_all()
                  
           check_all_passenger()             
           my_tree.pack(pady=20)
           #Create function to delete teh passngere from  teh DateBase                 
           def del_system():
                  cursor = db.cursor()
                  i = 0
                  for row in result:
                         i += 1
                         name_del = name.get()
                                                     
                         sql = "DELETE FROM  customers WHERE name = %s"
                         val = (name.get(),)
                         cursor.execute(sql, val)
                         db.commit()
                         print(cursor.rowcount, "record(s) deleted")
           
                  
                  cursor.close()
                  db.close()           
           #Create entry to search about one passenger by name   
           name= Entry(window2,font=fnt5,textvariable=passeneger)
           name.place(x=205,y=300)
           enter_name = name.insert(0,"")
           passeneger_name = name.get()

           #Create entry to input the current price
           old_price = Entry(window2,font=fnt5,textvariable=name)
           old_price.place(x=560,y=300)
           old_price1 = old_price.get()

           #Create entry to input the new price
           modify = Entry(window2,font=fnt5,textvariable=price)
           modify.place(x=930,y=300)
           modify_price = modify.get()
           #Create label  person name 
           label = Label(window2,text='Person Name: ',font=fnt5,bg='#6FAFE7',fg='black')
           label.place(x=50, y=300)
           #Create label  old price 
           label = Label(window2,text='Old Date : ',font=fnt5,bg='#6FAFE7',fg='black')
           label.place(x=450, y=300)
           #Create label  new price 
           label = Label(window2,text='New Date: ',font=fnt5,bg='#6FAFE7',fg='black')
           label.place(x=810, y=300)
           #Create Button to do single search
           btn = Button(window2,text='Search By Name',font=fnt4,bg='#6FAFE7',fg='black',command=search_single)
           btn.place(x=50, y=360)
           #Create Button to display all passenger information
           btn = Button(window2,text='List of Passenger',font=fnt4,bg='#6FAFE7',fg='black',command=check_all_passenger)
           btn.place(x=287, y=360)
           #Create Button to display new price
           btn5 = Button(window2,text='Update Date',font=fnt4,bg='#6FAFE7',fg='black',command=modify_price_passenger)
           btn5.place(x=550, y=360)
           #Create Button to display delete passenger fron DataBase 
           btn = Button(window2,text='Delete from system',font=fnt4,bg='#6FAFE7',fg='black',command= del_system)
           btn.place(x=740, y=360)
           #Create Button to delete all passenger from treeview 
           btn = Button(window2,text='Delete All',font=fnt4,bg='#6FAFE7',fg='black',command=delete_all)
           btn.place(x=1020, y=360)

           but = tk.Label(window2, text = "                    Thank You                    ",bg="#2176C1", fg='white',width = 50, height = 2 ,relief=tk.RAISED,font=fnt3)
           but.place(x = 175,y =420 ) 
           #Destroy second GUI
           window2.mainloop()

           
           


          
       #Create label display the app name
       button2 = tk.Label(root, text = "AIRLINE RESERVATION SYSTEM",bg="#2176C1", fg='white',width = 50, height = 3 ,relief=tk.RAISED,font=fnt2)
       button2.pack(padx = 36,pady =30 )
       
       #Create label name
       label_name = Label(root,text='Name:',font=fnt2,bg='#6FAFE7',fg='black')
       label_name.place(x=100, y=170)
       #Create label address
       label_address = Label(root,text='Address:',font=fnt2,bg='#6FAFE7',fg='black')
       label_address.place(x=100, y=220)
       #Create label mobile
       label_mobile = Label(root,text='Mobile:',font=fnt2,bg='#6FAFE7',fg='black')
       label_mobile.place(x=100, y=270)   
       #Create label date
       label_date = Label(root,text='Date:',font=fnt2,bg='#6FAFE7',fg='black')
       label_date.place(x=100, y=320)
       #Create label time
       label_time = Label(root,text='Time:',font=fnt2,bg='#6FAFE7',fg='black')
       label_time.place(x=100, y=370)
       #Create label from
       label_from = Label(root,text='From:',font=fnt2,bg='#6FAFE7',fg='black')
       label_from.place(x=100, y=420)
       #Create label to
       label_to = Label(root,text='To:',font=fnt2,bg='#6FAFE7',fg='black')
       label_to.place(x=100, y=470)
       #Create label price
       label_to = Label(root,text='Price:',font=fnt2,bg='#6FAFE7',fg='black')
       label_to.place(x=100, y=520)
       #Create entry name
       e_name = Entry(root,font=fnt2,textvariable=name)
       e_name.place(x=260,y=175)
       #Create entry addrress
       e_address = Entry(root,font=fnt2,textvariable=address)
       e_address.place(x=260,y=225)
       #Create entry mobile
       e_mobile = Entry(root,font=fnt2,textvariable=mobile)
       e_mobile.place(x=260,y=275)
       #Create entry date fly
       e_date= Entry(root,font=fnt2,textvariable=date_fly)
       e_date.place(x=260,y=325)
       #Create entry time fly
       e_time= Entry(root,font=fnt2,textvariable=time_fly)
       e_time.place(x=260,y=375)
       #Create entry from where
       e_from = ttk.Combobox(root,font=fnt2,values=["New Delhi","Kolkata","Chennai","Bengaluru","Mumbai","Dubai","Las Vegas","Wahington DC","France"])
       e_from.place(x=260,y=425)
       #Create entry destination
       e_to = ttk.Combobox(root,font=fnt2,values=["New Delhi","Kolkata","Chennai","Bengaluru","Mumbai","Dubai","Las Vegas","Wahington DC","France"])
       e_to.place(x=260,y=475)
       #Create entry price
       e_price = Entry(root,font=fnt2,textvariable=price)
       e_price.place(x=260,y=525)
       
       
       #Create Button to add the information to DataBase
       btn = Button(root,text='Add Passenger',font=fnt4,bg="#2176C1", fg='white',command=get_info_new_frame)
       btn.place(x=260, y=575)
       #Create Button to display the information it is alreay in Database and who you can deal with those information (search,modify,display,delete)
       btn = Button(root,text='Show data',font=fnt4,bg="#2176C1", fg='white',command=show_data)
       btn.place(x=480, y=575)
       def clicker(e):
              select_record()

       def select_record():
               # Clear entry boxes
               e_time.delete(0, END)
               e_from.delete(0, END)
               e_to.delete(0, END)

               # Grab record number
               selected = my_tree.focus()
               # Grab record values
               values = my_tree.item(selected, 'values')

               #temp_label.config(text=values[0])

               # output to entry boxes
               e_time.insert(0, values[0])
               e_from.insert(0, values[1])
               e_to.insert(0, values[2])

       my_tree=ttk.Treeview(root,height=15)       
       my_tree.place(x=660,y=230)
       my_tree['columns']=("Time","Boarding","Destination")

       my_tree.column("#0",width=120,minwidth=25)
       my_tree.column("Time",anchor=W,width=120)
       my_tree.column("Boarding",anchor=W,width=120)
       my_tree.column("Destination",anchor=W,width=120)

       my_tree.heading("#0",text="Label",anchor=W)
       my_tree.heading("Time",text="Time",anchor=W)
       my_tree.heading("Boarding",text="Boarding",anchor=W)
       my_tree.heading("Destination",text="Destination",anchor=W)

       my_tree.tag_configure('oddrow', background="white")
       my_tree.tag_configure('evenrow', background="lightblue")

       my_tree.insert(parent='',index='end',iid=0,text="City1(click+)",values=("--","Mumbai","---"))
       my_tree.insert(parent='0',index='end',iid=1,text="City1",values=("10:00","Mumbai","New Delhi"))
       my_tree.insert(parent='0',index='end',iid=2,text="City1",values=("11:00","Mumbai","Bengaluru"))
       my_tree.insert(parent='0',index='end',iid=3,text="City1",values=("12:00","Mumbai","Chennai"))
       my_tree.insert(parent='0',index='end',iid=4,text="City1",values=("13:00","Mumbai","Dubai"))
       my_tree.insert(parent='0',index='end',iid=5,text="City1",values=("14:00","Mumbai","Las Vegas"))
       my_tree.insert(parent='0',index='end',iid=6,text="City1",values=("15:00","Mumbai","Washington DC"))
       my_tree.insert(parent='0',index='end',iid=7,text="City1",values=("16:00","Mumbai","France"))
       my_tree.insert(parent='',index='end',iid=8,text="City2(click+)",values=("--","Kolkata","---"))
       my_tree.insert(parent='8',index='end',iid=9,text="City2",values=("9:00","Kolkata","New Delhi"))
       my_tree.insert(parent='8',index='end',iid=10,text="City2",values=("10:00","Kolkata","Chennai"))
       my_tree.insert(parent='8',index='end',iid=11,text="City2",values=("11:00","Kolkata","Bengaluru"))
       my_tree.insert(parent='8',index='end',iid=12,text="City2",values=("12:00","Kolkata","Dubai"))
       my_tree.insert(parent='8',index='end',iid=13,text="City2",values=("13:00","Kolkata","Las Vegas"))
       my_tree.insert(parent='8',index='end',iid=14,text="City2",values=("14:00","Kolkata","Washington DC"))
       my_tree.insert(parent='8',index='end',iid=15,text="City2",values=("15:00","Kolkata","France"))
       my_tree.insert(parent='',index='end',iid=16,text="City3(click+)",values=("--","New Delhi","---"))
       my_tree.insert(parent='16',index='end',iid=17,text="City3",values=("10:00","New Delhi","Mumbai"))
       my_tree.insert(parent='16',index='end',iid=18,text="City3",values=("11:00","New Delhi","Bengaluru"))
       my_tree.insert(parent='16',index='end',iid=19,text="City3",values=("12:00","New Delhi","Chennai"))
       my_tree.insert(parent='16',index='end',iid=20,text="City3",values=("13:00","New Delhi","Dubai"))
       my_tree.insert(parent='16',index='end',iid=21,text="City3",values=("14:00","New Delhi","Las Vegas"))
       my_tree.insert(parent='16',index='end',iid=22,text="City3",values=("15:00","New Delhi","Washington DC"))
       my_tree.insert(parent='16',index='end',iid=23,text="City3",values=("16:00","New Delhi","France"))
       my_tree.insert(parent='',index='end',iid=24,text="City4(click+)",values=("--","Bengaluru","---"))
       my_tree.insert(parent='24',index='end',iid=25,text="City4",values=("10:00","Bengaluru","New Delhi"))
       my_tree.insert(parent='24',index='end',iid=26,text="City4",values=("11:00","Bengaluru","Chennai"))
       my_tree.insert(parent='24',index='end',iid=27,text="City4",values=("12:00","Bengaluru","Kolkata"))
       my_tree.insert(parent='24',index='end',iid=28,text="City4",values=("13:00","Bengaluru","Dubai"))
       my_tree.insert(parent='24',index='end',iid=29,text="City4",values=("14:00","Bengaluru","Las Vegas"))
       my_tree.insert(parent='24',index='end',iid=30,text="City4",values=("15:00","Bengaluru","Washington DC"))
       my_tree.insert(parent='24',index='end',iid=31,text="City4",values=("16:00","Bengaluru","France"))
       my_tree.insert(parent='0',index='end',iid=32,text="City1",values=("9:00","Mumbai","Kolkata"))
       my_tree.insert(parent='8',index='end',iid=33,text="City2",values=("16:00","Kolkata","Mumbai"))
       my_tree.insert(parent='16',index='end',iid=34,text="City3",values=("9:00","New Delhi","Kolkata"))
       my_tree.insert(parent='24',index='end',iid=35,text="City4",values=("9:00","Bengaluru","Mumbai"))

       def up():
               rows = my_tree.selection()
               for row in rows:
                       my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

       # Move Row Down
       def down():
               rows = my_tree.selection()
               for row in reversed(rows):
                       my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)



       #Buttons
       move_up = Button(root,text='Move Up',font=fnt4,bg="#2176C1", fg='white',command=up)
       move_up.place(x=720, y=575)

       move_down = Button(root,text='Move Down',font=fnt4,bg="#2176C1", fg='white',command=down)
       move_down.place(x=900, y=575)
       
       my_tree.bind("<ButtonRelease-1>", clicker)

       butto = tk.Label(root, text = "Flights Available",bg="#2176C1", fg='white',width = 27, height = 1 ,relief=tk.RAISED,font=fnt3)
       butto.place(x = 660,y =170 )
       
       root.mainloop()

#.....DEFINING MAIN WINDOW
def main():
    global rootx
    def destro():
        rootx.destroy()
        
    rootx = tk.Toplevel()
    rootx.title("SSDEC")
    rootx.minsize(width = 1200, height = 610)
    rootx.maxsize(width = 1200, height = 610)
    photo = tk.PhotoImage(file = "plane.png")
    rootx.iconphoto(False,photo)
    img = ImageTk.PhotoImage(file="db3.png")
    label = Label(rootx,image=img)
    label.place(x=0, y=0)

    buttonFont = font.Font(family='Helvetica', size=25, weight='bold')
    button2 = tk.Label(rootx, text = "AIRLINE RESERVATION SYSTEM",bg="medium orchid", width = 50, height = 5, relief=tk.RAISED,font=buttonFont)
    button2.pack(padx = 1, pady = 30 )
    buttonFont1 = font.Font(family='Helvetica', size=18, weight='bold')
    button3 = tk.Label(rootx, text = "CREATED AND DESIGNED BY :----\n\nRHITWIK....MISHRA\n\n XII-A\n\nSSDEC ",bg="#6FAFE7",relief="ridge" ,width = 50, height = 7,font=buttonFont1)
    button3.pack(padx = 10, pady = 30 )
    button5 = Button(rootx, text = "NEXT PAGE", width = 30,command=airline)
    button5.place(x = 970, y= 510 )
    B9=Button(rootx,text="QUIT",command=destro,width=30)
    B9.place(x=10,y=510)
        
    rootx.mainloop()
def passwor():
    
    failure_max = 3
    passwords = [('dinesh sir', 'teacher1'), ('omg', 'its5am')]

    def make_entry(passx, caption, width=None, **options):
        tk.Label(passx, text=caption).pack(side=tk.TOP)
        entry = tk.Entry(passx, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        return entry

    def enter(event):
        check_password()

    def check_password(failures=[]):
        #Collect 1's for every failure and quit program in case of failure_max failures
        print(user.get(), password.get())
        if (user.get(), password.get()) in passwords:
            main()
            rootx.quit()
        failures.append(1)
        if sum(failures) >= failure_max:
            rootx.destroy()
            raise SystemExit('Unauthorized login attempt')
        else:
            rootx.title('Try again. Attempt %i/%i' % (sum(failures)+1, failure_max))
        

    rootx = tk.Tk()
    rootx.geometry('300x160')
    rootx.title('Enter your information')
    #frame for window margin
    passx = tk.Frame(rootx, padx=10, pady=10)
    passx.pack(fill=tk.BOTH, expand=True)
    #entrys with not shown text
    user = make_entry(passx, "User name:", 16, show="*")
    password = make_entry(passx, "Password:", 16, show="*")
    #button to attempt to login
    b = tk.Button(passx, borderwidth=4, text="Login", width=10, pady=8, command=check_password)
    b.pack(side=tk.BOTTOM)
    password.bind('<Return>', enter)


    user.focus_set()

    passx.mainloop()
passwor()
