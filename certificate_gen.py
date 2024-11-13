import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Function to calculate the center position
def calculate_center(text, font, image_width, image_height):
    # Get the bounding box of the text
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]  # Width of the text
    text_height = bbox[3] - bbox[1]  # Height of the text
    x = (image_width - text_width) // 2  # Center the text horizontally
    y = (image_height - text_height) // 2  # Center the text vertically
    return x, y

# Path to save the certificates
output_folder = r"D:\student clubs\ISSA\Email Automation\React&Roll_Certificates"  # Define the folder where the PDFs will be saved
os.makedirs(output_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Load participant names from Excel
excel_path = "React & Roll Participants - ISSA NIE.xlsx"  # Path to your Excel file
df = pd.read_excel(excel_path)
participants = df['Name'].tolist()  # Assuming the column name is 'Name'

# Load a font
font_path = "Tinos-Italic.ttf"  # Path to your font file
font_size = 80  # Adjust the font size based on your template
font = ImageFont.truetype(font_path, font_size)

# Loop through participants and create a certificate for each
for name in participants:
    # Load the certificate template again for each participant (so each one is saved separately)
    img = Image.open("XYZ (1).png")
    image_width, image_height = img.size

    # Create drawing context
    draw = ImageDraw.Draw(img)

    # Get the center position for the name
    x, y = calculate_center(name, font, image_width, image_height)

    # Add the name to the certificate (change text color if needed)
    draw.text((x, y), name, fill="black", font=font)

    # Construct the path to save the PDF in the output folder
    pdf_path = os.path.join(output_folder, f"{name}_certificate.pdf")
    
    # Save the personalized certificate as a PDF in the specified folder
    img.save(pdf_path, "PDF", resolution=100.0)  # Save as PDF with 100 DPI
    print(f"Certificate for {name} saved as PDF at {pdf_path}!")

# Optionally, show the image to verify
# img.show()
