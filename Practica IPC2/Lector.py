import xml.etree.cElementTree as ET
from xml.dom import minidom
import os
print("Ingrese la ruta del XML")
filename = input()
if not os.path.isfile(filename):
    print("No se encontro, verifique que este bien escrito")
    exit()
tree = ET.parse(filename)
root = tree.getroot()
#Codigo By Riu
#Listas
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
class Lista:
    def __init__(self):
        self.head = None
#-------------------------------------------------------

    def insert(self, data):
        new_node = Nodo(data)

        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
#-------------------------------------------------------
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
#-------------------------------------------------------
    def bubble_sorting(self):
        if self.head is None or self.head.next  is None:
            return
        bubble_list = False
        while not bubble_list:
            bubble_list = True
            current_node = self.head
            while current_node.next is not None:
                if current_node.data["Codigo"] > current_node.next.data["Codigo"]:
                    bubble_list = False
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                current_node = current_node.next        
#-------------------------------------------------------
plataformas = Lista()
#-------------------------------------------------------------------
print("--------Generando Lista Plataformas--------")
for plataforma in root.find("ListaPlataformas").findall("Plataforma"):
    codigo = plataforma.find("codigo").text
    nombre = plataforma.find("nombre").text
    plataformas.insert({"Codigo": codigo, "Nombre Plataforma": nombre})

print("Plataformas:")
plataformas.print_list()       
print("--------Generando Lista Juegos--------")
juegos = Lista()
for juego in root.find("ListadoJuegos").findall("Juego"):
    codigo = juego.find("codigo").text
    nombre = juego.find("nombre").text
    try:
        plataforma_codigo = juego.find("Plataformas/Plataforma/codigo").text
    except AttributeError:
        plataforma_codigo = None
    juegos.insert({"Codigo": codigo, "Juego": nombre, "Codigo Plataforma": plataforma_codigo})
print("Juegos")
juegos.print_list()



#--------------------------------------------------
print("-----------------Iniciando Ordenamiento-----------------")
plataformas.bubble_sorting()
juegos.bubble_sorting()
print("Plataformas:")
plataformas.print_list()
print("Juegos")
juegos.print_list()

print("------------------------Iniciando Creacion de XML----------------------------------")

new_root = ET.Element("JuegosViejos")

lista_plataformas = ET.SubElement(new_root, "ListaPlataformas")
for plataforma in plataformas:
    n = ET.SubElement(lista_plataformas, "Plataforma")
    codigo = ET.SubElement(n, "codigo")
    codigo.text = plataforma["Codigo"]
    nombre = ET.SubElement(n, "nombre")
    nombre.text = plataforma["Nombre Plataforma"]
    print(codigo.text, nombre.text)

listado_juegos = ET.SubElement(new_root, "ListadoJuegos")
for juego in juegos:
    m = ET.SubElement(listado_juegos, "Juego")
    codigo = ET.SubElement(m, "codigo")
    codigo.text = juego["Codigo"]
    nombre = ET.SubElement(m, "nombre")
    nombre.text = juego["Juego"]
    if juego["Codigo Plataforma"] is not None:
        plataformas_node = ET.SubElement(m, "Plataformas")
        plataforma_node = ET.SubElement(plataformas_node, "Plataforma")
        codigo_node = ET.SubElement(plataforma_node, "codigo")
        codigo_node.text = juego["Codigo Plataforma"]

xmlstr = minidom.parseString(ET.tostring(new_root)).toprettyxml(indent ="  ")
with open("Ejemplo2_sorted.xml", "w") as f:
    f.write(xmlstr)
print("Archivo generado con exito en teoria")