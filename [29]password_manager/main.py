import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import pyperclip
import json
import sys
from os import path
# ---------------------------------- CONSTANTS -----------------------------------#
BLUE = "#132640"
PINK = "#F2BBE3"
PURPLE = "#8C84BF"
FONT = "Early GameBoy"
FONT_ALSO = "Dogica"

# ----------------------------- IMPOTANT FUNCTIONS -------------------------------#
def path_correction_somethinf(relative_path):
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.abspath(path.join(base_path, relative_path))

# ----------------------------- PASSWORD GENERATOR -------------------------------#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0, tk.END)
    pass_entry.insert(0, password)

    pyperclip.copy(password)


# -------------------------------- SAVE PASSWORD ---------------------------------#

def save():
    website = website_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) > 0 or len(username) > 0 or len(password) >0:
        okie = messagebox.askokcancel(title="CONFIRMATION", message=f"The credentials entered are as follows:\nUsername: {username}\nPassword: {password}\nAre you sure you want to save these?")
        if okie:
            try:
                with open("data.json", "r") as data:
                    data = json.load(data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, tk.END)
                user_entry.delete(0, tk.END)
                pass_entry.delete(0, tk.END)
    else:
        messagebox.showerror(title="error 404", message="You have left the entries blank.\nPlease fill all the fields to procede!")


# -------------------------------- FIND PASSWORD ---------------------------------#

def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="error 069", message="No Data File Found!")
    else:
        search = website_entry.get()
        try:
            email = data[search]["email"]
            password = data[search]["password"]
        except KeyError:
            if search != "":
                messagebox.showerror(title="error 007", message=f"No Details for {search} exist!")
            else:
                messagebox.showerror(title="error 404", message=f"You have left the website field empty!\nPlease fill it to procede.")
                
        else:
            messagebox.showinfo(title=f"{search}", message=f"email: {email}\npassword: {password}")
            pyperclip.copy(password)

# ---------------------------------- UI SETUP ------------------------------------#

screen = tk.Tk()
screen.title("LowKeyPurr")
screen.config(padx=40, pady=40, bg=BLUE)
logo = tk.PhotoImage(file="another_logo_2.png")
screen.iconphoto(False, logo)

canvas = tk.Canvas(width=444, height=444, bg=BLUE, highlightthickness=0)
canvas.create_image(230, 222, image=logo)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website~", font=(FONT, 17), fg=PINK, bg=BLUE)
website_label.grid(row=1, column=0)

user_label = tk.Label(text="Username~", font=(FONT, 17), fg=PINK, bg=BLUE)
user_label.grid(row=2, column=0)

pass_label = tk.Label(text="Password~", font=(FONT, 17), fg=PINK, bg=BLUE)
pass_label.grid(row=3, column=0)

website_entry = tk.Entry(width=27, font=(FONT_ALSO, 12),foreground=PINK,background=BLUE)
website_entry.grid(row=1, column=1, sticky="W")
website_entry.focus()

user_entry = tk.Entry(width=42, font=(FONT_ALSO, 12),fg=PINK,bg=BLUE)
user_entry.grid(row=2, column=1, columnspan=2)

search_button = tk.Button(text="Search", width=17,font=(FONT, 10), fg=PURPLE, bg=BLUE, command=find_password)
search_button.grid(row=1, column=2)

pass_entry = tk.Entry(width=27, font=(FONT_ALSO, 12),fg=PINK,bg=BLUE)
pass_entry.grid(row=3, column=1, sticky="W")

generate_button = tk.Button(text="Generate Password", width=17,font=(FONT, 10), fg=PURPLE, bg=BLUE, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", font=(FONT, 10), fg=PURPLE, bg=BLUE, width=51, command=save)
add_button.grid(row=4, column=1, columnspan=2)


screen.mainloop()