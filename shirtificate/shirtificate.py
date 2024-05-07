from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create instance of FPDF class
pdf = Shirtificate()

# Add a page
pdf.add_page()

# Set properties
pdf.set_auto_page_break(auto=True, margin=15)

# Set font for the name
pdf.set_font("Arial", size=16)

# Prompt user for name
name = input("Name: ")

# Add name on top of the shirt
pdf.set_text_color(255, 255, 255)  # white color
pdf.set_xy(75, 130)  # adjust position as needed
pdf.cell(60, 10, name, 0, 1, 'C')

# Add image of the shirt
pdf.image("shirt.png", x=45, y=50, w=120)

# Output PDF
pdf.output("shirtificate.pdf")
