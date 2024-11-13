from PIL import Image, ImageTk
import tkinter as tk

# Function to capture mouse click coordinates
def get_coordinates(event):
    print(f"Mouse clicked at: {event.x}, {event.y}")

# Open image using Pillow
img = Image.open("XYZ (1).png")

# Convert the image to something Tkinter can display
root = tk.Tk()
img_tk = ImageTk.PhotoImage(img)

# Create a label with the image
label = tk.Label(root, image=img_tk)
label.pack()

# Bind the click event to the label
label.bind("<Button-1>", get_coordinates)

# Start the Tkinter event loop
root.mainloop()