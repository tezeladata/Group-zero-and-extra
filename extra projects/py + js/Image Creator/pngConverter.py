from PIL import Image
import numpy as np

file_path = "output.raw"
width, height = 1000, 1000

try:
    with open(file_path, 'rb') as f:
        raw_data = f.read()

    if len(raw_data) != width * height * 4:
        raise ValueError(f"Expected raw data size of {width * height * 4} bytes, but got {len(raw_data)} bytes")

    image_data = np.frombuffer(raw_data, dtype=np.uint8).reshape((height, width, 4))

    img = Image.fromarray(image_data, 'RGBA')

    output_path = "random_image.png"
    img.save(output_path)
    print(f"Image has been saved to {output_path}")

except Exception as e:
    print(f"Error: {str(e)}")