import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x300")

# Create a treeview widget  

tree = ttk.Treeview(root)

# Define the columns

tree["columns"] = ("one", "two", "three")

# Set the column headings

tree.column("#0", width=0, stretch=tk.NO)

tree.column("one", anchor=tk.CENTER, width=80)

tree.column("two", anchor=tk.CENTER, width=80)

tree.column("three", anchor=tk.CENTER, width=80)

# Create the headings

tree.heading("#0", text="", anchor=tk.CENTER)

tree.heading("one", text="Name", anchor=tk.CENTER)

tree.heading("one", text="Name", anchor=tk.CENTER)

tree.heading("two", text="Age", anchor=tk.CENTER)

tree.heading("three", text="Gender", anchor=tk.CENTER)

tree.heading("three", text="Gender", anchor=tk.CENTER)

# Insert data

tree.insert(parent="", index="end", iid=0, text="", values=("John", "25", "Male"))

tree.insert(parent="", index="end", iid=1, text="", values=("one", "two", "three"))

tree.pack()

root.mainloop()