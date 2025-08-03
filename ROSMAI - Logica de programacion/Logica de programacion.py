# DIA 1

"""
Lógica de programación desde cero parte 1.
"""

# https://python.org

# Esto es un comentario en una linea.

"""
Esto tambien es 
un comentario
en varias lineas.
"""

'''
Esto tambien es 
un comentario
en varias lineas.
'''

my_variable = "Mi variable"
my_variable = "Mi nueva variable"

MY_CONSTANT = "Mi constante" # por convencion. 

"""
Datos 
primitivos.
"""

my_int = 1 # numero entero. 
my_float = 2.25 # numero decimal. 
my_bool = True 
my_bool = False 
my_string = "Mi cadena de texto" # para imprimir una cadena de texto, van entre comillas dobles o solas.
my_other_string = 'Mi otra cadena de texto' # para imprimir otra cadena de texto. 

print("Hola, Python.") # para imprimir un texto o palabra.

print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))
print(type(my_other_string))

"""
Operadores.
"""

#Operadores aritmeticos

# Tienes que acordarte de que se pone en cada uno.

print(f"Suma: 10 + 3 = {10 + 3}") # lo que esta entre las llaves es una interpolacion y sirve para enseñar la suma.
#F : Sirve para interpolar valores dentro de un texto fácilmente, es decir,
#meter variables o expresiones directamente dentro del texto usando llaves {}.

print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}") # el resto de la divison.
print(f"Exponente: 10 ** 3 = {10 ** 3}") # un numero elavado a algo.
print(f"Divison entera: 10 // 3 = {10 // 3}")

# Operadores de comparacion

# Tienes que acordarte de que se pone en cada uno.

print(f"Igualdad: 10 == 3 {10 == 3}")
print(f"Desigualdad: 10 != 3 {10 != 3}")
print(f"Mayor que: 10 > 3 {10 > 3}")
print(f"Menor que: 10 < 3 {10 < 3}")
print(f"Mayor o igual que: 10 >= 10 {10 >= 10}")
print(f"Menor o igual que: 10 <= 3 {10 <= 3}")

# Operadores logicos

# Tienes que acordarte de que se pone en cada uno.

print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") # Pide que sean las dos condiciones verdaderas.
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}") # Solo pide que sea verdadera una condicion.
print(f"NOT !: 10 + 3 == 14 es {10 + 3 == 14}") 
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}") 

# Operadores de asignacion 

# Tienes que acordarte de que se pone en cada uno.

my_number = 10 # asignacion 
print(my_number)
my_number += 1 # suma y asignacion 
print(my_number)
my_number -= 1 # resta y asignacion 
print(my_number)
my_number *= 2 # multiplicar y asignacion 
print(my_number)
my_number /= 2 # dividir y asignacion 
print(my_number)
my_number %= 3 # modulo y asignacion 
print(my_number)
my_number **= 1 # exponente y asignacion 
print(my_number)
my_number //= 1 # division entera y asignacion 
print(my_number)

# Operadores de identidad 

# Tienes que acordarte de que se pone en cada uno.

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}") # igualdad 
print(f"my_number is not my_new_number es {my_number is not my_new_number}") # desigualdad

# Operadores de pertenencia 

# Tienes que acordarte de que se pone en cada uno.

print(f"'o' in 'Paolo' = {'o' in 'Paolo'}") # Verifica si ese objeto esta en lo que quieres saber como por ejemplo en el nombre.
print(f"'g' not in 'Paolo' = {'g' not in 'Paolo'}") # Dara true porque es verdad que esa letra no esta.
print(f"'t' in 'Paolo' = {'t' in 'Paolo'}") # Dara falso porque no esta esa letra.

# DIA 2

# Operadores de bit 

# Casi nunca se usan solo cuando estas estudiando. 

a = 10 # 1010 esto es en binario. 
b = 3 # 0011 esto es en binario. 

print(f"AND: 10 & 3 = {10 & 3}") # No entendi ni verga , compara bit a bit.
print(f"OR: 10 | 3 = {10 | 3}") # Compara todos los bits y si al menos uno o dos son 1 da 1.
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # Si los bits son diferentes son 1 pero si son iguales es 0. 
print(f"NOT: ~10 = {~10}") # Intercambia el valor bit a bit. 
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # Desplaza los bits a un lado expecifico. 
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # Desplaza los bits a un lado expecifico. 

"""
Estructuras de control.
"""

# Condicionales 

# Tienes que acordarte de que se pone en cada uno.

my_string = "Paolo"

if my_string == "Paolo" : 
    print("my string es 'Paolo'")
elif my_string  == "Conde" : 
    print("my string es 'Conde'") # Se comprueba si esto es cierto (si el 'if' fallo).
else:
    print("my string no es 'Paolo'") # Si ninguna condición se cumple, se ejecuta esto.

# Interativas 

# Tienes que acordarte de que se pone en cada uno.

for i in range(11):
  print(i) # Sirve para inprimir una seguencia o bucle , range sinifica que imprime todos esos numeros o seguencia sin tener en cuenta ese ultimo numero.
# for indica cuantas veces se imprime esa secuencia.

i = 0

while i <= 10:
 print(i) # while sirve para imprimir algo si se cumple una condicion exacta.
 i += 1

# Manejo de excepciones

# Tienes que acordarte de que se pone en cada uno.

try:               # try sirve para que por si acaso el programa falle no pete y al reves imprima algo que tu digas.
    print(10 / 0)
except: 
      print("Se ha producido un error") 
finally:           # finally sirve para que si pete o no imprima lo que tu quieras decir.
    print("Ha finalizado el manejo de excepciones")   
   

"""
Extra.
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
       print(number)

"""
Funciones definidas por el usuario.
"""

# Simple.

# Tienes que acordarte de que se pone en cada uno.

def greet():   # def , funcion que hace algo en concreto y simple.
    print("Hola, Python!")

greet() # Llama a esa funcion para que se ejecute.

# Con retorno.

# Tienes que acordarte de que se pone en cada uno.

def return_greet(): # Sirve para devolver una cadena de texto. 
    return "Hola, Python!"

greet = return_greet # Esto es una variable que sirve para guardar el return_greet.
print(greet)

# Con un argumento.

# Tienes que acordarte de que se pone en cada uno.

def arg_greet(name):  # Sirve para especificar en un apartado exactamente que quieres poner o llamar.
     print(f"Hola, {name}")

arg_greet("Paolo")

# Con argumentos.

# Tienes que acordarte de que se pone en cada uno.

def args_greet(greet, name):  # Sirve para especificar en apartados exactamente que quieres poner o llamar.
     print(f"{greet}, {name}")

args_greet("Hi", "Paolo")

# Con un argumento predeterminado.

# Tienes que acordarte de que se pone en cada uno.

def default_arg_greet(name="Python"):  # Sirve para que cuando un parametro no tiene especificacion ponca lo que tu quieres por defecto.
     print(f"Hola, {name}")

default_arg_greet("Paolo")
default_arg_greet()

# Con argumentos y retornos.

# Tienes que acordarte de que se pone en cada uno.

def return_args_greet(greet, name):  
     return f"{greet}, {name}"


print(return_args_greet("Hi", "Paolo"))

# Con retorno de varios valores.

# Tienes que acordarte de que se pone en cada uno.

def multiple_retorn_greet():  # Para que imprimir varias palabras en un retorno por separado.
    return "Hola", "Python"

greet, name= multiple_retorn_greet() 
print(greet) 
print(name) 

# Con un numero variable de argumentos.

# Tienes que acordarte de que se pone en cada uno.

def variable_arg_greet(*names):  # *name , significa que le puedes pasar mas de un nombre.
    for name in names:
        print(f"Hola, {name}")
              
variable_arg_greet("Python", "Paolo", "Itachi") # Le pasas mas de un nombre para saludar.

# DIA 3 

# Con un numero variable de argumentos con palabras clave.

# Tienes que acordarte de que se pone en cada uno.

def variable_key_arg_greet(**names):  # Sirve para especificar qué es cada cosa.
    for param, name in names.items():
        print(f"Hola, {name} ({param})")

variable_key_arg_greet(
    lenguage="Python", 
    name="Paolo", 
    alias="Itachi", 
    age=36
)


"""
Funciones dentro de funciones.
"""

def outer_function():       # Sirve para tener funciones dentro de otras y poder llamarlas, no sirve de mucho.
    def inner_fuction():
        print("Funcion interna: Hola, Python")
    inner_fuction()

outer_function()

"""
Funciones del lenguaje.
"""

print(len("Paolo")) # len, indica la longitud.
print(type("Paolo")) # type, te dice el tipo de variable que es.
print("Paolo".upper()) # upper, sirve para que ponga todo en mayusculas.

"""
Variables locales y globales.
"""

global_variable = "Python"  # global, funcina en diferentes funciones y lo pudes llamar.

print(global_variable)

def hello_python():     
    local_variable = "Hello"    # local, solo funciona dentro de esa misma funcion no lo pudes llamar.
    print(f"{local_variable}, {global_variable}")

hello_python()

"""
Estructuras de datos.
"""

# Listas

# Tienes que acordarte de que se pone en cada uno.

my_list = ["Paolo", "Christian", "Itachi", "Moure"]
print(my_list)
my_list.append("Castor") # append, sirve para añadir algo mas a la lista ya hecha. Insercion.
print(my_list)
my_list.remove("Castor") # remove, sirve para eliminar algo de la lista ya creada. Eliminacion.
print(my_list)
print(my_list[1]) # sirve para saber en que posicion este alguien exactamente.
my_list[1] = "Cuervillo"
print(my_list)  # Sirve para actualizar un nombre. Actualizacion.
my_list.sort()  # Ordena toda la cadena de texto.
print(my_list)

# Tuplas 

# Tienes que acordarte de que se pone en cada uno.

my_tuple = ("Paolo", "Conde", "Ramirez", 16) # Es una lista pero donde no pudes modificar nada es totalmente seguro.
print(type(my_tuple))

# Sets

# Tienes que acordarte de que se pone en cada uno.

my_set = {"Paolo", "Christian", "Itachi", "Moure"}  # Son estructuras desordenadas pero buenas para muchos datos a la vez.
print(my_set)
my_set.add("paoloconde05@gmail.com") # Insercion
print(my_set)
my_set.remove("Christian") # Eliminacion
print(my_set)
print(type(my_set))

# Diccionario

# Tienes que acordarte de que se pone en cada uno.

my_dict: dict = {        # No son ordenados solo son claves y valores.
    "name":"Paolo", 
    "surmane":"Christian", 
    "alias":"Itachi", 
    "age":"16"
} 
my_dict["email"] = "paoloconde05@gmail.com"  # Insercion
print(my_dict)
print(my_dict["name"])  # Acceso 

# DIA 4

my_dict["age"] = "17"   # Actualizacion
print(my_dict)
del my_dict["surmane"]  # Eliminacion
print(my_dict)
print(type(my_dict))

"""
Cadenas de Caracteres.
"""

s1 = "Hola"
s2 = "Python"

# Concatenacion.

print(s1 + s2) # Sumar los valores para hacer la cadena de texto.

# Repeticion.

print(s1 * 3) # Le pones multiplicacion para repetir esa palabra las veces que quiras.

# Indexacion.

print(s1[0] + s1[1] + s1[2] + s1[3]) # Forma de acceder a una letra en especifico. 

# Longitud. 

print(len(s2)) # Cuenta el numero de letras de una palabra o frase.

# Slicing.

print(s2[2:6]) # Te imprime solo las letras que le especificas que imprima.
print(s2[2:])

# Busqueda.

print("a" in s1) # Sirve para buscar si esas letras estan en la palabra principal.

# Reemplazo.

print(s1.replace("o", "a")) # Sirve para cambiar una letra o palabra.

# Division.

print(s2.split("t")) # Sirve para cortar el lugar donde hay una letra.

# Mayusculas, minusculas y primera letra en mayusculas.

print(s1.upper()) # Para convertir a mayusculas.
print(s1.lower()) # Para convertir a minusculas.
print("paolo conde".title()) # Para convertir las primeras letras en mayusculas.
print("paolo conde".capitalize()) # Para convertir la primera letra en mayusculas.

# Eliminacion de espacios al principio y al final.

print(" Paolo conde ".strip()) # Elimina los espacios.

# Busqueda al principio y al final.

print(s1.startswith("Ho")) # Para confirmar si esa cadena de texto empieza con lo que tu quieres.
print(s1.startswith("Py"))
print(s1.endswith("la")) # Para confirmar si esa cadena de texto acaba con lo que tu quieres.
print(s1.endswith("thon"))

s3 = "Paolo Conde paoloconde05@gmail.com"

# Busqueda de posicion.

print(s3.find("conde")) # Encontrar la posicion desde donde empieza esa palabra.

# Busquedas de ocurriencias.

print(s3.lower().count("o")) # Te dice cuantas veces hay esa letra o palabra.

# Formateo.

print("Saludo: {}, lenguaje: {}".format(s1, s2)) # Expecificar que es cada cosa.

# Interpolacion.

print(f"Saludo: {s1}, lenguaje: {s2}") # Esto esta explicado arriba del todo.

# Trasmorfacion en lista de caracteres.

print(list(s3)) # Crea una lista con todos los caracteres de la variable.

# Transformacion de lista en cadena.

l1 = [s1, ",", s2, "!"] # No entendi casi nada.
print("".join(l1))

# Transformaciones numericas.

s4 = "123456"    # Para transformar una cadena de texto aun entero.
s4 = int(s4)
print(s4)

s5 = "123456.123"   # Para transformar una cadena de texto en un decimal.
s5 = float(s5)
print(s5)

# Comprobaciones varias.

s4 = "123456"
print(s1.isalnum()) # Para saber si es alfanumerica.
print(s1.isalpha()) # Para saber si contiene letras.
print(s4.isalpha())
print(s4.isnumeric()) # para saber si es un numero.

# DIA 5 

"""
Valor y referencia.
"""

# Tipos de datos por valor.

# Muy impotartante en todos los lenguajes.

my_int_a = 10   # Sirve para guardar cuanto vale un valor y que no varie tantas veces.
my_int_b = my_int_a
# my_int_b = 20
# my_int_a = 30
print(my_int_a)
print(my_int_b)

# Tipos de datos por referencia.

# Muy impotartante en todos los lenguajes.

my_list_a = [10, 20]
my_list_b = my_list_a  # Ambas variables apuntan a la misma lista
my_list_b.append(30)   # Se modifica la lista original
print(my_list_a)  # Muestra [10, 20, 30]
print(my_list_b)  # También muestra [10, 20, 30]

# Funciones con datos por valor.

# Muy impotartante en todos los lenguajes.

my_int_c = 10   # Sirve para no modificar el valor.

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funciones con datos por referencia.

# Muy impotartante en todos los lenguajes.

def my_list_func(my_list: list):  # Ambas variables apuntan a la misma lista
    my_list.append(30)     # Se modifica la lista original
    print(my_list)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

# DIA 6

"""
Recursividad.
"""

# Función que hace una cuenta regresiva desde un número hasta 0 usando recursividad
def countdown(number: int):  # Se define la función y se espera un número entero
    if number >= 0:  # Si el número aún es mayor o igual que 0
        print(number)  # Imprime el número actual
        countdown(number - 1)  # Llama a sí misma restando 1 (esto es recursividad)

# Llamamos a la función para empezar desde 100
countdown(100)  # Cuenta regresiva desde 100 hasta 0

"""
Extra
"""


# Función que calcula el factorial de un número (n! = n * (n-1) * (n-2) ... * 1)
def factorial(number: int) -> int:  # Espera un número entero y devuelve otro entero
    if number < 0:  # Si el número es negativo, mostramos un error
        print("Los números negativos no son válidos")
        return 0  # Devolvemos 0 como forma de indicar error
    elif number == 0:  # El factorial de 0 es 1 (por definición matemática)
        return 1
    else:
        return number * factorial(number - 1)  # Multiplica el número por su factorial anterior


print(factorial(5))  # Resultado: 120


# Función que devuelve el número de la secuencia de Fibonacci en cierta posición
def fibonacci(number: int) -> int:  # Espera un número entero y devuelve otro entero
    if number <= 0:  # Si la posición es menor o igual a 0, mostramos un error
        print("La posición tiene que ser mayor que cero")
        return 0
    elif number == 1:  # Primer número en la secuencia es 0
        return 0
    elif number == 2:  # Segundo número en la secuencia es 1
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)  # Suma de los dos anteriores


print(fibonacci(5))  # Resultado: 3


"""
Pilas y colas.
"""

# Pila (LIFO).

# Push
stack = []
stack.append("1") # push , introducir un elemento.
stack.append("2") # push , introducir un elemento.
stack.append("3") # push , introducir un elemento.
print(stack)

# Pop
stack_item = stack[len(stack) - 1] # pop , sirve para desapilar.
del stack[len(stack) - 1] # Sirve para desapilar ese objeto.
print(stack_item)

print(stack.pop()) # Pop , sirve para desapilar el ultimo objeto.

print(stack)

# Cola (FIFO).

queue = []

# enqueue , introducir elementos.
queue.append(1)
queue.append(2)
queue.append(3)

# dequeue , eliminar elementos.
print(queue.pop(0)) # En las colas tienes que especificar que objeto quitar para no quitar el ultimo siempre.
print(queue.pop(1))
print(queue)

"""
Clases.
"""

# Creamos una clase llamada Programmer. Las clases en Python se escriben con mayúscula al principio.
class Programmer:

    surname: str = None

    # Este es el método especial __init__, que se ejecuta automáticamente al crear un objeto de la clase.
    # Sirve para definir los atributos (características) del objeto.
    def __init__(self, name: str, age: int, languaje: list):
        # Guardamos los valores recibidos como atributos del objeto con "self".
        self.name = name       # Guardamos el nombre
        self.age = age         # Guardamos la edad (tú lo habías llamado 'edad', pero abajo usabas 'age')
        self.languaje = languaje  # Guardamos la lista de lenguajes de programación

    # Este es un método que imprime los datos del programador.
    def print(self):
        # Mostramos el nombre, la edad y los lenguajes con un f-string (cadena formateada)
        print(f"Nombre: {self.name} | Apellidos: {self.surname} | Edad: {self.age} | Lenguaje: {self.languaje}")

# Aquí estamos creando un objeto de la clase Programmer con tus datos.
# "Paolo" es el nombre, 16 la edad, y la lista con los lenguajes.
my_programmer = Programmer("Paolo", 16, ["Python", "Dart", "Java"])

# Llamamos al método print para mostrar los datos guardados del objeto.
my_programmer.print()
my_programmer.surname = "Conde"
my_programmer.print()

# DIA 7

"""
Herencia y poliformismo.
"""

# TEMA: HERENCIA Y POLIMORFISMO

# Creamos una clase llamada Animal. Esta será la clase principal (superclase).
# Las demás clases (como Dog y Cat) heredarán de esta.
class Animal:

    # Este es el método constructor de la clase Animal.
    # Se ejecuta automáticamente cuando se crea un objeto de tipo Animal.
    # Toma un parámetro llamado name (nombre del animal) y lo guarda en la variable self.name.
    def __init__(self, name: str):
        self.name = name

    # Este es un método llamado sound() que no hace nada.
    # Está definido aquí para que las clases hijas lo puedan modificar (sobrescribir).
    def sound(self):
        pass  # 'pass' significa que no hace nada (es un método vacío)


# Creamos una subclase llamada Dog (Perro) que hereda de Animal.
class Dog(Animal):

    # Esta función sobrescribe el método sound() de la clase Animal.
    # Es decir, cuando se llame a sound() en un perro, imprimirá "Guau!".
    def sound(self):
        print("Guau!")


# Creamos otra subclase llamada Cat (Gato) que también hereda de Animal.
class Cat(Animal):

    # Esta función también sobrescribe el método sound().
    # Cuando se llame a sound() en un gato, imprimirá "Miau!".
    def sound(self):
        print("Miau!")


# Esta función recibe como parámetro un objeto que sea de tipo Animal o sus subclases.
# Luego llama al método sound() de ese objeto.
# Gracias al polimorfismo, se ejecutará el método correcto según el tipo real del objeto.
def print_sound(animal: Animal):
    animal.sound()


# Creamos un objeto de la clase Animal. Su nombre es "Animal".
# Como la clase Animal no tiene definido un sonido real, no se imprime nada.
my_animal = Animal("Animal")
print_sound(my_animal)

# Creamos un objeto de la clase Dog (perro) con nombre "Perro".
# Al llamar a print_sound, se ejecuta el método sound() de Dog.
# Se imprime "Guau!".
my_dog = Dog("Perro")
print_sound(my_dog)

# Creamos un objeto de la clase Cat (gato) con nombre "Gato".
# Al llamar a print_sound, se ejecuta el método sound() de Cat.
# Se imprime "Miau!".
my_cat = Cat("Gato")
print_sound(my_cat)

"""
EXCEPCIONES.
"""

# Las excepciones permiten capturar errores que ocurren cuando se ejecuta el programa.
# Por ejemplo, dividir entre cero o acceder a un índice inexistente de una lista.

# Este bloque intenta ejecutar operaciones que pueden fallar.
try:
    print(10/0)  # Esto va a producir un error porque no se puede dividir entre 0.
    print([1, 2, 3, 4][4])  # Esto también daría error porque el índice 4 no existe.
except Exception as e:
    # Si ocurre un error, este bloque lo captura y muestra un mensaje indicando el tipo de error.
    # type(e) → da el tipo del error (ej: <class 'ZeroDivisionError'>)
    # type(e).__name__ → saca solo el nombre del error sin todo lo demás (ej: "ZeroDivisionError")
    print(f"Se ha producido un error: {e} ({type(e).__name__})")

"""
MANEJO DE FICHEROS.
"""

import os  # Importamos el módulo 'os', que permite trabajar con archivos del sistema.

# Nombre del archivo que vamos a usar.
file_name = "mouredev.txt"

# Abrimos el archivo en modo escritura ("w" = write).
# Si el archivo no existe, lo crea. Si ya existe, lo borra y lo vuelve a escribir.
with open(file_name, "w") as file:
    # Escribimos tres líneas en el archivo:
    file.write("Itachi\n")  # Primera línea
    file.write("16\n")      # Segunda línea
    file.write("Python")    # Tercera línea (sin salto de línea
    
    # \n , sirve para hacer un salto de linea.


# Abrimos el mismo archivo en modo lectura ("r" = read).
# Leemos todo el contenido y lo imprimimos en pantalla.
with open(file_name, "r") as file:
    print(file.read())

# Eliminamos el archivo del sistema.
os.remove(file_name)

"""
XML Y JSON.
"""

# Importamos los módulos necesarios para trabajar con XML y JSON.
import xml.etree.ElementTree as xml
import json

# Creamos un diccionario con varios datos personales y una lista de lenguajes de programación.
data = {
    "name": "Brais Moure",                         # Clave "name", valor "Brais Moure"
    "age": 36,                                     # Clave "age", valor 36
    "birth_date": "29-04-1987",                    # Clave "birth_date", valor fecha
    "programming_languages": ["Python", "Kotlin", "Swift"]  # Lista como valor
}

# Nombres de los archivos que vamos a crear
xml_file = "mouredev.xml"
json_file = "mouredev.json"

# FUNCIÓN PARA CREAR UN ARCHIVO XML
def create_xml():

    # Creamos el nodo raíz llamado "data"
    root = xml.Element("data")

    # Recorremos todas las claves y valores del diccionario
    for key, value in data.items():
        # Creamos un nodo hijo con el nombre de la clave
        child = xml.SubElement(root, key)

        # Si el valor es una lista (como programming_languages)
        if isinstance(value, list):
            # Creamos un nodo "item" por cada elemento de la lista
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            # Si el valor no es lista, lo convertimos a texto directamente
            child.text = str(value)

    # Creamos el árbol XML completo y lo guardamos en un archivo
    tree = xml.ElementTree(root)
    tree.write(xml_file)

# Llamamos a la función para crear el archivo XML
create_xml()

# Abrimos el archivo XML y mostramos su contenido
with open(xml_file, "r") as xml_data:
    print(xml_data.read())

# Eliminamos el archivo XML
os.remove(xml_file)


# FUNCIÓN PARA CREAR UN ARCHIVO JSON
def create_json():
    # Abrimos el archivo en modo escritura y escribimos el contenido del diccionario como JSON
    with open(json_file, "w") as json_data:
        json.dump(data, json_data) # dump() es una función del módulo json en Python.
# Sirve para guardar (volcar) datos en formato JSON dentro de un archivo.
# Guarda los datos (diccionario, lista, etc.) en un archivo .json
# Lo escribe tal cual tú lo pusiste: con claves y valores bien visibles
# Lo deja bonito y entendible si le pones indent=4
# Evita que se vea todo pegado o mal interpretado
# Es sencillo, no te pide árboles, clases padre, ni hacer rituales 

# Llamamos a la función para crear el archivo JSON
create_json()

# Abrimos el archivo JSON y mostramos su contenido
with open(json_file, "r") as json_data:
    print(json_data.read())

# Eliminamos el archivo JSON
os.remove(json_file)

# DIA 8

"""
Lógica de programación desde cero parte 2.
"""

"""
Pruebas unitarias.
"""

# Tienes que acordarte de que se pone en cada uno.

import unittest # Esto sirve para testear. 

def sun(a, b) -> float: # Esto es como lo que vas a testear que el numero x sumado por el numero y da z.
    if not isinstance(a,(int, float)) or not isinstance(b,(int, float)): # Esto sirve para que el test solo funcione con decimales y numeros enteros.
        raise ValueError("Los argumentos deben ser enteros o decimales.") # Esto te emprime un error ya definido por Python que es el ValueError.
    return a + b 

class TestSum(unittest.TestCase): # En python para poder correr el test necesitas crear esta clase para que funcione.

 def test_sum(self): # Tiene que incluir el nombre test para que se ejucute.
    self.assertEqual(sum(5, 7), 12) # Primero lo dices lo que quieres testear en este caso los dos primeros nuemeros y despues le dices lo que tendria que dar.
    self.assertEqual(sum(5, -7), -2) # Difentes tipos de test.
    self.assertEqual(sum(0, 0), 0) # Difentes tipos de test.
    self.assertEqual(sum(2.5, 2.1), 4.6) # Difentes tipos de test.
    self.assertEqual(sum(2, 2.1), 4.1) # Difentes tipos de test.
    self.assertEqual(sum(2.5, 2.5), 5) # Difentes tipos de test.

    with self.assertRaises(ValueError): # Esto sirve para especificar que de error cuando pasa algo.
         sum("5", 7) # Aqui le dices que de error si pasa esto: sum("5", 7), osino no pasa nada y da True.
    with self.assertRaises(ValueError): 
         sum(5, "7") # Lo mismo que antes pero que de error ahora si pasa esto.
    with self.assertRaises(ValueError): 
         sum("5", "7") # Lo mismo que antes pero que de error ahora si pasa esto.
    with self.assertRaises(ValueError): 
         sum("a", 7) # Lo mismo que antes pero que de error ahora si pasa esto.
    with self.assertRaises(ValueError): 
         sum(None, 7) # Lo mismo que antes pero que de error ahora si pasa esto.

unittest.main() # Esto sirve para llamar al test.

# Apuntes

# def setUp(self) -> None:
#    self. aqui lo que quieres del constesto
# Esto lo que hace esque el programa tenga un contexto de lo que tiene que testear.
# self.assertIn , sirve para comprobar si algo existe.
# self.assertEqual , sirve para comprobar si algo es igual a otra cosa.
# self.assertRaises , sirve para comprobar si algo da error.

"""
Fechas.
"""

# Tienes que acordarte de que se pone en cada uno.

from datetime import datetime # Esto sirve para trabajar con fechas en Python tienes que poner esto siempre antes de trabajar con fechas.

now = datetime.now() # Esto sirve para decirte la hora de este momento la de ahora.
birth_date = datetime(2009, 2, 5, 12, 0, 0) # Esto sirve para añadir a datetime su fecha de nacimiento y hora y el programa lo tranforma, tiene que estar en este orden si o si.

print(now) # Esto lo imprime.
print(birth_date) # Esto lo imprime.

difference = now - birth_date # Esto sirve para calcular los dias que hay entre esas dos fechas.
print(type(difference)) # Esto lo imprime y te dice el tipo que es.

print(f"Tengo: {difference.days // 365} años.") # Para saber cuantos años hay entre las dos fechas.

# Apuntes

# birth_date.strftime("%d %m %y") , esto sirve para formatear la fecha y que aparezca en ese orden importante que tiene que ser con el porcetaje % y la letra minuscula.
# Con la Y mayuscula te pone el año completo no solo los dos ultimos digitos.
# Para horas, minutos y segundo tiene que estar todo en mayuscula.
# Con j te dice el dia del año en el que nacistes.
# Con A te dice el dia del mes en el que nacistes.
# Con h te dice el nombre del mes en el que nacistes en abreviatura.
# Con B te dice el mes del mes en el que nacistes.

"""
Asincronia.
"""

# Tienes que acordarte de que se pone en cada uno.

import datetime # Sirve para trabajar con datas.
import time # Sirve para importan el tiempo que tarda.
import asyncio # Sirve para asegurar de que se corra en segundo plano.

async def task(name: str, duration: int): # Le dices que va haber dentro con una funcion.
    print(f"Tarea: {name}. Duracion: {duration}s. Inicio: {datetime.datetime.now()}") # Le dices lo que imprimir con nombre, duracion y inicio.
    time.sleep(duration) # Le indicas que va pasar un tiempo x entre esas dos acciones.
    print(f"Tarea: {name}. Fin: {datetime.datetime.now()}") # Le indicas cuando acaba.

asyncio.run(task("1", 2)) # Le indicas el tiempo y el nombre de las acciones tambien que se corra de manera asingrona.

#asyncio.run(task("2", 3)) Esta se eyecutaria en segundo plano despues de la primera.
# await , sirve para que cada accion espere a que acabe la anterior.

"""
Expresiones regulares.
"""

# Tienes que acordarte de que se pone en cada uno.

import re # Sirve para poder trabajar con expresiones regulares.

def find_numbers(text: str) -> list: # La funcion para ejucutar la expresion regular.
    re.findall(r"[0-9]+", text) # Expresion regular que tiene que empezar con r y en este caso comprueba si hay nuemros de 0 al 9 y que pueden aparecer 1 o mas veces.

find_numbers("Este es el ejercicio 16 publicado el 15-04-2024.") # Lo que vas a comprobar.

# Apuntes

# 20 Expresiones regulares.

# ^ → Coincide con el inicio de la línea
# $ → Coincide con el final de la línea
# . → Cualquier carácter (excepto salto de 
# línea)
# * → Repite 0 o más veces el elemento 
# anterior
# + → Repite 1 o más veces el elemento 
# anterior
# ? → Hace que el elemento anterior sea 
# opcional (0 o 1 vez)
# {n} → Repite exactamente n veces el 
# elemento anterior
# {n,} → Repite al menos n veces
# {n,m} → Repite entre n y m veces
# [] → Conjunto de caracteres posibles (ej: 
# [aeiou])
# [^] → Niega el conjunto (ej: [^0-9] = no 
# dígitos)
# \d → Coincide con cualquier dígito   
# (equivale a [0-9])
# \D → Todo lo que no es dígito (equivale a 
# [^0-9])
# \w → Cualquier carácter alfanumérico o 
# guión bajo (equivale a [a-zA-Z0-9_])
# \W → Todo lo que no sea alfanumérico ni
# guión bajo
# \s → Cualquier espacio en blanco (espacio, # tab, salto de línea)
# \S → Todo lo que no sea espacio en blanco
# | → Alternancia (ej: perro|gato → coincide # con perro o gato)
# (...) → Agrupa patrones (útil para aplicar # repeticiones o capturas)
# (?P<nombre>...) → Grupo con nombre (para capturar con nombre en vez de número)

"""
Iteraciones.
"""

# Tienes que acordarte de que se pone en cada uno.

# 01 - Utilizar un for.

for i in range(1, 11):
  print(i) # Sirve para inprimir una seguencia o bucle , range sinifica que imprime todos esos numeros o seguencia sin tener en cuenta ese ultimo numero.

# for indica cuantas veces se imprime esa secuencia.

# 03 - Utilizar un while.

i = 0

while i <= 10:
 print(i) # while sirve para imprimir algo si se cumple una condicion exacta.
 i += 1

# 03 - Funcion recursiva / Utilizar una funcion.

def count_ten(i=1): # Funcion para definir lo que vas a hacer en este caso contar.
    if i <= 10: # Le metes un if para que no sea un bucle infinito.
     print(i) # Imprimes el numero.
     count_ten(i + 1) # Al nuemro le sumas 1.
 
count_ten() # Llamas al numero.

# Apuntes

# Diez formas de imprimir una secuencia de nuemeros.

# 1. Bucle for ascendente
# Recorres los números del 1 al 10 sumando de uno en uno.

# 2. Bucle while ascendente
# Mientras el número sea menor o igual a 10, lo vas aumentando y mostrando.

# 3. Lista ya escrita
# Escribes los números manualmente en una lista y la imprimes tal cual.

# 4. Función recursiva
# Una función se llama a sí misma aumentando el número hasta llegar al final.

# 5. Usando range()
# Generas automáticamente una secuencia del 1 al 10 con esa función.

# 6. Bucle for descendente
# Recorres los números del 10 al 1 restando uno cada vez.

# 7. Con una cadena de texto
# Escribes los números como texto separados por espacios y lo imprimes todo junto.

# 8. Usando map()
# Transformas una lista de números con una función y los imprimes.

# 9. Con join()
# Unes los números (convertidos en texto) con espacios en una sola línea.

# 10. Sin bucles, solo con print()
# Escribes todos los números manualmente dentro del print.

"""
Conjuntos.
"""

# Tienes que acordarte de que se pone en cada uno.

data = [1, 2, 3, 4, 5] # Lo que contine la lista en este caso.
print(f"Estructura inicial: {data}.")

data.append(6) # Añadir un elemento.
print(f"Añadiendo elemento al final: {data}.")

data.insert(0, 0) # Añadir al principio, primero pones la posicion y despues el objeto a insertar.
print(f"Añadiendo elemento al principio: {data}.")

data.extend([7, 8, 9]) # Añadir varios objetos de una vez en bloque.
print(f"Añadiendo elemento al final: {data}.")

data[3:3] = [-1, -2, -3] # Añadir varios elementos en una posicion exacta.
print(f"Añadiendo elemento en una posicion: {data}.")

del data[3] # Para eliminar un elemento en concreto.
print(f"Eliminando un elemento en concreto: {data}.")

data[4] = -1 # Para actualizar un elemento en concreto.
print(f"Actualizando un elemento en concreto: {data}.")

print(f"Comprobar si un elemento existe: {-1 in data}.") # Para comprobar si esta ese objeto.

print(f"Eliminar el contenido: {data.clear()}.") # Para eliminar la lista.

# Apuntes

# Union / Conjuntos.
# set_1.union(set_2), esto lo que hace es unirlo un conjunto añade todo solo una vez aunque este repetido, se utiliza con un set con este simbolo {}.
# Intersecion.
# set_1.intersection(set_2), esto lo que hace es una insercion que es coger solo lo que se repite, se utiliza con un set con este simbolo {}.
# Diferencia.
# set_1.difference(set_2), esto lo que hace es una diferencia que es coger solo los que son derentes entre esos dos sets, se utiliza con un set con este simbolo {}.
# Diferencia semetrica.
# set_1.symmetric_difference(set_2), esto lo que hace es una diferencia semetrica que es todo lo que no tienen en comun, se utiliza con un set con este simbolo {}.

"""
Enumeraciones.
"""

# Tienes que acordarte de que se pone en cada uno.

from enum import Enum # Sirve para poder trabajar con las Enumeraciones (Enum).

class Weekday(Enum):
    MONDAY = 1 # En python hay que asignarle un valor a cada clave.
    TUESDAY = 2 # En python hay que asignarle un valor a cada clave.
    WEDNESDAY = 3 # En python hay que asignarle un valor a cada clave.
    THURSDAY = 4 # En python hay que asignarle un valor a cada clave.
    FRIDAY = 5 # En python hay que asignarle un valor a cada clave.
    SATURDAY = 6 # En python hay que asignarle un valor a cada clave.
    SUNDAY = 7 # En python hay que asignarle un valor a cada clave.

def get_day(number: int): # Una funcion para poder trabajar con este caso.
    print(Weekday(number).name) # Esto sirve para llamar al lo que tines en Weeday o puedes hacer esto Weekday.FRIDAY, asi llamas a algo en especifico.

get_day(2) # Llamas a la variable que tenga asignado el numero 2.

# Apuntes (Este ejercicio es dificil para mi.)

# Para poder hacer este ejercicio podemos crear una calse con los diferentes estados, hacer otra clase que sea el order,
# Y decirle lo que necesitamos en una funcion el id y el status y despues crear la varibale order_1 y hay metrele Order y el id y status.
# Despues crear una funcion para cada estado y depues hacer una funcion display donde diga el estado del producto con self.status.name.
# Despues solo arreglas unas cosas en cada funcion para que funcione bien.

"""
Peticiones HTTP.
"""

# Tienes que acordarte de que se pone en cada uno.

import requests # Sirve para poder trabajar con las Peticiones.

response = requests.get("https://moure.dev") # Esto sirve para hacer la peticion al programa.
if response.status_code == 200: # Esto sirve que cuando el codigo de la pagina esta bien osea da 200 imprima el texto.
  print(response.text) 
else:
    print("Error con el codigo.") # Esto sirve para que si la url esta mal no de error te ponga esto.

# Apuntes (Este ejercicio es el mas dificil para mi.) Mins : 2:56:00 - 3:24:00

# Importante este ejercicio sera muy largo y muchas cosas dentro de otras tengo que tener paciencia porque va a dar muchos errores.
# Importante consultar la pagina de pokeapi para hacer este ejercicio.
# print(response), Esto sirve para que te ponga el numero del codigo como el tipico 404 error.
# print(response.text), Esto sirve para ver todo el texto del programa.
# Podemos utilizar una data con response.json para obtener algo en concreto.
# Podemos despues hacer un print entrar al data y dentro del data entrar a algo en especifico por ejemplo el nombre del pokemon.
# Para saber el tipo tenemso que hacer un for type en la data el nombre de lo que vas a buscar en este caso types,
# Y despues emprimes exactamente lo que quieres dentro de esa lista el tipo y el name en este caso.
# Para las evoluciones necesitamso otra url especifica donde aparecen las evoluciones, dodne hace slo mismo que antes el data y el response.json,
# Y dentro de la url entras a evolution_chain y dentro de eso a la url de la evolucion. 
# Si quires ver en los juegos que esta tienes que llamar a la primera url y dentro llamar a game_indices, esto se hace con un data y un for,
# Despues llamas a cada cosa que pone en la pokeapi esto se haria antes de las evoluciones para que no de error y este mejor estructurado todo el codigo.

"""
Callbacks.
"""

# Tienes que acordarte de que se pone en cada uno.

# a 