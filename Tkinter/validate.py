from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.title("Registration Form")
root.geometry("350x400")

Label(root, text="Registration Form", font=("Arial", 16)).pack(pady=10)

Label(root, text="Name").pack()
name = Entry(root)
name.pack()

Label(root, text="Email").pack()
email = Entry(root)
email.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

Label(root, text="Age").pack()
age = Entry(root)
age.pack()


def register():
    n = name.get().strip()
    e = email.get().strip()
    p = password.get()
    a = age.get().strip()

    if n == "" or e == "" or p == "" or a == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    if not re.match(r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$", e):
        messagebox.showerror("Error", "Enter a valid email!")
        return

    if len(p) < 6:
        messagebox.showerror("Error", "Password must have at least 6 characters!")
        return

    if not a.isdigit() or int(a) <= 0 or int(a) > 120:
        messagebox.showerror("Error", "Enter a valid age!")
        return

    messagebox.showinfo("Success", "Registration Successful!")


Button(root, text="Register", command=register).pack(pady=20)

root.mainloop()