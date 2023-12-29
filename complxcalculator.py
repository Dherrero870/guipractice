import tkinter as tk
import math

def on_button_click(value):
    current_input = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_input + value)

def on_clear():
    entry.delete(0, tk.END)

def on_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def apply_function(func):
    try:
        result = func(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("Advanced Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14), command=lambda value=button: on_button_click(value) if value != '=' else on_equal()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='sin', padx=20, pady=20, font=('Arial', 14), command=lambda: apply_function(math.sin)).grid(row=row_val, column=col_val)
col_val += 1
tk.Button(root, text='cos', padx=20, pady=20, font=('Arial', 14), command=lambda: apply_function(math.cos)).grid(row=row_val, column=col_val)
col_val += 1
tk.Button(root, text='sqrt', padx=20, pady=20, font=('Arial', 14), command=lambda: apply_function(math.sqrt)).grid(row=row_val, column=col_val)
col_val += 1
tk.Button(root, text='log', padx=20, pady=20, font=('Arial', 14), command=lambda: apply_function(math.log)).grid(row=row_val, column=col_val)

tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=on_clear).grid(row=row_val, column=col_val+1, columnspan=3)
root.mainloop()