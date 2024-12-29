# imports
from tkinter import *
from tkinter import messagebox
import random


# generate password function
def generate_password():
    # delete previous text from entry box and get length of the password
    return_password_entry.delete(0, END)
    get_password_length = int(password_length_entry.get())

    # characters that password must be comprised of:
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()"

    # create the password
    for i in range(0, get_password_length):
        password = random.choice(lower_case_letters + upper_case_letters + numbers + symbols)
        return_password_entry.insert(END, password)


# copy password to clipboard function
def copy_password():
    root.clipboard_append(return_password_entry.get())
    messagebox.showinfo(title="Password Copied to Clipboard!", message="Your password was successfully copied to your clipboard!")


# screen
root = Tk()
root.geometry("600x600")
root.title("High Seas Password Generator")

# title label
title_label = Label(root, text="Password Generator", font=("Arial", 30))
title_label.pack()

# main frame
main_frame = Frame(root)
main_frame.pack(pady=60)

# password length label
password_length_label = Label(main_frame, text="Password Length: ", font=("Arial", 20))
password_length_label.pack()

# entry box for password length
password_length_entry = Entry(main_frame, font=("Arial", 16))
password_length_entry.pack()

# return password entry
return_password_entry = Entry(main_frame, font=("Arial", 26), bg="dodgerblue")
return_password_entry.pack(pady=36)

# generate password button
generate_password_btn = Button(main_frame, text="Generate Password", width=16, height=1, font=("Arial", 14), command=generate_password)
generate_password_btn.pack()

# copy password to clipboard button
copy_password_btn = Button(main_frame, text="Copy to Clipboard", width=16, height=1, font=("Arial", 14), command=copy_password)
copy_password_btn.pack()

# mainloop
root.mainloop()