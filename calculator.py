import tkinter as tk
import math  # Importing the math module for square root function

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        # Check if there's a square root symbol in the entry, and handle it
        expression = entry.get()
        # Replace the square root symbol with math.sqrt() for calculation
        if '√' in expression:
            expression = expression.replace('√', 'math.sqrt(') + ')'
        
        result = eval(expression)  # Use eval to evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to switch to Dark Mode
def set_dark_mode():
    root.tk_setPalette(background='#2E2E2E', foreground='#FFFFFF')
    entry.config(bg='#2E2E2E', fg='#FFFFFF', insertbackground='white')
    for button in buttons_list:
        button.config(bg='#4A4A4A', fg='#FFFFFF', activebackground='#6A6A6A')
    dark_button.config(bg='#6A6A6A', fg='#FFFFFF')
    light_button.config(bg='#E0E0E0', fg='#000000')

# Function to switch to Light Mode
def set_light_mode():
    root.tk_setPalette(background='#FFFFFF', foreground='#000000')
    entry.config(bg='#FFFFFF', fg='#000000', insertbackground='black')
    for button in buttons_list:
        button.config(bg='#E0E0E0', fg='#000000', activebackground='#D0D0D0')
    light_button.config(bg='#D0D0D0', fg='#000000')
    dark_button.config(bg='#4A4A4A', fg='#FFFFFF')

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Create the entry widget (where input will be shown)
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg='#FFFFFF', fg='#000000', insertbackground='black')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('√', 5, 0),  # Square root button
]

# Create and place the buttons
buttons_list = []
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: button_click(t))
    
    button.grid(row=row, column=col)
    buttons_list.append(button)

# Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=2, columnspan=2)

# Dark mode button
dark_button = tk.Button(root, text="Dark Mode", width=15, height=2, font=("Arial", 14), command=set_dark_mode)
dark_button.grid(row=6, column=0, columnspan=2)

# Light mode button
light_button = tk.Button(root, text="Light Mode", width=15, height=2, font=("Arial", 14), command=set_light_mode)
light_button.grid(row=6, column=2, columnspan=2)

# Set initial theme to light mode
set_light_mode()

# Start the main event loop
root.mainloop()
