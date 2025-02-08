import tkinter as tk
from math import sin, cos, tan, log, log10, sqrt, factorial, exp, pi, e, radians, degrees
from tkinter import messagebox

# Function definitions
def click_button(value):
    current = display.get()
    if value == "C":
        display.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif value == "del":
        display.delete(len(current)-1, tk.END)
    elif value in ["sin", "cos", "tan", "log", "ln", "sqrt", "n!", "deg", "rad"]:
        try:
            if value == "sin":
                result = sin(radians(float(current)))
            elif value == "cos":
                result = cos(radians(float(current)))
            elif value == "tan":
                result = tan(radians(float(current)))
            elif value == "log":
                result = log10(float(current))
            elif value == "ln":
                result = log(float(current))
            elif value == "sqrt":
                result = sqrt(float(current))
            elif value == "n!":
                result = factorial(int(current))
            elif value == "deg":
                result = degrees(float(current))
            elif value == "rad":
                result = radians(float(current))
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    else:
        display.insert(tk.END, value)

# GUI Setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("600x800")
root.resizable(False, False)
root.config(bg="#ffffff")

# Display field
display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief=tk.FLAT, justify=tk.RIGHT, bg="#f9f9f9")
display.grid(row=0, column=0, columnspan=5, pady=20, padx=20, ipady=10)

# Button layout
buttons = [
    ["2^", "pi", "e", "C", "del"],
    ["x^2", "1/x", "|x|", "exp", "mod"],
    ["sqrt", "(", ")", "n!", "/"],
    ["x^y", "7", "8", "9", "*"],
    ["10^", "4", "5", "6", "-"],
    ["log", "1", "2", "3", "+"],
    ["ln", "+/-", "0", ".", "="]
]

# Button placement
for r, row in enumerate(buttons):
    for c, btn_text in enumerate(row):
        if btn_text == "C":
            color = "#ff4d4d"
        elif btn_text == "=":
            color = "#b71c1c"
        else:
            color = "#f0f0f0"

        tk.Button(root, text=btn_text, font=("Arial", 16), bg=color, fg="black",
                  width=6, height=2, command=lambda b=btn_text: click_button(b)).grid(row=r+1, column=c, padx=5, pady=5)

# Add a frame for extra functions like trigonometry
extra_frame = tk.Frame(root, bg="#ffffff")
extra_frame.grid(row=len(buttons)+1, column=0, columnspan=5, pady=10)

extra_buttons = ["sin", "cos", "tan", "deg", "rad"]
for i, btn_text in enumerate(extra_buttons):
    tk.Button(extra_frame, text=btn_text, font=("Arial", 14), bg="#d9d9d9", fg="black",
              width=10, height=2, command=lambda b=btn_text: click_button(b)).grid(row=0, column=i, padx=5, pady=5)

# Run the GUI
root.mainloop()
