import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_qr_code():
    # Get the file path from the user
    filepath = filedialog.askopenfilename(title="Select a File")
    
    if not filepath:
        messagebox.showerror("Error", "No file selected.")
        return
    
    # Open the file and read its contents
    with open(filepath, "rb") as f:
        file_contents = f.read()
    
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(file_contents)
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
