
from reportlab.pdfgen import canvas
import sys

# Read the content of the file

file_path = sys.argv[1]
with open(file_path, "r") as file:
    content = file.read()

# Create a PDF with the content
pdf_path = "./pruebas.pdf"
c = canvas.Canvas(pdf_path)
text_object = c.beginText(12, 769.89)# 72 = 1 inch como margen
text_object.setFont("Times-Roman", 12)
text_object.setLeading(13.8)
text_object.textLines(content)

c.drawText(text_object)
c.save()

print("PDF created successfully!")
