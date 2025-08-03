# EJERCICIO
# Explora el concepto de manejo de excepciones según tu lenguaje.
# Fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el programa se detenga de manera inesperada.
# Prueba a dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.

# DIFICULTAD EXTRA (opcional)
# Crea una función que sea capaz de procesar parámetros, pero que también
# pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
# corresponderse con un tipo de excepción creada por nosotros de manera
# personalizada, y debe ser lanzada de manera manual) en caso de error.
# Captura todas las excepciones desde el lugar donde llamas a la función.
# Imprime el tipo de error.
# Imprime si no se ha producido ningún error.
# Imprime que la ejecución ha finalizado.

# Mi codigo.

class Error_1:
 def __init__(self, number: int):
    pass

 try:
     dividendo = int(input("Indique un dividendo: "))
     divisor = int(input("Indique un divisor: "))
     cociente = dividendo / divisor
     print(f"La solucion a esa division es: {cociente}") 
 except Exception as e:
     print(f"Se ha producido un error: {e} ({type(e).__name__})")
 else:
    print("La ejecucion a finalizado.")

class Error_2:
 def __init__(self):
    self.my_list = [] # Esto lo vi por chatgpt.

 try:
    my_list = input("Introduzca tres nombres: ")
    busqueda = input("Busque uno de esos tres nombres: ")
    print(f"El nombre que as buscado es este verdad: {busqueda}") 
 except Exception as e:
     print(f"Se ha producido un error: {e} ({type(e).__name__})")
 else:
    print("La ejecucion a finalizado.")

class Error_3:
 def __init__(self, number: int):
    pass

 try:
     number_1 = int(input("Indique un numero para sumar: "))
     number_2 = int(input("Indique otro numero para sumar: "))
     resultado = number_1 + number_2
     print(f"La solucion a esta suma es: {resultado}")
 except Exception as e:
     print(f"Se ha producido un error: {e} ({type(e).__name__})")
 else:
    print("La ejecucion a finalizado.")

g1 = Error_1()
g2 = Error_2()
g3 = Error_3()

g1.error_1() 

# Creo que esta todo bien pero no lo e comprobado 
