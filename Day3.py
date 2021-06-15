from tkinter import *
window=Tk()
window.title("REGISTRATION FORM")
window.geometry('500x600')
window.configure(background='#8ecae6')

fname=Label(window,text="FIRST NAME",bg='#8ecae6',border=10 ).grid(row=0,column=0)
fname1=Entry(window).grid(row=0,column=2)


lname=Label(window,text="LAST NAME",bg='#8ecae6',border=10).grid(row=1,column=0)
lname1=Entry(window,).grid(row=1,column=2)

age=Label(window,text="AGE",bg='#8ecae6',border=10).grid(row=2,column=0)
age1=Entry(window).grid(row=2,column=2)

gender=Label(window,text="GENDER",bg='#8ecae6',border=10).grid(row=3,column=0)
Genders=["MALE","FEMALE","OTHERS"]
gen=StringVar()

gen.set("MALE")
gender1=OptionMenu(window,gen,*Genders).grid(row=3,column=2)

qual=Label(window,text="QUALIFICATON",bg='#8ecae6',border=10).grid(row=4,column=0)


dept=Label(window,text="DEPARTMENT",bg='#8ecae6',border=10).grid(row=5,column=0)
dept1=Entry(window).grid(row=5,column=2)

passyear=Label(window,text="PASSING YEAR",bg='#8ecae6',border=10).grid(row=6,column=0)
passyear1=Entry(window).grid(row=6,column=2)

mail=Label(window,text="MAIL ID",bg='#8ecae6',border=10).grid(row=7,column=0)
mail1=Entry(window).grid(row=7,column=2)

number=Label(window,text="NUMBER",bg='#8ecae6',border=10).grid(row=8,column=0)
number1=Entry(window).grid(row=8,column=2)

prolan=Label(window,text="PROGRAMMING LANGUAGES",bg='#8ecae6',border=10).grid(row=9,column=0)
lan=StringVar
Radiobutton(window,text="C",variable=lan,value=1,bg='#8ecae6',border=5).grid(row=9,column=2)
Radiobutton(window,text="C++",variable=lan,value=2,bg='#8ecae6',border=5).grid(row=10,column=2)
Radiobutton(window,text="JAVA",variable=lan,value=3,bg='#8ecae6',border=5).grid(row=11,column=2)
Radiobutton(window,text="PYTHON",variable=lan,value=4,bg='#8ecae6',border=5).grid(row=12,column=2)

location=Label(window,text="LOCATION",bg='#8ecae6',border=10).grid(row=13,column=0)
location1=Entry(window).grid(row=13,column=2)

def myclick(name):
     res = "Welcome to " + txt.get()
     lbl.configure(text=res)
button=Button(window,text="SUBMIT",bg='#8ecae6',border=10,command=lambda :myclick(fname1.get)).grid(row=14,column=2)
window.mainloop()
