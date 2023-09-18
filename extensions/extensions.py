def main():
    # Define a dictionary mapping file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }

    # Prompt the user for a file name and remove leading/trailing spaces
    file_name = input("Enter the name of a file: ").strip()

    # Get the file extension (if any) and convert it to lowercase for case insensitivity
    file_extension = file_name[file_name.rfind(".") :].lower()

    # Check if the file extension is in the dictionary, otherwise use the default
    media_type = media_types.get(file_extension, "application/octet-stream")

    # Output the determined media type
    print(media_type)


if __name__ == "__main__":
    main()
