
from reportlab.pdfgen import canvas
import sys

limiteLineas = 51
imprimir = ""
pdf_path = "./pruebas.pdf"

file_path = sys.argv[1] # es el path del archivo que se le pasa como argumento
with open(file_path, "r") as file:
    content = file.read() #lee el contenido del archivo



lines_code = content.split('\n') # es una lista de lineas de codigo
ultima_linea = len(lines_code) # obtengo la ultima linea del archivo su indice
contador = 0

c = canvas.Canvas(pdf_path)
def imprimirLineas():
    global contador
    global imprimir
    global c
    text_object = c.beginText(72, 769.89)# 72 = 1 inch como margen
    text_object.setFont("Times-Roman", 12)
    text_object.setLeading(13.8)
    text_object.textLines(imprimir)
    c.drawText(text_object)
    c.showPage()
    contador = 0
    imprimir = ""

for contadorLinea, line in enumerate(lines_code, start=1):
    if contador < limiteLineas: # esto solamente es falso cuando cuando contador es igual a 51, si contador no llega a 51 no se imprime nada
        imprimir = imprimir + line + "\n"
        contador = contador + 1
        if contadorLinea == ultima_linea:
            imprimirLineas()
    else:
        imprimirLineas()

c.save()
# Create a PDF with the content
print("PDF created successfully!")
