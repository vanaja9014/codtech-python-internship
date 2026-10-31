# CodTech Task 2 - TO-DO LIST (Tkinter GUI)
# Intern ID: CITS9786 | Name: Dasari Vanaja

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def clear_all():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("CodTech To-Do List - Vanaja")
root.geometry("400x450")
root.config(bg="#f0f0f0")

tk.Label(root, text="My To-Do List", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)
tk.Button(frame, text="Add Task", command=add_task, bg="green", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Delete", command=delete_task, bg="red", fg="white", width=10).grid(row=0, column=1, padx=5)
tk.Button(root, text="Clear All", command=clear_all, bg="blue", fg="white", width=22).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 11))
listbox.pack(pady=10)

root.mainloop()
