import tkinter as tk
from tkinter import messagebox


def calculate_interest():
    try:
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())

        si = (principal * time * rate) / 100

        ci = principal * (pow((1 + rate / 100), time)) - principal

        label_si_result.config(text=f"Simple Interest: {si:.2f}")
        label_ci_result.config(text=f"Compound Interest: {ci:.2f}")

    except ValueError:
        messagebox.showerror(
            "Invalid Input", "Please enter valid numerical values."
        )


def clear_fields():
    entry_principal.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    label_si_result.config(text="Simple Interest: -")
    label_ci_result.config(text="Compound Interest: -")


root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x350")
root.resizable(False, False)

padding_options = {"padx": 10, "pady": 8}

title_label = tk.Label(
    root, text="Simple Interest & Compound Interest Calculator", font=("Helvetica", 16, "bold")
)
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Principal Amount:", font=("Helvetica", 10)).grid(
    row=0, column=0, sticky="w", **padding_options
)
entry_principal = tk.Entry(frame, font=("Helvetica", 10))
entry_principal.grid(row=0, column=1, **padding_options)

tk.Label(frame, text="Time Period (Years):", font=("Helvetica", 10)).grid(
    row=1, column=0, sticky="w", **padding_options
)
entry_time = tk.Entry(frame, font=("Helvetica", 10))
entry_time.grid(row=1, column=1, **padding_options)

tk.Label(frame, text="Rate of Interest (%):", font=("Helvetica", 10)).grid(
    row=2, column=0, sticky="w", **padding_options
)
entry_rate = tk.Entry(frame, font=("Helvetica", 10))
entry_rate.grid(row=2, column=1, **padding_options)

label_si_result = tk.Label(
    root,
    text="Simple Interest: -",
    font=("Helvetica", 11, "bold"),
    fg="green",
)
label_si_result.pack(pady=5)

label_ci_result = tk.Label(
    root,
    text="Compound Interest: -",
    font=("Helvetica", 11, "bold"),
    fg="blue",
)
label_ci_result.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

btn_calculate = tk.Button(
    button_frame,
    text="Calculate",
    font=("Helvetica", 10, "bold"),
    bg="#4CAF50",
    fg="white",
    width=10,
    command=calculate_interest,
)
btn_calculate.pack(side="left", padx=10)

btn_clear = tk.Button(
    button_frame,
    text="Clear",
    font=("Helvetica", 10, "bold"),
    bg="#f44336",
    fg="white",
    width=10,
    command=clear_fields,
)
btn_clear.pack(side="left", padx=10)

root.mainloop()
