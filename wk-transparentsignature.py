import cv2
import numpy as np
from PIL import Image

def make_signature_transparent_advanced(input_path, output_path, threshold=127):
    """
    Converts a signature to a transparent PNG using OpenCV for preprocessing.
    :param input_path: Path to the input image.
    :param output_path: Path to save the output image.
    :param threshold: Threshold for binarization. Default is 127.
    """
    # Read the image in grayscale
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding
    _, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    # Convert to RGBA
    img_rgba = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)

    # Set white pixels (now 255, 255, 255) to transparent (0, 0, 0, 0)
    img_rgba[img_rgba[:, :, 0] == 255] = [0, 0, 0, 0]

    # Save the image
    Image.fromarray(img_rgba).save(output_path, 'PNG')
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    make_signature_transparent_advanced(r"G:\My Drive\Personal\Firma\7M59Ex60ZqRr6y1eA4LgWX.png", r"C:\Users\USERNAME\Downloads\Productos\output_imagefirma.png")


