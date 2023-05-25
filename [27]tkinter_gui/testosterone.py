import tkinter as tk

khidki = tk.Tk()

khidki.title("testis")
khidki.minsize(width=800, height=500)

labhel = tk.Label(text="we can write boisss!", font=("Amatic Sc", 30, "italic"))
labhel.pack()

khatka = tk.Button(text="uhm")
khatka.pack()

dabba = tk.Entry()
dabba.pack()
dabba.insert(5, "whatcha doing boi")

chithi = tk.Text(height=3, width=45)
chithi.pack()
chithi.focus()
chithi.insert(tk.END, "HA ye likha hua hai pehle se")

spinni_boi = tk.Spinbox(from_=7, to=15, width=2)
spinni_boi.pack()

paimaana = tk.Scale(from_=7, to=56)


def khatka_daba_kya():
    labhel["text"] = chithi.get("1.0", tk.END)

def spin_kra_gya():
    print(spinni_boi.get())

khatka["command"] = khatka_daba_kya
spinni_boi["command"] = spin_kra_gya

khidki.mainloop()