from tkinter import *

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


root = Tk()
root.title("Simple Calc")
root.geometry("309x330+400+175")
root.configure(background='#837e7e')
root.iconbitmap("Guillendesign-Variations-1-Calculator-3.ico")

e = Entry(root, width=12, borderwidth=5, font=("Helvetica", 15), bg="#a49b9b", justify=RIGHT, relief=SUNKEN)
e.grid(row=0,column=0,columnspan=4,padx=11,pady=10,sticky=N+W+E)
e.focus_set()


#Defining button functions

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math=="addition":
        result = f_num + float(second_number)
        if result % 1 == 0:
            result = int(result)
        e.insert(0,result)
    if math=="subtraction":
        result = f_num - int(second_number)
        if result % 1 == 0:
            result = int(result)
        e.insert(0, result)
    if math=="multiplication":
        result = f_num * int(second_number)
        if result % 1 == 0:
            result = int(result)
        e.insert(0, result)
    if math=="division":
        result = f_num / int(second_number)
        if result % 1 == 0:
            result = int(result)
        e.insert(0, result)
    if math=="percentage":
        result = round(f_num * float((int(second_number)/100)),2)
        if result % 1 == 0:
            result = int(result)
        e.insert(0, result)
    if math=="squared":
        second_number = int(second_number)
        result = 1
        counter = second_number
        while counter !=0:
            result = result * f_num
            counter -= 1
        if result % 1 == 0:
            result = int(result)
        e.insert(0, result)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_percent():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = float(first_number)
    e.delete(0, END)

def button_squared():
    first_number = e.get()
    global f_num
    global math
    math = "squared"
    f_num = float(first_number)
    e.delete(0, END)

def button_dot():
    string = e.get()
    e.delete(0, END)
    string = string+"."
    e.insert(END, string)

def button_plusminus():
    value = e.get()
    e.delete(0, END)
    value = float(value) * -1
    e.insert(0, str(value))

#Define buttons

button_clear = HoverButton(root, text="C",padx=29, pady=15, command=button_clear, activebackground='#989393', background="#6d6565", fg="white")
button_squared = HoverButton(root, text="**",padx=28, pady=15, command=button_squared, activebackground='#989393', background="#6d6565", fg="white")
button_percent = HoverButton(root, text="%",padx=30, pady=15, command=button_percent, activebackground='#989393', background="#6d6565", fg="white")
button_divide = HoverButton(root, text="/",padx=32, pady=15, command=button_divide, activebackground='#989393', background="#6d6565", fg="white")

button_7 = HoverButton(root, text="7",padx=30, pady=15, command=lambda: button_click(7), activebackground='#504e4e', background='#252323', fg="white")
button_8 = HoverButton(root, text="8",padx=30, pady=15, command=lambda: button_click(8), activebackground='#504e4e', background='#252323', fg="white")
button_9 = HoverButton(root, text="9",padx=32, pady=15, command=lambda: button_click(9), activebackground='#504e4e', background='#252323', fg="white")
button_multiply = HoverButton(root, text="X",padx=31, pady=15, command=button_multiply, activebackground='#989393', background="#6d6565", fg="white")

button_4 = HoverButton(root, text="4",padx=30, pady=15, command=lambda: button_click(4), activebackground='#504e4e', background='#252323', fg="white")
button_5 = HoverButton(root, text="5",padx=30, pady=15, command=lambda: button_click(5), activebackground='#504e4e', background='#252323', fg="white")
button_6 = HoverButton(root, text="6",padx=32, pady=15, command=lambda: button_click(6), activebackground='#504e4e', background='#252323', fg="white")
button_subtract = HoverButton(root, text="-",padx=32, pady=15, command=button_subtract, activebackground='#989393', background="#6d6565", fg="white")

button_1 = HoverButton(root, text="1",padx=30, pady=15, command=lambda: button_click(1), activebackground='#504e4e', background='#252323', fg="white")
button_2 = HoverButton(root, text="2",padx=30, pady=15, command=lambda: button_click(2), activebackground='#504e4e', background='#252323', fg="white")
button_3 = HoverButton(root, text="3",padx=32, pady=15, command=lambda: button_click(3), activebackground='#504e4e', background='#252323', fg="white")
button_add = HoverButton(root, text="+",padx=31, pady=15, command=button_add, activebackground='#989393', background="#6d6565", fg="white")

button_plusminus = HoverButton(root, text="+/-",padx=24, pady=15, command=button_plusminus, activebackground='#989393', background="#6d6565", fg="white")
button_0 = HoverButton(root,text="0",padx=30, pady=15, command=lambda: button_click(0), activebackground='#504e4e', background='#252323', fg="white")
button_dot = HoverButton(root, text=".",padx=33, pady=15, command=button_dot, activebackground='#989393', background="#6d6565", fg="white")
button_equal = HoverButton(root, text="=",padx=31, pady=15, command=button_equal, activebackground='#989393', background="#6d6565", fg="white")

# Put buttons on screen

button_clear.grid(row=1,column=0,sticky=W)
button_squared.grid(row=1,column=1,sticky=W)
button_percent.grid(row=1,column=2,sticky=E)
button_divide.grid(row=1,column=3,sticky=E)

button_7.grid(row=2,column=0,sticky=W)
button_8.grid(row=2,column=1,sticky=W)
button_9.grid(row=2,column=2,sticky=E)
button_multiply.grid(row=2,column=3,sticky=E)

button_4.grid(row=3,column=0,sticky=W)
button_5.grid(row=3,column=1,sticky=W)
button_6.grid(row=3,column=2,sticky=E)
button_subtract.grid(row=3,column=3,sticky=E)

button_1.grid(row=4,column=0,sticky=W)
button_2.grid(row=4,column=1,sticky=W)
button_3.grid(row=4,column=2,sticky=E)
button_add.grid(row=4,column=3,sticky=E)

button_plusminus.grid(row=5,column=0,sticky=W)
button_0.grid(row=5,column=1,sticky=W)
button_dot.grid(row=5,column=2,sticky=E)
button_equal.grid(row=5,column=3,sticky=E)


root.mainloop()