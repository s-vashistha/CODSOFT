import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length, complexity):
    characters = string.ascii_letters + string.digits + string.punctuation
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    length = int(length_entry.get())
    complexity = complexity_combo.get().lower()
    
    password = generate_password(length, complexity)
    password_label.config(text="Generated Password: " + password)

# main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#467892")  

# style
style = ttk.Style()
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 16, "bold"))
style.configure("TButton", background="#007acc", foreground="black")
style.configure("TCombobox", background="white")
heading_label = tk.Label(root, text="Welcome to My App!", font=("Helvetica", 16, "bold"), fg="red")
heading_label.pack(pady=10)
# create and place widgets
length_label = ttk.Label(root, text="Enter password length:")
length_label.pack(pady=10)

length_entry = ttk.Entry(root)
length_entry.pack(pady=5)

complexity_label = ttk.Label(root, text="Select complexity level:")
complexity_label.pack()

complexity_values = ["Low", "Medium", "High"]
complexity_combo = ttk.Combobox(root, values=complexity_values, state="readonly")
complexity_combo.set("High")
complexity_combo.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_button_click)
generate_button.pack(pady=10)

password_label = ttk.Label(root, text="Generated Password: ")
password_label.pack()


root.mainloop()
