import numpy as np
import tkinter as tk
from tkinter import messagebox, filedialog

students = []
marks = []

# -------- ADD STUDENT --------
def add_student():
    name = name_entry.get()
    mark = mark_entry.get()

    if not name or not mark:
        messagebox.showerror("Error", "Enter both name and marks")
        return

    try:
        mark = float(mark)
    except:
        messagebox.showerror("Error", "Marks must be a number")
        return

    students.append(name)
    marks.append(mark)

    listbox.insert(tk.END, f"{name:<15} | {mark}")

    name_entry.delete(0, tk.END)
    mark_entry.delete(0, tk.END)


# -------- DELETE STUDENT --------
def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Select a student to delete")
        return

    index = selected[0]
    listbox.delete(index)
    students.pop(index)
    marks.pop(index)


# -------- CALCULATE --------
def calculate():
    if not marks:
        messagebox.showerror("Error", "No data entered")
        return

    arr = np.array(marks)

    avg = np.mean(arr)
    high = np.max(arr)
    low = np.min(arr)

    def grade(m):
        if m >= 90: return "A"
        elif m >= 75: return "B"
        elif m >= 60: return "C"
        else: return "D"

    result_text = "Name           | Marks | Grade\n"
    result_text += "-"*35 + "\n"

    for i in range(len(students)):
        result_text += f"{students[i]:<15} | {marks[i]:<5} | {grade(marks[i])}\n"

    result_text += "\n"
    result_text += f"Average: {avg:.2f}\nHighest: {high}\nLowest: {low}"

    result_label.config(text=result_text)


# -------- SAVE REPORT --------
def save_report():
    if not marks:
        messagebox.showerror("Error", "No data to save")
        return

    file = filedialog.asksaveasfilename(defaultextension=".txt")

    if file:
        with open(file, "w") as f:
            f.write(result_label.cget("text"))
        messagebox.showinfo("Success", "Report saved!")


# -------- UI --------
root = tk.Tk()
root.title("Student Marks Analyzer Pro")
root.geometry("500x600")
root.config(bg="#1e1e1e")

# Title
tk.Label(root, text="Student Marks Analyzer", 
         font=("Arial", 16, "bold"), 
         bg="#1e1e1e", fg="white").pack(pady=10)

# Input frame
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

tk.Label(frame, text="Name", bg="#1e1e1e", fg="white").grid(row=0, column=0)
tk.Label(frame, text="Marks", bg="#1e1e1e", fg="white").grid(row=0, column=1)

name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=0, padx=5)

mark_entry = tk.Entry(frame)
mark_entry.grid(row=1, column=1, padx=5)

# Buttons
tk.Button(root, text="Add Student", command=add_student, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_student, bg="#f44336", fg="white").pack(pady=5)

# Listbox + Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
listbox.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=listbox.yview)

# Actions
tk.Button(root, text="Calculate Result", command=calculate, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="Save Report", command=save_report, bg="#9C27B0", fg="white").pack(pady=5)

# Result display
result_label = tk.Label(root, text="", justify="left", bg="#1e1e1e", fg="white")
result_label.pack(pady=10)

root.mainloop()