import tkinter as tk

window = tk.Tk()
window.minsize(width=800, height=500)
window.config(padx=200, pady=100)

labhel = tk.Label(text="Label")
labhel.grid(column=0, row=0)

buttton = tk.Button(text="button")
buttton.grid(column=1, row=1)

new_button = tk.Button(text="NewButton")
new_button.grid(column=2, row=0)

entry = tk.Entry()
entry.grid(column=3, row=3)

window.mainloop()