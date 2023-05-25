import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()
window.title("Miles to Kilometers Converter")

def convert():
    # Get the value entered in the input field
    miles = float(input_field.get())
    
    # Convert the value from miles to kilometers
    kilometers = miles * 1.60934
    
    # Set the result label to the converted value
    result_label.config(text=f"{kilometers:.2f} kilometers")

# Create an input field for the user to enter a value in miles
input_field = tk.Entry(window)
input_field.pack()

# Create a button that will call the convert function when clicked
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

# Create a label to display the result of the conversion
result_label = tk.Label(window)
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
