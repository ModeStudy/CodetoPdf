from reportlab.pdfgen import canvas
import glob
import sys
import os
import glob

limiteLineas = 51
pdf_path = "./pruebas.pdf"
file_path = sys.argv[1] # es el path del archivo que se le pasa como argumento
c = canvas.Canvas(pdf_path)


def listar_archivos(directorio):
    archivos_cpp = glob.glob(directorio + "/*.cpp")
    return archivos_cpp


def leer_archivo(file_path):
    with open(file_path, "r") as file:
        content = file.read() #lee el contenido del archivo
    return content

def preparar_contenido(path):
    global c 
    lines_code = leer_archivo(path).split('\n') # es una lista de lineas de codigo
    ultima_linea = len(lines_code) # obtengo la ultima linea del archivo su indice
    contador = 0
    imprimir = ""
    for contadorLinea, line in enumerate(lines_code, start=1):
        if contador < limiteLineas: # esto solamente es falso cuando cuando contador es igual a 51, si contador no llega a 51 no se imprime nada
            imprimir = imprimir + line + "\n"
            contador = contador + 1
            if contadorLinea == ultima_linea:
                imprimirLineas(imprimir, contador)
                imprimir = ""
                contador = 0
        else:
            imprimirLineas(imprimir, contador)
            imprimir = ""
            contador = 0

def imprimirLineas(imprimir, contador):
    global c
    text_object = c.beginText(72, 769.89)# 72 = 1 inch como margen
    text_object.setFont("Times-Roman", 12)
    text_object.setLeading(13.8)
    text_object.textLines(imprimir)
    c.drawText(text_object)
    c.showPage()


for archivo in listar_archivos(file_path):
    preparar_contenido(archivo)

c.save()
# Create a PDF with the content
print("PDF created successfully!")