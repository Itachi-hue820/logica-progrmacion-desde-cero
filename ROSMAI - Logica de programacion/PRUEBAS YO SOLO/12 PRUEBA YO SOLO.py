
# Mi codigo.

import os
import json
import xml.etree.ElementTree as ET

xml_file = "datos.xml"
json_file = "datos.json"

class Data:
    def __init__(self, name, age, birth_date, programming_languages):
        self.name = name  
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

def create_xml():
    
    root = ET.Element("data") 
    ET.SubElement(root, "name").text = "Pablo"
    ET.SubElement(root, "age").text = "16"
    ET.SubElement(root, "birth_date").text = "2008-01-01"

    pl = ET.SubElement(root, "programming_languages")
    ET.SubElement(pl, "language").text = "Python"
    ET.SubElement(pl, "language").text = "JavaScript"

    tree = ET.ElementTree(root)
    tree.write(xml_file)

def create_json():
    data = {
        "name": "Pablo",
        "age": 16,
        "birth_date": "2008-01-01",
        "programming_languages": ["Python", "JavaScript"]
    }

    with open(json_file, "w") as f:
        json.dump(data, f)

create_xml()
create_json()

with open(xml_file, "r") as archivo_xml:
    root = ET.fromstring(archivo_xml.read())
    name = root.find("name").text
    age = int(root.find("age").text) 
    birth_date = root.find("birth_date").text

    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    persona_desde_xml = Data(name, age, birth_date, programming_languages)
    
    print(" Datos desde XML:")
    print(persona_desde_xml.__dict__)

with open(json_file, "r") as archivo_json:
    data_dict = json.load(archivo_json)
    persona_desde_json = Data(
        data_dict["name"],
        data_dict["age"],
        data_dict["birth_date"],
        data_dict["programming_languages"]
    )

    print("Datos desde JSON:")
    print(persona_desde_json.__dict__)

os.remove(xml_file)
os.remove(json_file)