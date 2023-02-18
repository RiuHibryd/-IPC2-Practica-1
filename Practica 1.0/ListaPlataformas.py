import xml.etree.cElementTree as ET
from xml.dom import minidom

#Mandar a llamar el archivo parseando
file = minidom.parse("Ejemplo2.xml")
doc = file.documentElement
#Obtener Elemento

print("---Acceso Global XML 1.0---")
ListaPlataformas = doc.getElementsByTagName("ListaPlataformas")


for Plataforma in ListaPlataformas:
    LaLista = Plataforma.getElementsByTagName("Plataforma")
    for Listado in LaLista:
        LaPltaforma = Listado.getElementsByTagName("nombre")
        ElCodigo = Listado.getElementsByTagName("codigo")
        print("Plataforma:", LaPltaforma[0].childNodes[0].nodeValue , "CodigoPlataforma:", ElCodigo[0].childNodes[0].nodeValue)
        

