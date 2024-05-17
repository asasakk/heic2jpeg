from PIL import Image
import pillow_heif
import glob
import pathlib

# dir = " your image Directory"

def heic_jpg(image_path, save_path):
    try:
        heif_file = pillow_heif.read_heif(image_path)
        for img in heif_file: 
            image = Image.frombytes(
                img.mode,
                img.size,
                img.data,
                'raw',
                img.mode,
                img.stride,
            )
        image.save(save_path, "JPEG")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

image_dir = pathlib.Path(dir)
heic_path = list(image_dir.glob('**/*.HEIC'))

for i in heic_path:
    image_path = str(i)
    save_path = str(image_dir / i.stem) + '.jpg'
    print(save_path)
    heic_jpg(image_path, save_path)
