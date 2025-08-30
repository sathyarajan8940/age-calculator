import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    dob = entry_dob.get()
    try:
        dob_date = datetime.strptime(dob, "%d-%m-%Y")  # expecting dd-mm-yyyy format
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        messagebox.showinfo("Age Calculator", f"Your Age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Format", "Please enter date in DD-MM-YYYY format.")

# GUI setup
root = tk.Tk()
root.title("Age Calculator")
root.geometry("350x200")
root.resizable(False, False)

# Widgets
label_title = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

label_dob = tk.Label(root, text="Enter DOB (DD-MM-YYYY):", font=("Arial", 12))
label_dob.pack(pady=5)

entry_dob = tk.Entry(root, font=("Arial", 12), justify="center")
entry_dob.pack(pady=5)

btn_calc = tk.Button(root, text="Calculate Age", font=("Arial", 12, "bold"), bg="blue", fg="white", command=calculate_age)
btn_calc.pack(pady=15)

# Run the app
root.mainloop()
