from tkinter import *
from tkinter import messagebox
import random
import string

def generate_password():
    generated_password.set('')

    try:
        password_length = int(password_length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length (integer)")
        return

    if password_length <= 0:
        messagebox.showerror("Error", "Please enter a valid password length")
        return

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    selected_options = [
        lowercase_var.get(),
        uppercase_var.get(),
        digits_var.get(),
        special_var.get()
    ]

    selected_characters = [lowercase_letters if selected_options[0] else '',
                           uppercase_letters if selected_options[1] else '',
                           digits if selected_options[2] else '',
                           special_characters if selected_options[3] else '']

    all_characters = ''.join(selected_characters)

    if not any(selected_options):
        messagebox.showerror("Error", "Please select at least one option for complexity")
        return

    password = ''.join(random.choice(all_characters) for _ in range(password_length))
    generated_password.set(password)

   
    password_length_entry.delete(0, END)
    lowercase_var.set(False)
    uppercase_var.set(False)
    digits_var.set(False)
    special_var.set(False)

root = Tk()
root.geometry('600x450')
root.title('Password Generator')
root.config(bg='#FFE4E1')
root.resizable(0, 0)

generated_password = StringVar()

Label(root, text='Password Length:', font=('Times new roman', 16, 'bold'), bg='#FFE4E1').place(x=20, y=20)
password_length_entry = Entry(root, font=('Arial', 12), width=30)
password_length_entry.place(x=200, y=20)

Label(root, text='Password Complexity:', font=('Times new roman', 16, 'bold'), bg='#FFE4E1').place(x=20, y=70)

lowercase_var = BooleanVar()
Checkbutton(root, text='Lowercase Letters', variable=lowercase_var, font=('Arial', 12), bg='#FFE4E1').place(x=250, y=70)

uppercase_var = BooleanVar()
Checkbutton(root, text='Uppercase Letters', variable=uppercase_var, font=('Arial', 12), bg='#FFE4E1').place(x=250, y=100)

digits_var = BooleanVar()
Checkbutton(root, text='Digits', variable=digits_var, font=('Arial', 12), bg='#FFE4E1').place(x=250, y=130)

special_var = BooleanVar()
Checkbutton(root, text='Special Characters', variable=special_var, font=('Arial', 12), bg='#FFE4E1').place(x=250, y=160)

Button(root, text="Generate Password", font=('Times new roman', 16, 'bold'), bg='#B0C4DE', command=generate_password).place(x=200, y=220)

Label(root, text='Generated Password:', font=('Times new roman', 16, 'bold'), bg='#FFE4E1').place(x=20, y=300)
generated_password_entry = Entry(root, textvariable=generated_password, font=('Arial', 12), width=30, state='readonly')
generated_password_entry.place(x=230, y=300)
generated_password_entry.config(bg='#FFFFFF')
Button(root, text="EXIT", font='Helvetica 18 bold', bg='#FF0000', command=root.destroy).place(x=250, y=350)

root.mainloop()
