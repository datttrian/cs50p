import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Text: ")
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (
        sys.argv[2] in figlet.getFonts()
    ):
        text = input("Text: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
