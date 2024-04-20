import cv2
import tkinter as tk
from tkinter import filedialog

def convert_image():
    input_path = filedialog.askopenfilename()

    if not input_path:
        return
    
    output_path = filedialog.asksaveasfilename(defaultextension="", filetypes=[("PNG files ","*.png"), ("JPEG files", "*.jpg")])

    if not output_path:
        return
    
    image = cv2.imread(input_path)
    cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

root = tk.Tk()
root.title("Change format")

convert_button = tk.Button(root, text="Change format", command=convert_image)
convert_button.pack(pady=10)

root.mainloop()