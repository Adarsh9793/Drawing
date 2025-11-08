

# Step 1: Import tkinter
from tkinter import *

# Step 2: Create the main window
window = Tk()
window.title("Canvas Line Example")  # Optional: Set window title
window.geometry("500x500")           # Optional: Set window size

# Step 3: Add a Canvas widget
canvas = Canvas(window, width=500, height=500, bg="white")
canvas.pack()

# Step 4: Draw a dashed red line from top-left to bottom-right
canvas.create_line(0, 0, 500, 500, fill="black", dash=(5, 5), width=2)

# Optional: Add another line for contrast
canvas.create_line(0, 500, 500, 0, fill="blue", dash=(10, 5), width=2)

# Step 5: Run the GUI loop
window.mainloop()