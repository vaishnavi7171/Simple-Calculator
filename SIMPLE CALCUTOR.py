from tkinter import*
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_no=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_no)
    e.delete(0,END)
def button_equal():
    sec_no=e.get()
    e.delete(0,END)
    if(math=="addition"):
        e.insert(0,f_num+int(sec_no))
    
    if(math=="subtraction"):
        e.insert(0,f_num-int(sec_no))
    
    if(math=="multiplication"):
        e.insert(0,f_num*int(sec_no))
    
    if(math=="division"):
        e.insert(0,f_num/int(sec_no))
    
    if(math=="square"):
        e.insert(0,f_num*f_num)
def button_subtract():
    first_no=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_no)
    e.delete(0,END)
def button_multiply():
    first_no=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_no)
    e.delete(0,END)
def button_divide():
    first_no=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_no)
    e.delete(0,END)


b_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
b_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
b_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
b_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
b_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
b_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
b_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
b_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
b_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
b_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
b_add=Button(root,text="+",padx=39,pady=20,command=button_add)
b_equal=Button(root,text="=",padx=40,pady=20,command=button_equal)
b_clear=Button(root,text="Clear",padx=30,pady=20,command=button_clear)
b_subtract=Button(root,text="-",padx=41,pady=20,command=button_subtract)
b_multiply=Button(root,text="*",padx=40,pady=20,command=button_multiply)
b_divide=Button(root,text="/",padx=41,pady=20,command=button_divide)

b_1.grid(row=3,column=0)
b_2.grid(row=3,column=1)
b_3.grid(row=3,column=2)
b_4.grid(row=2,column=0)
b_5.grid(row=2,column=1)
b_6.grid(row=2,column=2)
b_7.grid(row=1,column=0)
b_8.grid(row=1,column=1)
b_9.grid(row=1,column=2)
b_0.grid(row=4,column=0)
b_clear.grid(row=4,column=1,columnspan=1)
b_equal.grid(row=4,column=3,columnspan=2)
b_add.grid(row=3,column=3)
b_subtract.grid(row=2,column=3)
b_multiply.grid(row=1,column=3)
b_divide.grid(row=4,column=2)


root.mainloop()