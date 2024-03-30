#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import ttk
from math import sqrt, sin, cos, tan, radians, exp
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_ui()

    def create_ui(self):
        self.result_entry = ttk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20), justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipadx=8, ipady=8)

        buttons = [
            "7", "8", "9", "/", "sqrt", "sin",
            "4", "5", "6", "*", "pow", "cos",
            "1", "2", "3", "-", "exp", "tan",
            "C", "0", "=", "+"
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(self.root, text=button, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 5:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_text = self.result_var.get()

        if button == "C":
            self.result_var.set("0")
        elif button == "=":
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
        elif button == "sqrt":
            self.result_var.set(str(sqrt(float(current_text))))
        elif button == "pow":
            try:
                result = str(eval(current_text + "**2"))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
        elif button == "sin":
            self.result_var.set(str(sin(radians(float(current_text)))))
        elif button == "cos":
            self.result_var.set(str(cos(radians(float(current_text)))))
        elif button == "tan":
            self.result_var.set(str(tan(radians(float(current_text)))))
        elif button == "exp":
            self.result_var.set(str(exp(float(current_text))))
        else:
            if current_text == "0":
                self.result_var.set(button)
            else:
                self.result_var.set(current_text + button)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:





# In[2]:


import tkinter as tk
from tkinter import ttk
from math import sqrt, sin, cos, tan, radians, exp
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_ui()

    def create_ui(self):
        self.result_entry = ttk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20), justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipadx=8, ipady=8)

        buttons = [
            "7", "8", "9", "/", "sqrt", "sin",
            "4", "5", "6", "*", "pow", "cos",
            "1", "2", "3", "-", "exp", "tan",
            "C", "0", "=", "+"
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(self.root, text=button, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 5:
                col_val = 0
                row_val += 1

    def button_click(self, button):
        current_text = self.result_var.get()

        if button == "C":
            self.result_var.set("0")
        elif button == "=":
            try:
                result = str(eval(current_text))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
        elif button == "sqrt":
            self.result_var.set(str(sqrt(float(current_text))))
        elif button == "pow":
            try:
                result = str(eval(current_text + "**2"))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
        elif button == "sin":
            self.result_var.set(str(sin(radians(float(current_text)))))
        elif button == "cos":
            self.result_var.set(str(cos(radians(float(current_text)))))
        elif button == "tan":
            self.result_var.set(str(tan(radians(float(current_text)))))
        elif button == "exp":
            self.result_var.set(str(exp(float(current_text))))
        else:
            if current_text == "0":
                self.result_var.set(button)
            else:
                self.result_var.set(current_text + button)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




