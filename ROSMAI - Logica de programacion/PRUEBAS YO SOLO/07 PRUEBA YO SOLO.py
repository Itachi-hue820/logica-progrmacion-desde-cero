# Fallos: 5 [{(stack[len(stack)] - 1)}")] me confundi en un simbolo, [stack.append(action)] se me olvido el action
# [if len(stack) > 0:] me confundi de donde hiba y lo puse mal, meti primero el while envez del stack asi que me daba error la sintaxis.
# erroes tipicos de los espacios mal puestos.
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

# Fallos: 2 se me habia olvidado estas cosas: print(f"Imprimiendo: {queue.pop(0)}") la parte de imprmir lo de queue y pop 0 me lo sabia.
# queue.append(action), print(f"Cola de impresion: {queue}") 

def shader_printed():

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

shader_printed()