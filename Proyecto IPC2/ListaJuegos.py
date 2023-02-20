import xml.etree.cElementTree as ET
from xml.dom import minidom
#Mandar a llamar el archivo parseando
file = minidom.parse("Ejemplo2.xml")
#Obtener Elemento
doc = file.documentElement

JuegoViejos = doc.getElementsByTagName("Juego")

for lista in JuegoViejos:
    NombreJuego = lista.getElementsByTagName("nombre")
    CodigoJuego = lista.getElementsByTagName("codigo")
    print("Nombre:", NombreJuego[0].childNodes[0].nodeValue,  " | ", "Codigo", CodigoJuego[0].childNodes[0].nodeValue , "|")
    