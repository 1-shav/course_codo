import tkinter as tk
from tkinter import ttk
import pandas as pd
from random import choice

# ---------------------------------- CONSTANTS -----------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
BLACK_SOMETHINF = "#1B1E23"
OFF_WHITE = "#FAF9F6"

# ---------------------------------- UI SETUP ------------------------------------#

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.root = tk.Tk("FlashyCards")
        self.configure(bg=BACKGROUND_COLOR, padx=30, pady=20)
        self.title("FlashyCards")
        self.geometry("600x500+500+250")

        #--------------------------------------english_frame_related--------------------------------#

        self.eng_frame = tk.Frame(self)
        
        self.eng_canvas = tk.Canvas(self.eng_frame, bg=BACKGROUND_COLOR, width=540, height=360, highlightthickness=0)

        self.card_eng = tk.PhotoImage(file="code_py/[31]capstone_flashcard/images/card_back_re.png")
        self.eng_canvas.create_image(270, 180, image=self.card_eng)
        self.eng_canvas.create_text(263, 99, text="ENGLISH", font=("Brass Mono", 20, "italic"), fill=OFF_WHITE)
        self.english_text = self.eng_canvas.create_text(263, 170, text="word", font=("Ariel", 47, "bold"), fill=OFF_WHITE)
        self.eng_canvas.pack()
        
        
        self.eng_frame.grid(column=0, row=0, columnspan=2)

        #----------------------------------french_frame_related------------------------------------#

        self.fre_frame = tk.Frame(self)

        self.fre_canvas = tk.Canvas(self.fre_frame, bg=BACKGROUND_COLOR, width=540, height=360, highlightthickness=0)

        self.card_fre = tk.PhotoImage(file="code_py/[31]capstone_flashcard/images/card_front_re.png")
        self.fre_canvas.create_image(270, 180, image=self.card_fre)
        self.fre_canvas.create_text(263, 99, text="FRENCH", font=("Brass Mono", 20, "italic") ,fill=BLACK_SOMETHINF)
        self.french_text = self.fre_canvas.create_text(263, 170, text="word", font=("Ariel", 47, "bold"), fill=BLACK_SOMETHINF)
        self.fre_canvas.pack()

        self.fre_frame.grid(column=0, row=0, columnspan=2)




        #-----------------------------------button_related----------------------------------------------#

        self.right_image = tk.PhotoImage(file="code_py/[31]capstone_flashcard/images/right_ree.png")
        self.wrong_image = tk.PhotoImage(file="code_py/[31]capstone_flashcard/images/wrong_ree.png")

        self.right_button = tk.Button(image=self.right_image,borderwidth=0, highlightthickness=0, command=self.he_knows)
        self.right_button.grid(column=0, row=1)

        self.wrong_button = tk.Button(image=self.wrong_image, borderwidth=0, highlightthickness=0, command=self.hes_dumb)
        self.wrong_button.grid(column=1, row=1)

        #------------------------------------important_ig-----------------------------------#
        
        try:
            with open(file="code_py/[31]capstone_flashcard/data/words_to_learn.csv") as data:
                data = pd.read_csv(data)
        except FileNotFoundError:
            with open(file="code_py/[31]capstone_flashcard/data/french_words.csv") as data:
                data = pd.read_csv(data)
        self.data_pairs = data.to_dict(orient="records")

        self.current_frame = self.fre_frame

        self.waiter = self.after(3000, self.upar_niche)

        self.refresh_word()

    #---------------------------functions-------------------------------#    

    def get_word(self):
        self.current_pair = choice(self.data_pairs)
        french_word = self.current_pair["French"]
        english_word = self.current_pair["English"]
        return french_word, english_word
    
    def he_knows(self):
        self.data_pairs.remove(self.current_pair)
        updated_data = pd.DataFrame(self.data_pairs)
        print(updated_data)
        with open(file="code_py/[31]capstone_flashcard/data/words_to_learn.csv", mode="w") as new_data_file:
            updated_data.to_csv(new_data_file, index=False)
        self.refresh_word()

    def hes_dumb(self):
        self.refresh_word()

    def refresh_word(self):
        french_word, english_word = self.get_word()
        self.fre_canvas.itemconfig(self.french_text, text=french_word)
        self.eng_canvas.itemconfig(self.english_text, text=english_word)
        self.next_card()

    def next_card(self):
        self.after_cancel(self.waiter)
        self.current_frame = self.fre_frame
        self.fre_frame.tkraise()
        self.waiter = self.after(3000, self.upar_niche)

    def upar_niche(self):
        self.current_frame = self.eng_frame
        self.eng_frame.tkraise()



            


if __name__ == "__main__":
    application = App()
    application.mainloop()        






"""
screen = tk.Tk()
screen.title("flash-card")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=526, height=346, bg=BACKGROUND_COLOR, highlightthickness=0)
card_fre = tk.PhotoImage(file="./code_py/flash-card-project-start/images/card_fre_re.png")
card_eng = tk.PhotoImage(file="./code_py/flash-card-project-start/images/card_eng_re.png")
canvas.create_image(263, 172, image=card_eng)
canvas.create_text(263, 172, text="Hello World", font=("Dogica", 20))
canvas.grid(row=0, column=0, columnspan=2)
screen.mainloop()
"""