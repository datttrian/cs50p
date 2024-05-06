import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_count = len(re.findall(r'\bum\b', s, re.IGNORECASE))
    return um_count


if __name__ == "__main__":
    main()
