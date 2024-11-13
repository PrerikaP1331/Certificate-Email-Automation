import os
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email credentials (use college club's official email and password)
sender_email = " issa_chapter@nie.ac.in "
sender_password = "nisc2020better"

# SMTP server settings
smtp_server = "smtp.gmail.com"  # Update if your college uses a different SMTP provider
smtp_port = 587

# Path to the Excel file and certificates folder
excel_file = "React & Roll Participants - ISSA NIE.xlsx"
certificates_folder = "React&Roll_Certificates"

# Read the Excel file
participants = pd.read_excel(excel_file)

# Function to send an email with an attached certificate
def send_certificate(recipient_email, recipient_name, certificate_path):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = "Certificate of Participation - React & Roll!(06.Nov.24)"

        # Email body text
        body = f"""Dear {recipient_name},

        Thank you for your participation in the React & Roll event! 
        We hope it has sparked your interest to further explore the exciting field of web development.

        To help you continue your learning journey, additional resources have been shared in the ISSA Club’s WhatsApp group. 
        Join the group to stay connected and access more materials:

        ISSA Community on WhatsApp: https://chat.whatsapp.com/FtWdILJgPtx5pNxXEh8t2v

        Best regards,  
        Team ISSA."""
        msg.attach(MIMEText(body, "plain"))
        msg["Content-Type"] = "text/plain; charset=UTF-8"  # Optional: explicitly set the content type

        # Attach the certificate PDF
        with open(certificate_path, "rb") as f:
            part = MIMEApplication(f.read(), _subtype="pdf")
            part.add_header("Content-Disposition", "attachment", filename=f"{recipient_name}_certificate.pdf")
            msg.attach(part)

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS for security
            server.login(sender_email, sender_password)  # Direct login with main password
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Certificate sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send certificate to {recipient_email}: {e}")

# Loop through each participant in the Excel file
for index, row in participants.iterrows():
    name = row["Name"]  # Adjust column names as per your Excel
    email = row["Email"]
    certificate_path = os.path.join(certificates_folder, f"{name}_certificate.pdf")

    # Check if the certificate file exists before sending
    if os.path.exists(certificate_path):
        send_certificate(email, name, certificate_path)
    else:
        print(f"Certificate for {name} not found at {certificate_path}")
