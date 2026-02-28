import io
from PIL import Image
from rembg import remove


def remove_background(input_path, output_path):
    """
    Removes the background from an image and replaces it with a white background.

    :param input_path: Path to the input image.
    :param output_path: Path to save the output image.
    """
    # Open the image file
    with open(input_path, 'rb') as file:
        input_data = file.read()

    # Remove the background
    output_data = remove(input_data)

    # Convert the output to an Image
    image_with_transparency = Image.open(io.BytesIO(output_data))

    # Create a white background image
    white_bg_image = Image.new("RGBA", image_with_transparency.size, "WHITE")

    # Paste the image on white background
    white_bg_image.paste(image_with_transparency, (0, 0), image_with_transparency)

    # Convert to RGB and save
    white_bg_image.convert('RGB').save(output_path)


# Example usage
remove_background(r"C:\Users\david\Downloads\Productos\Imagen de WhatsApp 2023-12-07 a las 15.37.42_6c9afd40_enhanced.jpg", r"C:\Users\david\Downloads\Productos\whitecharger.png")