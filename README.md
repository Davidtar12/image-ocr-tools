# image-ocr-tools

Image & document processing: OCR text extraction, table parsing, PDF merging, batch image conversion and compression.

## Scripts

| Script | Description |
|--------|-------------|
| `wk-ocrimg.py` | OCR a single image to text using Tesseract |
| `wk-ocr-eng.py` | OCR optimised for English-language documents |
| `wk-ocrmultipleimgs.py` | Batch OCR all images in a folder — outputs one text file per image |
| `wk-ocrpdfs.py` | OCR scanned PDF files page by page — outputs text per page |
| `ocr-tables.py` | Detect and extract tables from images using OCR + layout analysis |
| `wk-tableextractor.py` | Extract tables from PDFs into structured CSV/Excel format |
| `wk-tableextractor with index and columnname.py` | Table extraction with auto-detected column headers and row index |
| `wk-tableforindex.py` | Extract tables with a specific index column (e.g., date-indexed financial tables) |
| `wk-merge-ocr-pdfs.py` | Merge multiple PDFs into a single file with an OCR text layer |
| `wk-imgcompresser.py` | Compress a single image — reduces file size while preserving quality |
| `wk-multiple-img-compressor.py` | Batch compress all images in a folder |
| `wk-imgconverter-metadata.py` | Convert image formats (JPG/PNG/WEBP) and clean or edit EXIF metadata |
| `wk-collage.py` | Create a photo collage from multiple images with configurable layout |
| `wk-transparentsignature.py` | Remove white background from scanned signatures — makes it transparent (PNG) |
| `workingwhitebg.py` | Replace any background colour in an image with white |
| `workingwhitebgmultiple.py` | Batch white-background replacement for all images in a folder |
| `wk-pruebamejorarimagen.py` | AI-assisted image quality enhancement (sharpening, contrast) |
| `wk-raf-converter.py` | Convert Fujifilm RAW (.raf) files to JPEG/PNG |

## Prerequisites

- Python 3.9+
- **Tesseract OCR** must be installed:
  - Windows: download installer from [github.com/UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
  - macOS: `brew install tesseract`
  - Linux: `sudo apt install tesseract-ocr`
- Verify install: `tesseract --version`

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# OCR a scanned image
python wk-ocrimg.py --input scan.png --output output.txt

# Batch OCR a folder
python wk-ocrmultipleimgs.py --folder ./scans --output ./text_output

# Extract table from image to CSV
python ocr-tables.py --input table_screenshot.png --output table.csv

# Compress all images in a folder
python wk-multiple-img-compressor.py --folder ./photos --quality 80

# Make signature transparent
python wk-transparentsignature.py --input signature.jpg --output signature.png
```

## Built with

Python · Tesseract OCR · Pillow · pdfplumber · OpenCV  
AI-assisted development (Claude, GitHub Copilot) — architecture, requirements, QA validation and debugging by me.
