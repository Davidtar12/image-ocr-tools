import os
import subprocess
from PyPDF2 import PdfMerger
from pdf2image import convert_from_path
import pytesseract

def merge_pdfs(folder_path):
    # Create an instance of PdfMerger
    merger = PdfMerger()

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as pdf_file:
                merger.append(pdf_file)

    # Write the merged PDF to a file
    merged_pdf_path = os.path.join(folder_path, 'merged.pdf')
    with open(merged_pdf_path, 'wb') as merged_file:
        merger.write(merged_file)

    return merged_pdf_path

def create_searchable_pdf(input_pdf_path, output_pdf_path):
    # Run OCRmyPDF - it uses Tesseract internally
    subprocess.run(['ocrmypdf', '--force-ocr', input_pdf_path, output_pdf_path], check=True)

def print_ocr_text(input_pdf_path):
    # Convert PDF to images
    images = convert_from_path(input_pdf_path)

    # OCR each page and print text
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='spa+eng')
        print(f"Page {i + 1} Text:\n{text}\n")

# Ask for the folder path
folder_path = input("Enter the folder path containing the PDFs: ")

# Merge PDFs in the folder
merged_pdf_path = merge_pdfs(folder_path)

# OCR the merged PDF
output_pdf_path = os.path.join(folder_path, 'merged_searchable.pdf')
create_searchable_pdf(merged_pdf_path, output_pdf_path)

# Print the OCR'd text (optional)
print_ocr_text(output_pdf_path)