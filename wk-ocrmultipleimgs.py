import subprocess
import pytesseract
import cv2

# Best practice: Specify Tesseract executable path if not in standard locations
# pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

def print_ocr_text(input_image_paths):
    for input_image_path in input_image_paths:
        # Load the image
        image = cv2.imread(input_image_path)

        # Perform OCR using Pytesseract (prioritizing Spanish)
        text = pytesseract.image_to_string(image, lang='spa+eng')

        # Print the extracted text
        print(f"OCR Results for {input_image_path}:")
        print(text)
        print("-" * 50)  # Separator between results of different images

# Replace with the paths to your images
input_image_paths = [
    r"C:\Users\david\Downloads\Libro\2 eremophiluis cc244538-00dd-49e7-960b-61fb0ca903bc.png",
    r"C:\Users\david\Downloads\Libro\3A PYGIDIUM 7dfd4083-f1a7-483b-a5ee-e1b5d18b3a44.png",
    r"C:\Users\david\Downloads\Libro\3B PYGIDIUM 1576dd76-4125-451f-810c-d5ae982c9292.png",
    r"C:\Users\david\Downloads\Libro\4 otro capitulo cc280cd9-93a6-4732-8755-220461352364.png",
    r"C:\Users\david\Downloads\Libro\5 Posfacio29fa2b22-d96c-4a98-b6f4-2ae570b8b71a.png",
    # Add as many image paths as you need
]

# Perform OCR and print results for each image
print_ocr_text(input_image_paths)