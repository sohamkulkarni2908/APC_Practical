from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Registration Form")
root.geometry("350x350")

Label(root, text = "Registration Form", font = ("Ariel",16)).pack()

Label(root, text = "Name").pack()
name = Entry(root)
name.pack()

Label(root, text = "Email").pack()
email = Entry(root)
email.pack()

Label(root, text = "Password").pack()
ps = Entry(root, show = "*")
ps.pack()

def register():
    messagebox.showinfo("Success","Registration Successful !")

Button(root, text = "Register",command= register).pack(pady= 20)

root.mainloop()