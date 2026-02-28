from PIL import Image
import io


def adaptive_compress_image(file_path, save_path=None, max_size=3.9, max_resolution=(4096, 4096)):
    """
    Adaptively compresses an image to be within a specified size limit in PNG format,
    while trying to maintain the best possible quality.

    :param file_path: Path to the image file.
    :param save_path: Path where the compressed image will be saved.
                      If None, saves in the same directory as the original.
    :param max_size: Maximum size of the image in MB. Defaults to 3.9 MB.
    :param max_resolution: Initial maximum resolution (width, height) of the image.
    :return: None. Saves the compressed image as a PNG.
    """
    # Open the image
    with Image.open(file_path) as img:
        # Gradually reduce resolution if necessary
        while img.size[0] > max_resolution[0] or img.size[1] > max_resolution[1]:
            img.thumbnail((img.size[0] * 0.9, img.size[1] * 0.9), Image.Resampling.LANCZOS)

            buffer = io.BytesIO()
            img.save(buffer, format="PNG", optimize=True)
            size_MB = buffer.getbuffer().nbytes / 1024 / 1024

            if size_MB <= max_size:
                break  # Exit loop if size requirement is met

            max_resolution = (int(img.size[0] * 0.9), int(img.size[1] * 0.9))

        # Determine the save path
        if save_path is None:
            save_path = file_path.replace('.png', '_compressed.png')

        # Save the final image
        img.save(save_path, format="PNG", optimize=True)


# Example usage
adaptive_compress_image(r"H:\My Drive\Ecuador\tortugasgalapagos2024\wetransfer_broll_repatriacion_tortugas-mp4_2024-02-12_1805\Repatriación Tortugas\305A0518.JPG", r"C:\Users\david\Downloads\WhatsApp Image 2024-03-13 at 23.40.42_ab6537e7loco.jpg")