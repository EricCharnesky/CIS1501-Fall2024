# https://umgpt.umich.edu/
# 1 - create an example tkinter program with a button that displays hello world when clicked
# 2 - add a text box the user can type in, and set the label to the text entered

import tkinter as tk

def on_button_click():
    # Get the text from the entry widget
    user_input = entry.get()
    # Set the label text to the user input
    label.config(text=user_input)

# Create the main window
window = tk.Tk()
window.title("Update Label Program")

# Create an entry widget for user input
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Create a label that will display messages
label = tk.Label(window, text="")
label.pack(pady=10)

# Create a button that will trigger the on_button_click function when clicked
button = tk.Button(window, text="Submit", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()