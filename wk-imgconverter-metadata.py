from PIL import Image
import subprocess
import os
import rawpy
import imageio

def preserve_metadata(source_path, target_path):
    # Use exiftool to transfer metadata from source to target
    exiftool_path = r"C:\Users\david\Downloads\exiftool-12.84\exiftool.exe"
    command = f'"{exiftool_path}" -overwrite_original -TagsFromFile "{source_path}" "{target_path}"'
    subprocess.run(command, shell=True)

def convert_image(input_path, output_path, extension):
    if extension.lower() == '.raf':
        # Handle RAW images with specific settings
        with rawpy.imread(input_path) as raw:
            # Adjust these settings as needed
            rgb = raw.postprocess(use_camera_wb=True, no_auto_bright=False, output_bps=8, auto_bright_thr=0.15)
            imageio.imsave(output_path, rgb)
            preserve_metadata(input_path, output_path)
    else:
        # Handle other formats
        with Image.open(input_path) as img:
            img.save(output_path)
            preserve_metadata(input_path, output_path)

# Directory settings
input_dir = r"C:\Users\david\Downloads\FOTOS"
output_dir = r"C:\Users\david\Downloads\FOTOS\Converted"

# Check and create output directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Supported formats including RAW
supported_formats = [".png", ".jpg", ".jpeg", ".webp", ".raf"]

# Processing files
for filename in os.listdir(input_dir):
    _, extension = os.path.splitext(filename)
    if extension.lower() in supported_formats:
        input_path = os.path.join(input_dir, filename)
        output_filename = os.path.splitext(filename)[0] + ".jpg"  # Converting to JPG
        output_path = os.path.join(output_dir, output_filename)
        convert_image(input_path, output_path, extension)

print("Image conversion completed.")
