from PIL import Image, ImageDraw

# Load the certificate template
img = Image.open("XYZ (1).png")

# Create a drawing context
draw = ImageDraw.Draw(img)

# Draw a red rectangle at a sample position (for testing)
name_position = (500, 600)  # Adjust this based on where you want to place the name
draw.rectangle([name_position, (name_position[0] + 200, name_position[1] + 50)], outline="red", width=3)

# Save or display the image to see the rectangle
img.show()  # This opens the image for you to visually inspect
img.save("certificate_with_rectangle.png")
