from tkinter import *

def operand(no):
    global exp
    exp=exp+no
    print(exp)
    t.set(exp)

def clear():
    global exp
    exp=""
    print(exp)
    t.set("")


def ans():
    global exp
    a=str(eval(exp))
    t.set(a)
    print(a)
    exp=""


root=Tk()
root.title("My Calculator")
root.resizable(0,0)
root.wm_iconbitmap("notepad.ico")
t=StringVar()
exp=""

text=Entry(root,justify="right",font=("Arial",20,"bold"),bd=30,insertwidth=3,bg="black",fg="white",textvariable=t).grid(columnspan=4)
b1=Button(root,text="1",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('1')).grid(row=1,column=0)
b2=Button(root,text="2",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('2')).grid(row=1,column=1)
b3=Button(root,text="3",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('3')).grid(row=1,column=2)
bsum=Button(root,text="+",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('+')).grid(row=1,column=3)

b4=Button(root,text="4",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('4')).grid(row=2,column=0)
b5=Button(root,text="5",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('5')).grid(row=2,column=1)
b6=Button(root,text="6",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('6')).grid(row=2,column=2)
bsub=Button(root,text="-",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('-')).grid(row=2,column=3)

b7=Button(root,text="7",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('7')).grid(row=3,column=0)
b8=Button(root,text="8",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('8')).grid(row=3,column=1)
b9=Button(root,text="9",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('9')).grid(row=3,column=2)
bmul=Button(root,text="*",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('*')).grid(row=3,column=3)

bcl=Button(root,text="C",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=clear).grid(row=4,column=0)
b0=Button(root,text="0",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('0')).grid(row=4,column=1)
bdot=Button(root,text=".",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('.')).grid(row=4,column=2)
bdiv=Button(root,text="/",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=lambda:operand('/')).grid(row=4,column=3)

beq=Button(root,text="=",padx=16,pady=16,fg="black",font=("Arial",20,"bold"),bd=8,command=ans).grid(row=5,columnspan=4)

mainloop()



#icon-icon.com  for icons
#python final.py build
#python final.py bdist_msi