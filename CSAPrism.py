import tkinter as tk
from tkinter import messagebox

# Function to calculate the area of the triangular base
def calculate_area ():
    try:
        # Get values from the input fields
        base = float(base_entry.get())
        height = float(height_entry.get())
        
        # Validate inputs
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")

        # Calculate area of the triangular base
        area = 0.5 * base * height
        result_label.config(text=f"Base Area: {area} square units")

        # Store the area and base height to calculate volume later
        global base_area
        base_area = area

    except ValueError as ve:
        messagebox.showerror("Input Error", f"Invalid input: {ve}")

# Create the main window
root = tk.Tk()
root.title("Triangular Prism Calculator")
root.geometry("400x200")

# Add labels and input fields for the base and height of the triangle
base_label = tk.Label(root, text="Enter Base of Triangle (in units):")
base_label.grid(row=0, column=0, padx=10, pady=10)

base_entry = tk.Entry(root)
base_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Enter Height of Triangle (in units):")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# Add button to calculate the base area
calculate_button = tk.Button(root, text="Calculate Base Area", command=calculate_area)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Label to display the base area
result_label = tk.Label(root, text="Base Area: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
