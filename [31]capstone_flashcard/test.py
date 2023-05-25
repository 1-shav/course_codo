import tkinter as tk

class FlashcardApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set up the frames
        front_frame = tk.Frame(self)
        front_frame.pack(side="top", fill="both", expand=True)
        back_frame = tk.Frame(self)
        back_frame.pack(side="top", fill="both", expand=True)

        # add widgets to the front frame
        front_label = tk.Label(front_frame, text="Front of the card", font=("Arial", 24))
        front_label.pack(side="top", fill="both", expand=True)

        # add widgets to the back frame
        back_label = tk.Label(back_frame, text="Back of the card", font=("Arial", 24))
        back_label.pack(side="top", fill="both", expand=True)

        # bind the flip function to a mouse click on the front frame
        button = tk.Button(text="flip", command=lambda: self.flip_card(front_frame, back_frame))
        button.pack(side="bottom")

        # set the current frame to the front frame
        self.current_frame = front_frame

    def flip_card(self, front_frame, back_frame):
        if self.current_frame == front_frame:
            self.current_frame = back_frame
        else:
            self.current_frame = front_frame
        self.current_frame.tkraise()
        print(self.current_frame)

app = FlashcardApp()
app.mainloop()
