import tkinter as tk

def check_strength(*args):
    """Checks the length of the password and updates the label."""
    password = password_var.get()
    length = len(password)
    
    if length == 0:
        result_label.config(text="Strength: ", fg="black")
    elif length < 6:
        result_label.config(text="Strength: Weak", fg="red")
    elif length < 12:
        result_label.config(text="Strength: Medium", fg="orange")
    else:
        result_label.config(text="Strength: Strong", fg="green")

# Initialize the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# Add a label for instructions
tk.Label(root, text="Enter your password below:", font=("Arial", 10)).pack(pady=10)

# Password variable and entry widget
password_var = tk.StringVar()
# The 'trace_add' method calls check_strength every time the text changes
password_var.trace_add("write", check_strength)

password_entry = tk.Entry(root, textvariable=password_var, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

# Label to display the strength result
result_label = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

# Start the application
root.mainloop()