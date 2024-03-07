from tkinter import*
import ttkbootstrap
from tkinter import ttk

def _add_(digit):
    value=display.get()
    if value == "0":
        value = digit
    else:
        value+= digit
    display.delete(0,END)
    display.insert(0,value)

def add_operator(operator):
    global first_num
    first_num= int(display.get())
    global math_operator
    math_operator = operator
    display.delete(0,END)

def calculate():
    second_num =  int(display.get())
    display.delete(0,END)
    if math_operator == "+":
        result = first_num + second_num
    elif math_operator == "-":
        result = first_num - second_num
    elif math_operator == "*":
        result = first_num * second_num
    else:
        result = first_num / second_num
    display.insert(0, result)

def clear():
    display.delete(0,END)
    display.insert(0,"0")

root=ttkbootstrap.Window(themename="flatly")
root.title("Calculator")
root.geometry("350x300")

display = ttk.Entry(root, font=("Helvetica", 20), justify=RIGHT)
display.insert(0, "0")
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


button_1 = ttk.Button(root, text="1",bootstyle="primary" , command=lambda: _add_("1"))
button_2 = ttk.Button(root, text="2", bootstyle="primary", command=lambda: _add_("2"))
button_3 = ttk.Button(root, text="3", bootstyle="primary", command=lambda: _add_("3"))
button_4 = ttk.Button(root, text="4", bootstyle="primary", command=lambda: _add_("4"))
button_5 = ttk.Button(root, text="5", bootstyle="primary", command=lambda: _add_("5"))
button_6 = ttk.Button(root, text="6", bootstyle="primary", command=lambda: _add_("6"))
button_7 = ttk.Button(root, text="7", bootstyle="primary", command=lambda: _add_("7"))
button_8 = ttk.Button(root, text="8", bootstyle="primary", command=lambda: _add_("8"))
button_9 = ttk.Button(root, text="9", bootstyle="primary", command=lambda: _add_("9"))
button_0 = ttk.Button(root, text="0", bootstyle="primary", command=lambda: _add_("0"))


button_add = ttk.Button(root, text="+", bootstyle="warning", command=lambda: add_operator("+"))
button_subtract = ttk.Button(root, text="-", bootstyle="warning", command=lambda: add_operator("-"))
button_multiply = ttk.Button(root, text="*", bootstyle="warning", command=lambda: add_operator("*"))
button_divide = ttk.Button(root, text="/", bootstyle="warning", command=lambda: add_operator("/"))
button_equal = ttk.Button(root, text="=", bootstyle="success", command=calculate)
button_clear = ttk.Button(root, text="AC", bootstyle="danger", command=clear)


button_1.grid(row=3, column=0, padx=5, pady=5)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_7.grid(row=1, column=0, padx=5, pady=5)
button_8.grid(row=1, column=1, padx=5, pady=5)
button_9.grid(row=1, column=2, padx=5, pady=5)
button_0.grid(row=4, column=0, padx=5, pady=5)

button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)
button_equal.grid(row=4, column=1, padx=5, pady=5)
button_clear.grid(row=4, column=2, padx=5, pady=5)

root.mainloop()
