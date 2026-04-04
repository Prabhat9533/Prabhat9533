import tkinter as tk
from tkinter import messagebox

# -------------------- MAIN WINDOW --------------------
root = tk.Tk()
root.title("Daily To-Do List")
root.geometry("500x400")
root.config(bg="#f2f2f2")

tasks = [
    ("Drink 4 Liters Water", "6:00 AM - 9:00 PM"),
    ("Gym / Workout", "6:00 AM"),
    ("Healthy Diet", "All Day"),
    ("Study", "10:00 AM - 1:00 PM"),
    ("Skill Development", "4:00 PM - 6:00 PM"),
    ("Proper Sleep", "11:00 PM - 6:00 AM"),
]

task_list = []

# -------------------- FUNCTIONS --------------------
def add_task():
    task = task_entry.get()
    time = time_entry.get()

    if task == "" or time == "":
        messagebox.showerror("Error", "Please enter task and time")
        return

    task_listbox.insert(tk.END, f"{task}  |  {time}")
    task_list.append(task)
    task_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

def open_checklist():
    checklist = tk.Toplevel(root)
    checklist.title("Task Checklist")
    checklist.geometry("350x400")
    checklist.config(bg="white")

    tk.Label(
        checklist,
        text="✔ Daily Task Checklist",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack(pady=10)

    for task in task_listbox.get(0, tk.END):
        var = tk.IntVar()
        cb = tk.Checkbutton(
            checklist,
            text=task,
            variable=var,
            bg="white",
            font=("Arial", 10)
        )
        cb.pack(anchor="w", padx=20)

# -------------------- UI ELEMENTS --------------------
title = tk.Label(
    root,
    text="📝 Daily To-Do List",
    font=("Arial", 16, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=10)

task_listbox = tk.Listbox(root, width=60, height=8)
task_listbox.pack(pady=10)

# Insert default tasks
for t, time in tasks:
    task_listbox.insert(tk.END, f"{t}  |  {time}")
    task_list.append(t)

# Entry fields
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)
task_entry.insert(0, "Enter new task")

time_entry = tk.Entry(root, width=30)
time_entry.pack(pady=5)
time_entry.insert(0, "Enter time")

# Buttons
add_btn = tk.Button(
    root,
    text="Add Task",
    bg="blue",
    fg="white",
    width=15,
    command=add_task
)
add_btn.pack(pady=5)

check_btn = tk.Button(
    root,
    text="Open Checklist",
    bg="green",
    fg="white",
    width=15,
    command=open_checklist
)
check_btn.pack(pady=5)

exit_btn = tk.Button(
    root,
    text="Exit",
    bg="red",
    fg="white",
    width=15,
    command=root.quit
)
exit_btn.pack(pady=10)

root.mainloop()
