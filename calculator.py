import tkinter as tk
import math

# Function to handle button clicks (core logic without GUI dependency)
def button_click(value, current):
    return current + value

# Function to calculate the result (core logic without GUI dependency)
def calculate(expression):
    try:
        if '√' in expression:
            # Handle square root operation
            expression = expression.replace('√', 'math.sqrt(') + ')'
        result = eval(expression)  # Use eval to evaluate the expression
        return str(result)
    except Exception:
        return "Error"

# Function to switch to Dark Mode
def set_dark_mode():
    pass  # Dark mode logic (no changes needed for testing)

# Function to switch to Light Mode
def set_light_mode():
    pass  # Light mode logic (no changes needed for testing)

# Create main window with rounded corners (simulate with canvas)
def setup_gui():
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x600")
    root.config(bg='#FFFFFF')  # Set background color

    # Create a Canvas widget to draw a rounded rectangle
    canvas = tk.Canvas(root, width=400, height=600, bg="#FFFFFF", bd=0, highlightthickness=0)
    canvas.grid(row=0, column=0)

    # Draw rounded rectangle (simulating rounded corners)
    canvas.create_oval(10, 10, 40, 40, fill="#FFFFFF", outline="#FFFFFF")  # Top-left corner
    canvas.create_oval(360, 10, 390, 40, fill="#FFFFFF", outline="#FFFFFF")  # Top-right corner
    canvas.create_oval(10, 550, 40, 580, fill="#FFFFFF", outline="#FFFFFF")  # Bottom-left corner
    canvas.create_oval(360, 550, 390, 580, fill="#FFFFFF", outline="#FFFFFF")  # Bottom-right corner
    canvas.create_rectangle(40, 10, 360, 550, fill="#FFFFFF", outline="#FFFFFF", width=0)

    # Create the entry widget (where input will be shown)
    entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg='#FFFFFF', fg='#000000', insertbackground='black', bd=0)
    entry.place(x=40, y=30)

    # Return root, canvas, and entry for further customization
    return root, canvas, entry


# Button Layout and Styles
def create_button(canvas, text, x, y, command=None):
    """Create a rounded button using Canvas"""
    button_radius = 20
    button_width = 60
    button_height = 60

    # Draw a rounded rectangle for the button
    canvas.create_oval(x, y, x + button_width, y + button_height, fill="#e0e0e0", outline="#d0d0d0", width=0)
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), bg="#e0e0e0", bd=0, command=command)
    button.place(x=x + 15, y=y + 15)  # Adjust the position inside the canvas for text center
    return button

# Setup GUI
root, canvas, entry = setup_gui()

# Button layout
buttons = [
    ('7', 100, 100), ('8', 170, 100), ('9', 240, 100), ('/', 310, 100),
    ('4', 100, 170), ('5', 170, 170), ('6', 240, 170), ('*', 310, 170),
    ('1', 100, 240), ('2', 170, 240), ('3', 240, 240), ('-', 310, 240),
    ('0', 100, 310), ('.', 170, 310), ('+', 240, 310), ('=', 310, 310),
    ('√', 100, 380),  # Square root button
]

# Create the buttons with rounded corners
buttons_list = []
for (text, x, y) in buttons:
    if text == "=":
        button = create_button(canvas, text, x, y, command=lambda: calculate(entry.get())) 
    else:
        button = create_button(canvas, text, x, y, command=lambda t=text: button_click(t, entry.get())) 
    buttons_list.append(button)

# Dark mode button
dark_button = tk.Button(root, text="Dark Mode", width=15, height=2, font=("Arial", 14), command=set_dark_mode)
dark_button.place(x=40, y=460)

# Light mode button
light_button = tk.Button(root, text="Light Mode", width=15, height=2, font=("Arial", 14), command=set_light_mode)
light_button.place(x=210, y=460)

# Start the main event loop
root.mainloop()
