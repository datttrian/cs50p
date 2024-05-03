from sys import exit, argv
from os import path
from PIL import Image, ImageOps


def main():
    # Expect two command-line arguments the names of images to read and write
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")

    # Extract input and output file paths from command-line arguments
    input_file = argv[1]
    output_file = argv[2]

    # Check if input and output file extensions are valid
    valid_extensions = {".jpg", ".jpeg", ".png"}
    if not input_file.lower().endswith(tuple(valid_extensions)):
        exit("Invalid input")
    if not output_file.lower().endswith(tuple(valid_extensions)):
        exit("Invalid output")

    # Check if input and output file extensions match
    if path.splitext(input_file)[1].lower() != path.splitext(output_file)[1].lower():
        exit("Input and output have different extensions")

    # Check if the input file exists
    if not path.exists(input_file):
        exit("Input does not exist")

    # Open the input image and the shirt image
    try:
        input_image = Image.open(input_file)
        shirt_image = Image.open("shirt.png")
    except FileNotFoundError:
        exit("Input file not found")

    # Resize and crop the input image to match the dimensions of the shirt image
    input_image_resized = ImageOps.fit(input_image, shirt_image.size)

    # Overlay the shirt image onto the input image
    input_image_resized.paste(shirt_image, (0, 0), shirt_image)

    # Save the resulting image to the specified output file
    input_image_resized.save(output_file)


if __name__ == "__main__":
    main()
