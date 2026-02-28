import cv2
import numpy as np

def enhance_image(image_path):
    # Read the image from the file
    original_image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if original_image is None:
        print(f"Error loading image {image_path}")
        return

    # Convert to LAB color space
    lab_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)

    # Split the LAB image to different channels
    l, a, b = cv2.split(lab_image)

    # Apply CLAHE to L-channel
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    # Merge the CLAHE enhanced L-channel with the a and b channel
    enhanced_lab_image = cv2.merge((cl, a, b))

    # Convert back to BGR color space
    enhanced_image = cv2.cvtColor(enhanced_lab_image, cv2.COLOR_LAB2BGR)

    # Save the enhanced image
    enhanced_image_path = image_path.replace('.jpg', '_enhanced.jpg')
    cv2.imwrite(enhanced_image_path, enhanced_image)

    return enhanced_image_path

# Use this function before the background removal process
enhanced_image_path = enhance_image(r"C:\Users\david\Downloads\Productos\Imagen de WhatsApp 2023-12-07 a las 15.37.42_6c9afd40.jpg")

# Then you can use the enhanced image for background removal