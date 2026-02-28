import subprocess
import pytesseract
import cv2
import pandas as pd
from pdf2image import convert_from_path
from pytesseract import Output

# Best practice: Specify Tesseract executable path if not in standard locations
# pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

def ocr_image_to_csv(input_image_path, output_csv_path):
    # Load the image
    image = cv2.imread(input_image_path)

    # Perform OCR using Pytesseract (prioritizing Spanish and English)
    data = pytesseract.image_to_data(image, output_type=Output.DICT, lang='spa+eng')

    # Convert data to a DataFrame
    df = pd.DataFrame(data)

    # Drop rows with empty text
    df = df[df['text'].notnull()]

    # Save the DataFrame as a CSV file
    df.to_csv(output_csv_path, index=False, header=False)
    print(f"OCR results for {input_image_path} saved to {output_csv_path}")

def ocr_pdf_to_csv(input_pdf_path, output_csv_path):
    # Convert PDF to images
    images = convert_from_path(input_pdf_path)

    # Create an empty DataFrame to store all the data
    all_data = pd.DataFrame()

    # OCR each page and append data to the DataFrame
    for i, image in enumerate(images):
        data = pytesseract.image_to_data(image, output_type=Output.DICT, lang='spa+eng')
        page_data = pd.DataFrame(data)
        page_data = page_data[page_data['text'].notnull()]
        page_data['page'] = i + 1
        all_data = all_data.append(page_data, ignore_index=True)

    # Save the DataFrame as a CSV file
    all_data.to_csv(output_csv_path, index=False, header=False)
    print(f"OCR results for {input_pdf_path} saved to {output_csv_path}")

# Example usage for images
ocr_image_to_csv(r"C:\Users\USERNAME\Downloads\Imagen de WhatsApp 2024-05-15 a las 10.38.19_3ec88003.jpg", r"C:\Users\USERNAME\Downloads\output.csv")

# Example usage for PDFs
#ocr_pdf_to_csv(r"path/to/pdf.pdf", r"path/to/output.csv")