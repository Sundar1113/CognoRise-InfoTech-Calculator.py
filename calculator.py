import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Attractive Calculator")
root.geometry("400x600")

entry = tk.Entry(root, width=16, font=('Arial', 30), bd=10, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 20), command=lambda b=button: on_button_click(b)).grid(row=row_val, column=col_val, pady=5, padx=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text="C", width=5, height=2, font=('Arial', 20), command=clear_entry).grid(row=row_val, column=col_val, pady=5, padx=5)
tk.Button(root, text="AC", width=5, height=2, font=('Arial', 20), command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val + 1, pady=5, padx=5)
tk.Button(root, text="=", width=5, height=2, font=('Arial', 20), command=calculate).grid(row=row_val, column=col_val + 2, pady=5, padx=5)

root.mainloop()
