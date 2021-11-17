from tkinter import *
import tkinter as ttk
import sqlite3




   
window = Tk()

#create/connect to table
conn=sqlite3.connect('covid.db')
#create cursor
c=conn.cursor()
#create table only once so commented the code
'''
c.execute("""CREATE TABLE covidrec(
         first_name text,
         last_name text,
         phNumber text,
         state text,
         city text,
         age int,
         gender text,
         hospitalName text,
         covidState int
         )
         """)
'''
def submit():
   #create/connect to table
   conn=sqlite3.connect('covid.db')
   #create cursor
   c=conn.cursor()

   c.execute("INSERT INTO covidrec VALUES(:fn,:ln,:pn,:state,:city,:age,:gender,:hospital,:covid)",
        {
        'fn':fnEntry.get(),
        'ln':lnEntery.get(),
        'pn':phEntry.get(),
        'state':stateEntry.get(),
        'city':cityEntry.get(),
        'age':ageEntry.get(),
        'gender':genderEntry.get(),
        'hospital':hospitalNameEntry.get(),
        'covid':covidtest.get()
        }


    )

   #commit changes
   conn.commit()
   #connection close
   conn.close()

   fnEntry.delete(0,END)
   lnEntery.delete(0,END)
   phEntry.delete(0,END)
   stateEntry.delete(0,END)
   cityEntry.delete(0,END)
   ageEntry.delete(0,END)
   genderEntry.delete(0,END)
   hospitalNameEntry.delete(0,END)

def query():
   #create/connect to table
   conn=sqlite3.connect('covid.db')
   #create cursor
   c=conn.cursor()
   #shows records
   c.execute("SELECT *FROM covidrec")
   print(c.fetchall())
   #commit changes
   conn.commit()
   #connection close
   conn.close()


covidtest= ttk.IntVar()


window.title("COVID form")
window.geometry('800x400')
window.configure(background = "white")

#labels
firstName = Label(window ,width=30,text = "First Name").grid(row = 0,column = 0)
lastName = Label(window,width=30 ,text = "Last Name").grid(row = 1,column = 0)
phNumber = Label(window ,width=30,text = "PH Number").grid(row = 2,column = 0)
state=Label(window ,width=30,text = "State").grid(row = 3,column = 0)
city=Label(window ,width=30,text = "city").grid(row = 4,column = 0)
age=Label(window,width=30 ,text = "age").grid(row = 5,column = 0)
gender=Label(window ,width=30,text = "gender").grid(row = 6,column = 0)
hospitalName=Label(window,width=30,text="Hospital Name:").grid(row=7,column=0)
covidState=Label(window,width=30,text="COVID state:").grid(row=8,column=0)

# textboxes
fnEntry = Entry(window,width=30)
fnEntry.grid(row = 0,column = 1)
lnEntery = Entry(window,width=30)
lnEntery.grid(row = 1,column = 1)
phEntry = Entry(window,width=30)
phEntry.grid(row = 2,column = 1)
stateEntry = Entry(window,width=30)
stateEntry.grid(row = 3,column = 1)
cityEntry = Entry(window,width=30)
cityEntry.grid(row = 4,column = 1)
ageEntry = Entry(window,width=30)
ageEntry.grid(row = 5,column = 1)
genderEntry = Entry(window,width=30)
genderEntry.grid(row = 6,column = 1)
hospitalNameEntry=Entry(window,width=30)
hospitalNameEntry.grid(row=7,column=1)

#radio buttons
ttk.Radiobutton(window,width=30, 
              text="positive",
              
              variable=covidtest, 
              value=1).grid(row=8,column=1)
ttk.Radiobutton(window,width=30, 
              text="Negative",
              
              variable=covidtest, 
              value=0).grid(row=9,column=1)

  

#submit button
btn = ttk.Button(window ,text="Submit",command=submit).grid(row=12,column=0)
query_btn=ttk.Button(window,text="show records",command=query).grid(row=13,column=0)
#commit changes
conn.commit()

#connection close
conn.close()

window.mainloop()




#created_and_changes_by_someshwarmirge
