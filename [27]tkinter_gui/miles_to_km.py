import tkinter as tk

khidki = tk.Tk()
khidki.title("Miles To Km")
khidki.minsize(width=300, height=150)
khidki.config(padx=50, pady=35)

inputational = tk.Entry()
inputational.insert(tk.END, "0")
inputational.config(width=10)
inputational.grid(row=0, column=1)

miles_morales = tk.Label(text="Miles", padx=7, pady=5)
miles_morales.grid(row=0, column=2)

labhel = tk.Label(text="is equal to", padx=7, pady=2)
labhel.grid(row=1, column=0)

km_morales = tk.Label(text="0", padx=5, pady=2)
km_morales.grid(row=1, column=1)

labhel2 = tk.Label(text="Km", padx=5, pady=2)
labhel2.grid(row=1, column=2)

def convert():
    km_morales.config(text=f"{int(inputational.get()) * 1.60934}")

khatka = tk.Button(text="Calculate", command=convert)
khatka.grid(row=2, column=1)


khidki.mainloop()