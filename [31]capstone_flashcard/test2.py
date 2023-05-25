import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Example App")
        self.geometry("300x200")

        # create and add two frames
        self.frame1 = tk.Frame(self)
        self.frame2 = tk.Frame(self)

        #create canvases in frames
        self.canvas1 = tk.Canvas(self.frame1, background="red", width=150, height=50)
        self.canvas2 = tk.Canvas(self.frame2, background="blue", width=150, height=50)
        self.canvas1.pack()
        self.canvas2.pack()

        # create buttons to switch between frames
        self.button1 = tk.Button(text="Go to frame 1", command=self.show_frame1)
        self.button2 = tk.Button(text="Go to frame 2", command=self.show_frame2)
        self.button1.grid(column=0, row=0)
        self.button2.grid(column=1, row=0)

        self.current_frame = self.frame1
        self.frame1.grid(column=0, row=1, sticky="NWES")
        self.frame2.grid(column=0, row=1, sticky="NWES")

    def show_frame1(self):
        self.frame1.tkraise()
        self.current_frame = self.frame1
        print(self.current_frame)
        

    def show_frame2(self):
        self.frame2.tkraise()
        self.current_frame = self.frame2
        print(self.current_frame)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
