from PIL import Image
import os
import io


def adaptive_compress_images(source_folder, output_folder, max_size=3.99, max_resolution=(4096, 4096)):
    """
    Adaptively compresses and converts all image files in a folder to be within a specified size limit in JPEG format,
    while trying to maintain the best possible quality.

    :param source_folder: Path to the source folder containing image files.
    :param output_folder: Path to the folder where compressed images will be saved.
    :param max_size: Maximum size of the image in MB. Defaults to 3.99 MB.
    :param max_resolution: Initial maximum resolution (width, height) of the image.
    :return: None. Saves the compressed images as JPEGs in the output folder.
    """
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the source folder
    for file_name in os.listdir(source_folder):
        # Construct full file path
        file_path = os.path.join(source_folder, file_name)

        # Skip if not an image file
        if not (file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg') or file_path.lower().endswith(
                '.png')):
            continue

        try:
            # Open the image
            with Image.open(file_path) as img:
                # Convert to RGB if necessary (e.g., for PNGs with transparency)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                # Gradually reduce resolution if necessary
                while True:
                    img.thumbnail(max_resolution, Image.Resampling.LANCZOS)
                    buffer = io.BytesIO()
                    img.save(buffer, format="JPEG", quality=85, optimize=True)
                    size_MB = buffer.getbuffer().nbytes / 1024 / 1024

                    if size_MB <= max_size:
                        break  # Exit loop if size requirement is met

                    # Reduce the max resolution for the next iteration
                    max_resolution = (int(max_resolution[0] * 0.9), int(max_resolution[1] * 0.9))

                # Save the final image
                output_file_name = os.path.splitext(file_name)[0] + '.jpg'
                output_path = os.path.join(output_folder, output_file_name)
                with open(output_path, 'wb') as f:
                    f.write(buffer.getvalue())

        except Exception as e:
            print(f"Error processing {file_name}: {e}")


# Example usage
source_folder = r"H:\My Drive\Perú\Aves mercurio Perú\Fotos Mongabay 2024-20240314T222151Z-001\Fotos Mongabay 2024\Historia"
output_folder = r"H:\My Drive\Perú\Aves mercurio Perú\Fotos Mongabay 2024-20240314T222151Z-001\Fotos Mongabay 2024\Historia\finalesred"
adaptive_compress_images(source_folder, output_folder)