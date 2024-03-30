#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
import random
import string
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.create_ui()

    def create_ui(self):
        heading_label = tk.Label(self.root, text="Password Generator", font=("Helvetica", 16, "bold"))
        heading_label.pack(pady=10)

        name_label = tk.Label(self.root, text="Name:")
        name_label.pack()

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        length_label = tk.Label(self.root, text="Password Length:")
        length_label.pack()

        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack()

        complexity_label = tk.Label(self.root, text="Complexity:")
        complexity_label.pack()

        self.complexity_combobox = ttk.Combobox(self.root, values=["Low", "Medium", "High"])
        self.complexity_combobox.pack()

        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=10)

        self.password_label = tk.Label(self.root, text="Generated Password:")
        self.password_label.pack()

        self.password_text = tk.Text(self.root, height=3, width=30)
        self.password_text.pack()

        accept_button = tk.Button(self.root, text="Accept", command=self.accept_password)
        accept_button.pack(pady=10)

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_form)
        reset_button.pack()

    def generate_password(self):
        length_text = self.length_entry.get()

        if not length_text.isdigit():
            messagebox.showerror("Error", "Invalid password length. Please enter a numeric value.")
            return

        length = int(length_text)
        complexity = self.complexity_combobox.get().lower()

        if complexity == "low":
            characters = string.ascii_letters + string.digits
        elif complexity == "medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_text.delete("1.0", tk.END)
        self.password_text.insert("1.0", password)

    def accept_password(self):
        name = self.name_entry.get()
        password = self.password_text.get("1.0", tk.END).strip()

        if name and password:
            messagebox.showinfo("Accepted", f"Name: {name}\nPassword: {password}")
        else:
            messagebox.showerror("Error", "Please enter both your name and a generated password.")

    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.complexity_combobox.set("")
        self.password_text.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




