import rawpy
import imageio

def convert_raw_image(input_path, output_path, brightening_factor=0.15):
    with rawpy.imread(input_path) as raw:
        # Process image with minimal adjustments:
        # use_camera_wb=True uses the camera's white balance setting,
        # no_auto_bright=True avoids automatic brightness adjustment
        rgb = raw.postprocess(use_camera_wb=True, no_auto_bright=False, output_bps=8, auto_bright_thr=brightening_factor)
        imageio.imsave(output_path, rgb)

input_path = r"C:\Users\david\Downloads\FOTOS\_DSF5021.RAF"
output_path = r"C:\Users\david\Downloads\FOTOS\Converted\File.jpg"

convert_raw_image(input_path, output_path)