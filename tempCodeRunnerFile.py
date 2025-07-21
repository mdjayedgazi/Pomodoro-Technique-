from tkinter import *

root = Tk()
root.geometry("400x200")  # Set window size

# Add spacing or widgets above (optional)
Label(root, text="Your App Title").grid(row=0, column=1, pady=20)

# Start Button on bottom-left
start_btn = Button(root, text="Start")
start_btn.grid(row=2, column=0, sticky="w", padx=10, pady=10)

# Reset Button on bottom-right
reset_btn = Button(root, text="Reset")
reset_btn.grid(row=2, column=5, sticky="e", padx=20, pady=10)

# Optional: Add a blank Label in the center (to push buttons to sides)
Label(root, text="").grid(row=2, column=1)

root.mainloop()
