import subprocess
from pdf2image import convert_from_path
import pytesseract

def create_searchable_pdf(input_pdf_path, output_pdf_path):
    # Run OCRmyPDF - it uses Tesseract internally
    subprocess.run(['ocrmypdf', '--force-ocr', input_pdf_path, output_pdf_path], check=True)

def print_ocr_text(input_pdf_path):
    # Convert PDF to images
    images = convert_from_path(input_pdf_path)

    # OCR each page and print text
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang='eng')
        print(f"Page {i + 1} Text:\n{text}\n")

# Replace with the path to your PDF
input_pdf_path = r"C:\Users\david\OneDrive\Audiobooks\Epubs or txt files\PDF\iMAGE\Art of the Andes _ from Chavín to Inca -- Rebecca R_ Stone -- World of Art, 3, 2012 -- Thames and Hudson -- 9780500203637 -- 2ef2415abbb33a5f4f681d3ecd008ece -- Anna’s Archive.pdf"
output_pdf_path = r'C:\Users\david\Downloads\artandes.pdf'

# Create a searchable PDF
create_searchable_pdf(input_pdf_path, output_pdf_path)

# Print the OCR'd text (optional)
print_ocr_text(input_pdf_path)