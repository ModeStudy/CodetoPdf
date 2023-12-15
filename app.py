from reportlab.pdfgen import canvas
import glob
import sys
import os

limiteLineas = 47
pdf_path = "./pruebas.pdf"
busqueda_path = sys.argv[2] # es el path del archivo que se le pasa como argumento
file_path = sys.argv[1] # es el path del archivo que se le pasa como argumento
c = canvas.Canvas(pdf_path, pagesize=(612,792))

def leer_archivo(file_path):
    with open(file_path, "r") as file:
        content = file.read() #lee el contenido del archivo
    return content

def preparar_lenguajes(path):
    lenguajes_aux =leer_archivo(path).split('\n')
    lenguajes = []
    for lenguaje in lenguajes_aux:
        if lenguaje != "":
            lenguajes.append(lenguaje)
    lenguajes_aux.clear()
    return lenguajes

def listar_archivos(path):
    lenguajes = preparar_lenguajes(busqueda_path)
    archivos = os.listdir(path)
    listar_archivos = []
    for archivo in archivos:
        for lenguaje in lenguajes:
            if archivo.endswith(lenguaje):
                archivo = path + "/" + archivo
                listar_archivos.append(archivo)
    return listar_archivos



def preparar_contenido(path):
    global c 
    lines_code = leer_archivo(path).split('\n') # es una lista de lineas de codigo
    ultima_linea = len(lines_code) # obtengo la ultima linea del archivo su indice
    contador = 0
    imprimir = ""
    y , x = 720, 72
    for contadorLinea, line in enumerate(lines_code, start=1):
        if contadorLinea == 1: 
            c.setFont("Times-Roman", 20)
            c.drawString(72, 720, obtener_titulo(path))
            y = 700
        if contador < limiteLineas: # esto solamente es falso cuando cuando contador es igual a 51, si contador no llega a 51 no se imprime nada
            if len(line)>80:
                aux, contador_aux = "", 0
                last = len(line)-1
                for i, letra in enumerate(line):
                    
                    if contador_aux < 80:
                        aux = aux + letra
                    else:
                        lines_code.insert(contadorLinea -1, aux)
                        aux = ""
                        contador_aux = 0
                    if last == i:
                        lines_code.insert(contadorLinea -1, aux)
            imprimir = imprimir + line + "\n"   
            contador = contador + 1
            if contadorLinea == ultima_linea:
                imprimirLineas(imprimir, x, y)
                imprimir = ""
                contador = 0
                y = 720
        else:
            imprimirLineas(imprimir, x, y)
            imprimir = ""
            contador = 0
            y = 720

def imprimirLineas(imprimir, x, y): #antes de este paso el contenido ya debe de estar preparado
    global c
    text_object = c.beginText(x, y)# 72 = 1 inch como margen
    text_object.setFont("Times-Roman", 12)
    text_object.setLeading(13.8)
    text_object.textLines(imprimir)
    c.drawText(text_object)
    c.showPage()

def obtener_titulo(path):
    ruta_archivo = ""
    for letra in path[::-1]: #volteo la ruta para empezar desde la ultima posicion
        if letra == "/":
            break #si encuentra una diagonal ya no me interesa seguir buscando
        else:
            ruta_archivo = ruta_archivo + letra #si es una letra la agrego a la variable
    return ruta_archivo[::-1] #finalmente invertimos la cadena

if os.path.isdir(file_path):
    for archivo in listar_archivos(file_path):
        preparar_contenido(archivo)
else:
    preparar_contenido(file_path)

c.save()
# Create a PDF with the content
print("PDF created successfully!")