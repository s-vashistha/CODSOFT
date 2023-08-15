import tkinter as tk
from tkinter import ttk, messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        heading_label = tk.Label(root, text="Welcome to My App!", font=("Helvetica", 16, "bold"), fg="grey")
        heading_label.pack()  

        self.tasks = []
        self.load_tasks()

        self.style = ttk.Style()
        self.style.configure("TButton",height=5, padding=5, relief="flat", background="#4CAF50", foreground="black")
        self.style.configure("TLabel", padding=5, background="#f6f")
        self.style.configure("TEntry", padding=5)

        self.root.configure(background="#4CA")  
        
        self.text_label = tk.Label(root, text="TO-DO LIST",font=("Arial", 16, "bold"), fg="green",justify= "left", pady=5)
        self.text_label.pack()


        self.task_entry = ttk.Entry(root, style="TEntry")
        self.task_entry.pack(pady=20)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.pack()

        self.tasks_frame = ttk.Frame(root)
        self.tasks_frame.pack()

        self.update_task_list()
    

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            self.task_entry.delete(0, "end")
            self.update_task_list()

    def update_task_list(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks, start=1):
            task_label = tk.Label (self.tasks_frame,text=f"{index}. {task}",background="#905090",pady=10,padx=30 )
            task_label.pack(anchor="w")

            update_button = tk.Button(
                self.tasks_frame, text="Update", command=lambda i=index: self.update_task(i)
            )
            update_button.pack(anchor="w" )

            delete_button = tk.Button(
                self.tasks_frame, text="Delete", command=lambda i=index: self.delete_task(i)
            )
            delete_button.pack(anchor="w")

    def update_task(self, index):
        updated_task = self.task_entry.get()
        if updated_task:
            self.tasks[index - 1] = updated_task
            self.save_tasks()
            self.task_entry.delete(0, "end")
            self.update_task_list()

    def delete_task(self, index):
        self.tasks.pop(index - 1)
        self.save_tasks()
        self.update_task_list()

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]


    

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
