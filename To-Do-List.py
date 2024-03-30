#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.heading_label = tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold"), bg="#b0e0e6")
        self.heading_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=40, selectmode=tk.SINGLE, bg="#c9f7c5")
        self.task_listbox.pack()

        self.mark_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_listbox()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks.sort()  # Sort tasks in alphabetical order
            self.update_task_listbox()
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            if not task.startswith("[✓]"):
                self.tasks[index] = "[✓] " + task
            self.update_task_listbox()
            self.save_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            new_task = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=task)
            if new_task is not None:
                self.tasks[index] = new_task
                self.update_task_listbox()
                self.save_tasks()

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




