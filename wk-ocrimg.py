import subprocess
import pytesseract
import cv2

# Best practice: Specify Tesseract executable path if not in standard locations
#pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

def print_ocr_text(input_image_path):
    # Load the image
    image = cv2.imread(input_image_path)

    # Perform OCR using Pytesseract (prioritizing Spanish)
    text = pytesseract.image_to_string(image, lang='spa+eng')

    # Print the extracted text
    print(text)

# Replace with the path to your image
input_image_path = r"C:\Users\david\Downloads\Inicio-Asana.png"

# Perform OCR and print results
print_ocr_text(input_image_path)