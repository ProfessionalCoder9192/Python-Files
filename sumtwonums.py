import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x250")

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=20)

result_label = tk.Label(root, text="Product: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()

