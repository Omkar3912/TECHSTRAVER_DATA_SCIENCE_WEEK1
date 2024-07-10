import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = int(length_entry.get())
    min_digits = int(digits_entry.get())
    include_special = special_var.get()

    if length < min_digits:
        messagebox.showerror("Error", "Password length cannot be less than the minimum number of digits.")
        return
    
    password_chars = string.ascii_letters
    if include_special:
        password_chars += string.punctuation
    password_chars += string.digits

    password = []
    for _ in range(min_digits):
        password.append(random.choice(string.digits))
    
    while len(password) < length:
        password.append(random.choice(password_chars))
    
    random.shuffle(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, ''.join(password))

app = tk.Tk()
app.title("Password Generator")

tk.Label(app, text="Password Length:").grid(row=0, column=0, padx=100, pady=100)
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=20, pady=20)

tk.Label(app, text="Minimum Digits:").grid(row=1, column=0, padx=20, pady=20)
digits_entry = tk.Entry(app)
digits_entry.grid(row=1, column=1, padx=20, pady=20)

special_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include Special Characters", variable=special_var).grid(row=2, columnspan=2, padx=20, pady=20)

tk.Button(app, text="Generate Password", command=generate_password).grid(row=3, columnspan=2, padx=20, pady=20)

password_entry = tk.Entry(app, width=40)
password_entry.grid(row=4, columnspan=2, padx=20, pady=20)

app.mainloop()
