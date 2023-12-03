
from reportlab.pdfgen import canvas

# Read the content of the file
file_path = "./pruebas.cpp"
with open(file_path, "r") as file:
    content = file.read()

# Create a PDF with the content
pdf_path = "./pruebas.pdf"
c = canvas.Canvas(pdf_path)
text_object = c.beginText(100, 750)
text_object.textLines(content)
c.drawText(text_object)
c.save()

print("PDF created successfully!")
