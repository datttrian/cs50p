from fpdf import FPDF

def create_shirtificate(name):
    # Create instance of FPDF class
    pdf = FPDF('P', 'mm', 'A4')

    # Add a page
    pdf.add_page()

    # Set font for CS50 Shirtificate title
    pdf.set_font("Arial", size = 24)

    # Title
    pdf.cell(200, 10, txt = "CS50 Shirtificate", ln = True, align = 'C')

    # Set font for name
    pdf.set_font("Arial", size = 16)

    # Name on shirt
    pdf.set_text_color(255, 255, 255)  # Set text color to white
    pdf.cell(200, 10, txt = name, ln = True, align = 'C')

    # Add shirt image
    pdf.image('shirtificate.png', x = 40, y = 50, w = 130)

    # Save the pdf with name .pdf
    pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    create_shirtificate(name)

if __name__ == "__main__":
    main()
