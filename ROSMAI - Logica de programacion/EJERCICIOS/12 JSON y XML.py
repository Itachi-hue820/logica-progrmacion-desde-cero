 # EJERCICIO:
 # Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 # siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 # - Nombre
 # - Edad
 # - Fecha de nacimiento
 # - Listado de lenguajes de programación
 # Muestra el contenido de los archivos.
 # Borra los archivos.

 # DIFICULTAD EXTRA (opcional):
 # Utilizando la lógica de creación de los archivos anteriores, crea un
 # programa capaz de leer y transformar en una misma clase custom de tu 
 # lenguaje los datos almacenados en el XML y el JSON.
 # Borra los archivos.

# Mi codigo.

# 📦 Importamos las herramientas necesarias para trabajar con archivos, XML y JSON
import os
import json
import xml.etree.ElementTree as ET

# 📝 Le ponemos nombre a los archivos que vamos a crear
xml_file = "datos.xml"
json_file = "datos.json"

# 🧠 Creamos una clase (como un molde) para guardar los datos de una persona
class Data:
    def __init__(self, name, age, birth_date, programming_languages):
        # 💡 Esto guarda el nombre que le pasamos
        self.name = name
        # 💡 Esto guarda la edad
        self.age = age
        # 💡 Esto guarda la fecha de nacimiento
        self.birth_date = birth_date
        # 💡 Esto guarda una lista de lenguajes de programación
        self.programming_languages = programming_languages

# 🛠️ Creamos un archivo XML con los datos de una persona
def create_xml():
    # ✏️ Empezamos a construir el archivo XML
    root = ET.Element("data") # 🌳 Nodo raíz llamado "data"
    ET.SubElement(root, "name").text = "Pablo"
    ET.SubElement(root, "age").text = "16"
    ET.SubElement(root, "birth_date").text = "2008-01-01"

    # 📚 Lista de lenguajes
    pl = ET.SubElement(root, "programming_languages")
    ET.SubElement(pl, "language").text = "Python"
    ET.SubElement(pl, "language").text = "JavaScript"

    # 💾 Guardamos todo en un archivo XML
    tree = ET.ElementTree(root)
    tree.write(xml_file)

# 🛠️ Creamos un archivo JSON con los mismos datos de la persona
def create_json():
    data = {
        "name": "Pablo",
        "age": 16,
        "birth_date": "2008-01-01",
        "programming_languages": ["Python", "JavaScript"]
    }

    # 💾 Guardamos todo en un archivo JSON
    with open(json_file, "w") as f:
        json.dump(data, f)

# 🧪 Llamamos a las funciones para crear los archivos XML y JSON
create_xml()
create_json()

# 📂 Abrimos el archivo XML para leer lo que hay dentro
with open(xml_file, "r") as archivo_xml:
    # 🔍 Leemos el contenido del XML y lo convertimos en algo que Python pueda entender
    root = ET.fromstring(archivo_xml.read())

    # 📥 Sacamos los datos del XML
    name = root.find("name").text
    age = int(root.find("age").text) # Convertimos la edad a número
    birth_date = root.find("birth_date").text

    # 📥 Sacamos los lenguajes de programación
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    # 🎉 Creamos un objeto Data con los datos del XML
    persona_desde_xml = Data(name, age, birth_date, programming_languages)

    # 👀 Mostramos lo que contiene el objeto
    print("📤 Datos desde XML:")
    print(persona_desde_xml.__dict__)

# 📂 Abrimos el archivo JSON para leer lo que hay dentro
with open(json_file, "r") as archivo_json:
    # 🔍 Cargamos el contenido del archivo como diccionario de Python
    data_dict = json.load(archivo_json)

    # 🎉 Creamos otro objeto Data con los datos del JSON
    persona_desde_json = Data(
        data_dict["name"],
        data_dict["age"],
        data_dict["birth_date"],
        data_dict["programming_languages"]
    )

    # 👀 Mostramos lo que contiene el objeto
    print("📤 Datos desde JSON:")
    print(persona_desde_json.__dict__)

# 🗑️ Borramos los archivos después de usarlos, porque ya no los necesitamos
os.remove(xml_file)
os.remove(json_file)