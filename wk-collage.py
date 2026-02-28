import os
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

# Function to create a collage from images in a folder
def create_collage(folder_path, output_path, collage_width=1080, collage_height=None, max_images=None):
    # Get a list of all image files in the folder
    folder_path = os.path.abspath(folder_path)
    image_files = [f for f in os.listdir(folder_path) if
                   f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp'))]

    if not image_files:
        print("No image files found in the folder.")
        return None

    # Sort the image files to ensure a consistent order
    image_files.sort()

    if max_images is not None and max_images < len(image_files):
        image_files = image_files[:max_images]

    # Calculate the collage height if not provided
    if collage_height is None:
        collage_height = collage_width

    # Process and resize each image to fit the collage layout
    processed_images = []
    for file in image_files:
        image_path = os.path.join(folder_path, file)
        image = Image.open(image_path)
        image = ImageOps.fit(image, (collage_width, collage_height), Image.LANCZOS)
        processed_images.append(image)

    # Determine the optimal layout for the images
    num_images = len(processed_images)
    num_cols = int(np.sqrt(num_images)) + (np.sqrt(num_images) != int(np.sqrt(num_images)))
    num_rows = int(np.ceil(num_images / num_cols))

    # Create the collage layout
    collage = np.zeros((num_rows * collage_height, num_cols * collage_width, 3), dtype=np.uint8)

    # Place the images in the collage according to the layout
    layout = [(row, col) for row, col in product(range(num_rows), range(num_cols)) if row * num_cols + col < num_images]
    for i, (row, col) in enumerate(layout):
        image = processed_images[i].convert('RGB')  # Convert to RGB mode
        image_array = np.array(image)
        collage[row * collage_height:(row + 1) * collage_height, col * collage_width:(col + 1) * collage_width] = image_array

    # Save the collage as an image file
    plt.imsave(output_path, collage)

    return collage

# Example usage
folder_path = r'C:\Users\david\Downloads\fotoscolpin'
output_path = "collage.png"  # Path to save the collage image
collage_width = 1080
collage_height = 1080
max_images = None  # Set to a specific number if you want to limit the number of images

collage_image = create_collage(folder_path, output_path, collage_width, collage_height, max_images)

if collage_image is not None:
    print("Collage created successfully!")