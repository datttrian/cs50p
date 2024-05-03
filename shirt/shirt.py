import sys
from PIL import Image, ImageOps


def main():
    # Improved argument handling
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py <input_image> <output_image>")

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    # Check file extensions
    if not file_extension_check(input_image_path, output_image_path):
        sys.exit("Input and output images must have the same extension")

    # Load images
    try:
        shirt = Image.open("shirt.png")
        before = Image.open(input_image_path)
    except FileNotFoundError:
        sys.exit("Could not find the image file")

    # Resize and paste images
    size = shirt.size
    before = ImageOps.fit(before, size)
    before.paste(shirt, box=(0, 0), mask=shirt)

    # Save output image
    before.save(output_image_path)


def file_extension_check(input_image_path, output_image_path):
    input_ext = input_image_path.lower().split('.')[-1]
    output_ext = output_image_path.lower().split('.')[-1]
    if input_ext != output_ext or input_ext not in ["png", "jpg", "jpeg"]:
        return False
    return True


if __name__ == "__main__":
    main()
