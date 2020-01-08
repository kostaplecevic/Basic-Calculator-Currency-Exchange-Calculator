from tkinter import *
import requests
from datetime import date
import time

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

# Function for changing frames

def raise_frame(frame_number):
    if frame_number == "Currency":
        root.geometry("309x350+400+175")
        currency_frame.tkraise()
    elif frame_number == "Simple":
        root.geometry("309x330+400+175")
        simple_frame.tkraise()

today = date.today()
t = time.localtime()

#Defining GUI and frames

root = Tk()
root.title("Simple Calc")
root.geometry("309x330+400+175")
root.configure(background='#837e7e')
root.iconbitmap("Guillendesign-Variations-1-Calculator-3.ico")

currency_frame = Frame(root, background='#837e7e')
currency_frame.place(x=0, y=0, width=500, height=500)

simple_frame = Frame(root, background='#837e7e')
simple_frame.place(x=0, y=0, width=500, height=500)

e = Entry(simple_frame, width=11, borderwidth=5, font=("Helvetica", 15), bg="#a49b9b", justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
e.grid(row=0,column=0,columnspan=3,padx=11,pady=10,sticky=W)
e.focus_set()

#Changing frames


choices = {
    "Simple":simple_frame,
    "Currency":currency_frame
}
change = StringVar(root)
change.set("Simple")
dropdownMenu = OptionMenu(simple_frame, change, *choices)
dropdownMenu.config(width=10)
dropdownMenu.grid(row=0, column=2,columnspan=2, sticky="W")

button_change = HoverButton(simple_frame, text="Change", command=lambda: raise_frame(change.get()))
button_change.grid(row=0,column=3, sticky="E")

dropdownMenu2 = OptionMenu(currency_frame, change, *choices)
dropdownMenu2.config(width=10)
dropdownMenu2.grid(row=0, column=0, sticky="E")

button_change2 = HoverButton(currency_frame, text="Change", command=lambda: raise_frame(change.get()))
button_change2.grid(row=0,column=2, sticky="E")


#Defining simple_frame button functions

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
        result = round(f_num * float((float(second_number)/100)),2)
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


#Define simple_frame buttons

button_clear = HoverButton(simple_frame, text="C",padx=29, pady=15, command=button_clear, activebackground='#989393', background="#6d6565", fg="white")
button_squared = HoverButton(simple_frame, text="**",padx=28, pady=15, command=button_squared, activebackground='#989393', background="#6d6565", fg="white")
button_percent = HoverButton(simple_frame, text="%",padx=30, pady=15, command=button_percent, activebackground='#989393', background="#6d6565", fg="white")
button_divide = HoverButton(simple_frame, text="/",padx=32, pady=15, command=button_divide, activebackground='#989393', background="#6d6565", fg="white")

button_7 = HoverButton(simple_frame, text="7",padx=30, pady=15, command=lambda: button_click(7), activebackground='#504e4e', background='#252323', fg="white")
button_8 = HoverButton(simple_frame, text="8",padx=30, pady=15, command=lambda: button_click(8), activebackground='#504e4e', background='#252323', fg="white")
button_9 = HoverButton(simple_frame, text="9",padx=32, pady=15, command=lambda: button_click(9), activebackground='#504e4e', background='#252323', fg="white")
button_multiply = HoverButton(simple_frame, text="X",padx=31, pady=15, command=button_multiply, activebackground='#989393', background="#6d6565", fg="white")

button_4 = HoverButton(simple_frame, text="4",padx=30, pady=15, command=lambda: button_click(4), activebackground='#504e4e', background='#252323', fg="white")
button_5 = HoverButton(simple_frame, text="5",padx=30, pady=15, command=lambda: button_click(5), activebackground='#504e4e', background='#252323', fg="white")
button_6 = HoverButton(simple_frame, text="6",padx=32, pady=15, command=lambda: button_click(6), activebackground='#504e4e', background='#252323', fg="white")
button_subtract = HoverButton(simple_frame, text="-",padx=32, pady=15, command=button_subtract, activebackground='#989393', background="#6d6565", fg="white")

button_1 = HoverButton(simple_frame, text="1",padx=30, pady=15, command=lambda: button_click(1), activebackground='#504e4e', background='#252323', fg="white")
button_2 = HoverButton(simple_frame, text="2",padx=30, pady=15, command=lambda: button_click(2), activebackground='#504e4e', background='#252323', fg="white")
button_3 = HoverButton(simple_frame, text="3",padx=32, pady=15, command=lambda: button_click(3), activebackground='#504e4e', background='#252323', fg="white")
button_add = HoverButton(simple_frame, text="+",padx=31, pady=15, command=button_add, activebackground='#989393', background="#6d6565", fg="white")

button_plusminus = HoverButton(simple_frame, text="+/-",padx=24, pady=15, command=button_plusminus, activebackground='#989393', background="#6d6565", fg="white")
button_0 = HoverButton(simple_frame,text="0",padx=30, pady=15, command=lambda: button_click(0), activebackground='#504e4e', background='#252323', fg="white")
button_dot = HoverButton(simple_frame, text=".",padx=33, pady=15, command=button_dot, activebackground='#989393', background="#6d6565", fg="white")
button_equal = HoverButton(simple_frame, text="=",padx=31, pady=15, command=button_equal, activebackground='#989393', background="#6d6565", fg="white")

# Put simple_frame buttons on screen

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

# Currency frame


choices = {
    "European Union Euro":  'EUR',
    "United States Dollar": 'USD',
    "United Kingdom Pound": 'GBP',
    "Switzerland Franc":    'CHF',
    "Chinese Yuan":         'CNY',
    "Russian Rouble":       'RUB',
    "Japanese Yen":         'JPY',
    "Indian Rupee":         'INR'
}

clicked = StringVar()
clicked.set("Select a currency")
clicked2 = StringVar()
clicked2.set("Select a currency")

def get_time():
    date = today.strftime("%B %d, %Y")
    current_time = time.strftime("%H:%M", t)
    current_time_and_date = "Updated " + date + " " + current_time
    return current_time_and_date

# Manus and entries for currency_frame

e = Entry(currency_frame, width=6, borderwidth=5, font=("Helvetica", 15), bg="#a49b9b", justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
e.grid(row=1,column=0,columnspan=2,padx=1,pady=10,sticky=W+E)

drop = OptionMenu(currency_frame, clicked, *choices)
drop.grid(row=1,column=2,columnspan=4,padx=11,pady=10,sticky=W+E)

e2 = Entry(currency_frame, width=6, borderwidth=5, font=("Helvetica", 15), bg="#a49b9b", justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
e2.grid(row=2,column=0,columnspan=2,padx=1,pady=10,sticky=W+E)

drop2 = OptionMenu(currency_frame, clicked2, *choices)
drop2.grid(row=2,column=2,columnspan=4,padx=11,pady=10,sticky=W+E)

# Button and update functions for currency frame


def update():
    global currency
    global currency2
    global rate

    currency = choices[clicked.get()]
    currency2 = choices[clicked2.get()]
    url = 'https://api.exchangerate-api.com/v4/latest/' + currency

    response = requests.get(url)
    data = response.json()
    rate = data['rates'][currency2]
    #print(rate)
    #print(data['rates'][currency2])
    #print(data)

    currency_string = "1 " + str(currency) + " = " + str(rate) + " " + str(currency2)
    current_rate_label = Label(currency_frame, text=currency_string, background='#837e7e', fg="white", font=("Helvetica", 10))
    current_rate_label.grid(row=4, column=0, columnspan=3, sticky=W)

    current_time_label = Label(currency_frame, text=get_time(), background='#837e7e', fg="white", font=("Helvetica", 10))
    current_time_label.grid(row=5, column=0, columnspan=3, sticky=E)
    if e.get() != '':
        number = e.get()
        number = float(number)
        result = number * rate
        result = round(result, 3)
        e2.delete(0, END)
        e2.insert(0, str(result))

def button_click(number):  # Chooses a number, gets the rates, converts and writes out the result
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

    number = e.get()
    number = float(number)
    result = number * rate
    result = round(result, 3)
    e2.delete(0, END)
    e2.insert(0, str(result))

def button_clear():
    e.delete(0, END)
    e2.delete(0 , END)

def button_dot():
    string = e.get()
    e.delete(0, END)
    string = string+"."
    e.insert(END, string)

def backspace():
    e_lenght = len(e.get()) - 1
    e.delete(e_lenght, END)

    number = e.get()
    number = float(number)
    result = number*rate
    result = round(result, 3)
    e2.delete(0, END)
    e2.insert(0, str(result))

current_rate_label = Label(currency_frame, text="", background='#837e7e', fg="white", font=("Helvetica", 10))
current_rate_label.grid(row=4, column=0, columnspan=3, sticky=W)

current_time_label = Label(currency_frame, text="", background='#837e7e', fg="white", font=("Helvetica", 10))
current_time_label.grid(row=5, column=0, columnspan=3, sticky=E)

#convert_button = Button(currency_frame, text="Convert", command=convert)
#convert_button.grid()

#Define currency frame buttons

update_button = HoverButton(currency_frame, text="Update rates", command=lambda: update(), activebackground='#837e7e', background='#837e7e',activeforeground="white", fg="white", borderwidth= 0, font=("Helvetica", 10, "bold", "underline"))
update_button.grid(row=6,column=0, pady=4)

button_clear = HoverButton(currency_frame, text="C", width=10, padx= 10, command=button_clear, activebackground='#989393', background="#6d6565", fg="white")
button_backspace = HoverButton(currency_frame, text="DEL", width=10, padx= 10, command=backspace, activebackground='#989393', background="#6d6565", fg="white")

button_7 = HoverButton(currency_frame, text="7",width=11, padx= 10, command=lambda: button_click(7), activebackground='#504e4e', background='#252323', fg="white")
button_8 = HoverButton(currency_frame, text="8",width=10, padx= 10, command=lambda: button_click(8), activebackground='#504e4e', background='#252323', fg="white")
button_9 = HoverButton(currency_frame, text="9",width=10, padx= 10, command=lambda: button_click(9), activebackground='#504e4e', background='#252323', fg="white")

button_4 = HoverButton(currency_frame, text="4",width=11, padx= 10, command=lambda: button_click(4), activebackground='#504e4e', background='#252323', fg="white")
button_5 = HoverButton(currency_frame, text="5",width=10, padx= 10, command=lambda: button_click(5), activebackground='#504e4e', background='#252323', fg="white")
button_6 = HoverButton(currency_frame, text="6",width=10, padx= 10, command=lambda: button_click(6), activebackground='#504e4e', background='#252323', fg="white")

button_1 = HoverButton(currency_frame, text="1",width=11, padx= 10, command=lambda: button_click(1), activebackground='#504e4e', background='#252323', fg="white")
button_2 = HoverButton(currency_frame, text="2",width=10, padx= 10, command=lambda: button_click(2), activebackground='#504e4e', background='#252323', fg="white")
button_3 = HoverButton(currency_frame, text="3",width=10, padx= 10, command=lambda: button_click(3), activebackground='#504e4e', background='#252323', fg="white")

button_0 = HoverButton(currency_frame,text="0", width=10, padx= 10, command=lambda: button_click(0), activebackground='#504e4e', background='#252323', fg="white")
button_dot = HoverButton(currency_frame, text=".", width=10, padx= 10, command=button_dot, activebackground='#989393', background="#6d6565", fg="white")

# Put currency_frame buttons on screen

button_clear.grid(row=7, column=2, columnspan=2)
button_backspace.grid(row=7, column=4, columnspan=2)

button_7.grid(row=8,column=0, columnspan=1)
button_8.grid(row=8,column=2, columnspan=2)
button_9.grid(row=8,column=4, columnspan=2)

button_4.grid(row=9,column=0, columnspan=1)
button_5.grid(row=9,column=2, columnspan=2)
button_6.grid(row=9,column=4, columnspan=2)

button_1.grid(row=10, column=0, columnspan=1)
button_2.grid(row=10, column=2, columnspan=2)
button_3.grid(row=10, column=4, columnspan=2)

button_0.grid(row=11, column=2, columnspan=2)
button_dot.grid(row=11, column=4, columnspan=2)


root.mainloop()