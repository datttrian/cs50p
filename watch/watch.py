import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to find YouTube URL in src attribute
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'

    # Search for the pattern in the input string
    match = re.search(pattern, s)

    if match:
        # Extract the video ID from the matched URL
        video_id = match.group(1)
        # Construct the shorter youtu.be equivalent URL
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
