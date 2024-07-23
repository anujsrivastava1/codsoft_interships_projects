import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        result_var.set(result)
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Select operation:").grid(row=2, column=0)
operation_var = tk.StringVar(value='+')
tk.OptionMenu(root, operation_var, '+', '-', '*', '/').grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Result:").grid(row=4, column=0)
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state='readonly').grid(row=4, column=1)

# Run the application
root.mainloop()
