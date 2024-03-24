try:
    from tkinter import*
except:
    from tkinter import*
from tkinter import messagebox
a=[]
def process():
    try:
        idno=int(Entry.get(t1))
        name=Entry.get(t2)
        age=int(Entry.get(t3))
        city=Entry.get(t4)
        qual=Entry.get(t5)
        a=[idno,name,age,city,qual]
        print(a)
        messagebox.showinfo('value',a)
    except:
        messagebox.showinfo("warning",'please enter the integer')
a=Tk()
l1=Label(a,text="student database storage").grid(row=0,column=25)
l2=Label(a,text="idno:").grid(row=1,column=0)
l3=Label(a,text="name:").grid(row=2,column=0)
l4=Label(a,text="age:").grid(row=3,column=0)
l5=Label(a,text="city:").grid(row=4,column=0)
l6=Label(a,text="qual:").grid(row=5,column=0)
t1=Entry(a,bd=2)
t1.grid(row=1,column=1)
t2=Entry(a,bd=2)
t2.grid(row=2,column=1)
t3=Entry(a,bd=2)
t3.grid(row=3,column=1)
t4=Entry(a,bd=2)
t4.grid(row=4,column=1)
t5=Entry(a,bd=2)
t5.grid(row=5,column=1)
b=Button(a,text='submit',command=process).grid(row=10,column=10)
a.mainloop()