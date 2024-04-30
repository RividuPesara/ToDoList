import json
import tkinter as tk
from tkinter import messagebox

def input_int(prompt, max_value):
    while True:
        try:
            num = int(prompt.strip())
            if 1 <= num <= max_value:
                return num
        except ValueError:
            continue

def input_task(prompt):
    while True:
        task_description = prompt.strip()
        if task_description:
            return task_description
        else:
            continue

def save_tasks(tasks):
    with open('todo_list.txt', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    description = task_entry.get()
    if description:
        task = {"description": description}
        tasks.append(task)
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Empty Description", "Please enter a task description.")

def delete_task():
    if not tasks:
        messagebox.showinfo("No Tasks", "No tasks saved.")
    else:
        try:
            del_num = int(task_num.get().strip())
            if 1 <= del_num <= len(tasks):
                del tasks[del_num-1]
                save_tasks(tasks)
                update_task_list()
            else:
                messagebox.showwarning("Invalid Task Number", "Please enter a valid task number.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid task number.")

def update_task_list():
    task_list.delete(0, tk.END)
    if tasks:
        for index, task in enumerate(tasks):
            task_get=task["description"]
            task_list.insert(tk.END, f"{index+1}. {task_get}")
    else:
        task_list.insert(tk.END, "No tasks saved.")

def quit_app():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("To-Do List")

tasks = []
try:
    with open('todo_list.txt', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    pass

task_label = tk.Label(root, text="Task Description:")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=5)

task_list = tk.Listbox(root, width=60)
task_list.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

delete_label = tk.Label(root, text="Task Number to Delete:")
delete_label.grid(row=2, column=0, padx=5, pady=5)

task_num = tk.Entry(root, width=10)
task_num.grid(row=2, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=2, column=2, padx=5, pady=5)

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.grid(row=3, column=1, padx=5, pady=10)

update_task_list()

root.mainloop()
