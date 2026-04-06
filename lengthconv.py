import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        result_label.config(text=f"Centimeters: {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

window = tk.Tk()
window.title("Inches to CM Converter")
window.geometry("350x250")

label_title = tk.Label(window, text="Inches to Centimeters", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

label_prompt = tk.Label(window, text="Enter length in inches:")
label_prompt.pack()

entry_inches = tk.Entry(window)
entry_inches.pack(pady=5)

btn_convert = tk.Button(window, text="Convert", command=convert, bg="blue", fg="white")
btn_convert.pack(pady=15)

result_label = tk.Label(window, text="Centimeters: ", font=("Arial", 12))
result_label.pack()

window.mainloop()
