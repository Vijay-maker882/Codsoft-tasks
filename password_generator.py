import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_var.get())

    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy password
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title Label
tk.Label(root, text="🔐 Random Password Generator", font=("Arial", 14, "bold")).pack(pady=10)

# Password length
tk.Label(root, text="Select Password Length:", font=("Arial", 10)).pack()
length_var = tk.StringVar(value="12")
tk.Spinbox(root, from_=4, to=50, textvariable=length_var, width=5, font=("Arial", 10)).pack(pady=5)

# Options
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

frame = tk.Frame(root)
frame.pack(pady=5)
tk.Checkbutton(frame, text="Include Letters (A-Z)", variable=letters_var).grid(row=0, column=0, sticky="w")
tk.Checkbutton(frame, text="Include Numbers (0-9)", variable=numbers_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame, text="Include Symbols (!@#$)", variable=symbols_var).grid(row=2, column=0, sticky="w")

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 11), bg="#4CAF50", fg="white").pack(pady=10)

# Display password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, justify="center").pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Arial", 10), bg="#2196F3", fg="white").pack(pady=5)

# Run GUI
root.mainloop()