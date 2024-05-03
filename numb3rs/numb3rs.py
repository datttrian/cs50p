import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression pattern for validating IPv4 addresses
    ipv4_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    # Check if the input matches the IPv4 pattern
    if re.match(ipv4_pattern, ip):
        # Check if each byte is within the valid range
        bytes = ip.split('.')
        for byte in bytes:
            if int(byte) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
