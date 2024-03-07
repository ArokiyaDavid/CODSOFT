from tkinter import *
from tkinter import messagebox
import pyperclip
import random

def generate_password():
    length = int(string_pass.get())
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num = ['0','1','2','3','4','5','6','7','8','9']
    special = ['@','#','$','%','&','*']
    all_chars = lower + upper + num + special

    if length < 6:
        messagebox.showerror('Error','Password length should be at least 6 characters.')
    else:
        generated_password = ''.join(random.sample(all_chars, length))
        messagebox.showinfo('Result','Your Password is: {}'.format(generated_password))
        pyperclip.copy(generated_password)

password = Tk()
password.title("Password Generator")
password.geometry('250x200')
password.resizable(0,0)

string_pass = StringVar()
Label(password, text="Enter Password Length").pack(pady=10)
Entry(password, textvariable=string_pass).pack()

btn_generate = Button(password, text="Generate", command=generate_password, bg='green',borderwidth=10)
btn_generate.pack(pady=10)

password.mainloop()
