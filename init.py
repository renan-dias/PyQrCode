# Imports
import pyqrcode
import tkinter as tk

from tkinter import messagebox
from tkinter import filedialog

from PIL import Image

# Variables
link = input("Enter your link here: ")
qr_code = pyqrcode.create(link)

# Functions
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

qr_code.png("QRCodes/QRCode.png", scale=5)
Image.open("QRCodes/QRCode.png")