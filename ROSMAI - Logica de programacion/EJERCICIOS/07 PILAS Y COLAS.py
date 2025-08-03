# EJERCICIO
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).

# DIFICULTAD EXTRA (opcional)
# Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
# de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
# que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
# Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
# el nombre de una nueva web.
# Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
# impresora compartida que recibe documentos y los imprime cuando así se le indica.
# La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
# interpretan como nombres de documentos.

# Mi código

# Fallos: 2

def web_navegation():

    stack = []

    while True:

        action = input("Añade alguna url o interactua con la web con las palabras adelante, atras, salir.")
    
        if action == "salir":
            print("Saliendo del navegador de la web.")
            break
        elif action == "adelante":
            pass
        elif action == "atras":
            if len(stack) > 0:
             stack.pop()
        else:
            stack.append(action)
         
        if len(stack) > 0:

           print(f"Has navegado a la web: {(stack[len(stack) - 1])}")

        else:
            print("Estas en la pagiande inicio.")


# web_navegation()

# Fallos: 4

def shared_printed():

    queue = []

    while True:

        action = input("Añade un documento o imprimir o salir.")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
             print(f"Imprimiendo: {queue.pop(0)}")
        else: 
            queue.append(action)
            
        print(f"Cola de impresion: {queue}")


shared_printed()