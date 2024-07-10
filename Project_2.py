import tkinter as tk
from tkinter import filedialog, messagebox
import pyqrcode
import png
from PIL import Image, ImageTk

def generate_qr():
    text = entry.get()
    if not text:
        messagebox.showerror("Error", "Input field cannot be empty!")
        return
    
    qr = pyqrcode.create(text)
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr.png(file_path, scale=8)
        display_qr_code(file_path)

def display_qr_code(file_path):
    img = Image.open(file_path)
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

app = tk.Tk()
app.title("QR Code Generator")

tk.Label(app, text="Enter URL or Text:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(app, width=40)
entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(app, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)

qr_label = tk.Label(app)
qr_label.grid(row=2, columnspan=2, padx=10, pady=10)

app.mainloop()
