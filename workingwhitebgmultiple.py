import os
import io
from PIL import Image
from rembg import remove


def remove_background(input_path, output_path):
    """
    Removes the background from an image and replaces it with a white background.

    :param input_path: Path to the input image.
    :param output_path: Path to save the output image.
    """
    with open(input_path, 'rb') as file:
        input_data = file.read()

    output_data = remove(input_data)

    image_with_transparency = Image.open(io.BytesIO(output_data))
    white_bg_image = Image.new("RGBA", image_with_transparency.size, "WHITE")
    white_bg_image.paste(image_with_transparency, (0, 0), image_with_transparency)
    white_bg_image.convert('RGB').save(output_path)


def process_multiple_images(image_paths, output_folder):
    """
    Processes multiple images to remove their backgrounds and save them with a white background.

    :param image_paths: List of paths to the input images.
    :param output_folder: Folder where the output images will be saved.
    """
    for input_path in image_paths:
        filename = os.path.basename(input_path)
        output_path = os.path.join(output_folder, 'white_bg_' + filename)
        remove_background(input_path, output_path)
        print(f"Processed {filename}")


# Example usage - list of image paths and the output directory
image_paths = [r"C:\Users\david\Downloads\Productos\WhatsApp Image 2024-01-07 at 9.12.44 PM (1).jpeg"]
output_folder = r"C:\Users\david\Downloads\Productos"

process_multiple_images(image_paths, output_folder)