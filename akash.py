import os
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def get_credentials():
    # Set up the Google Drive API credentials
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def upload_to_drive(file_path):
    # Set up the Google Drive API service
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)
    
    # Upload the file to Google Drive
    file_metadata = {"name": os.path.basename(file_path)}
    media = {"body": open(file_path, "rb")}
    file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    
    # Get the link to the uploaded file
    link = f"https://drive.google.com/uc?id={file['id']}"
    return link


def generate_qr_code():
    # Get the file path from the user
    filepath = filedialog.askopenfilename(title="Select a File")
    
    if not filepath:
        messagebox.showerror("Error", "No file selected.")
        return
    
    # Upload the file to Google Drive
    link = upload_to_drive(filepath)
    
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Display the QR code
    img.show()


# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create a button to select a file
file_button = tk.Button(root, text="Select a File", command=generate_qr_code)
file_button.pack()

# Run the main loop
root.mainloop()
