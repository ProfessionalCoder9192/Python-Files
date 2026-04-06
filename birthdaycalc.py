import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())
        
        today = date.today()
        birth_date = date(y, m, d)
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_label.config(text=f"Present Age: {age} years")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x350")

tk.Label(root, text="Enter Day (1-31):").pack(pady=5)
day_entry = tk.Entry(root)
day_entry.pack()

tk.Label(root, text="Enter Month (1-12):").pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Enter Year (YYYY):").pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack()

calc_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white")
calc_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

root.mainloop()