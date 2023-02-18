import xml.etree.cElementTree as ET
from xml.dom import minidom
tree = ET.parse("Ejemplo2.xml")
root = tree.getroot()
#Codigo By Riu
#Listas
plataformas = []
juegos = []

for plataforma in root.find("ListaPlataformas").findall("Plataforma"):
    codigo = plataforma.find("codigo").text
    nombre = plataforma.find("nombre").text
    plataformas.append({"Codigo": codigo, "Nombre Plataforma": nombre})
#-------------------------------------------------
for juego in root.find("ListadoJuegos").findall("Juego"):
    codigo = juego.find("codigo").text
    nombre = juego.find("nombre").text
    plataformas_juego = []
    for plataforma in juego.find("Plataformas").findall("Plataforma"):
        codigo_plataforma = plataforma.find("codigo").text
        plataformas_juego.append({"Codigo": codigo_plataforma})
    juegos.append({"Codigo": codigo, "Nombre": nombre, "Plataforma": plataformas_juego})

print(plataformas)
print(juegos)
