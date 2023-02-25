import tkinter as tk
import qrcode
from PIL import ImageTk, Image

# Create the tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# Create a label for the URL input
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

# Create an entry box for the URL input
url_entry = tk.Entry(root)
url_entry.pack()

# Create a function to generate the QR code and display it
def generate_qr():
    # Get the URL from the entry box
    url = url_entry.get()
    
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Display the QR code in a tkinter window
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img
    
# Create a button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

# Create a label to display the QR code
qr_label = tk.Label(root)
qr_label.pack()

# Start the tkinter mainloop
root.mainloop()
