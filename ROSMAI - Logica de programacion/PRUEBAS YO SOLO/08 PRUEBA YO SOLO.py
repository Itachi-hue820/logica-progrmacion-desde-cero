class Stack:
    
    def __init__(self):
        self.stack = []
        
name = input("Inserte tres nombres: ")

while True:
     option = int(input(
     "Selecione una de estas tres opciones: \n" 
     "1) insertar\n"
     "2) eliminar\n"
     "3) salir\n"
     ))

     match option:
         case"1":
             name = input("Inserte la palabra: ")
             self.stack.append(name)  # Esto lo vi por chatgpt porque se me habia olvidado.
             print(f"La palabra: {name}, a sido insertada correctamente.")
         case"2":
             if len(self.stack) > 0: # Esto lo vi por chatgpt.
              eliminada = self.stack.pop() # Esto lo vi por chatgpt.
              print(f"La palabra: {eliminada}, a sido eliminada correctamente.")
             else:
              print("La pila esta vacia.")
         case"3":
          print("Saliendo del programa.")
          break 

my_stack()
         
class Queue:
    
    def __init__(self):
        self.queue = []

name = input("Inserte tres nombres: ")

while True:
     option = int(input(
     "Selecione una de estas tres opciones: \n" 
     "1) insertar\n"
     "2) eliminar\n"
     "3) salir\n"
     ))

     match option:
         case"1":
             name = input("Inserte la palabra: ")
             self.queue.append(name)  
             print(f"La palabra: {name}, a sido insertada correctamente.")
         case"2":
             if len(self.queue) > 0: 
              eliminada = self.queue.pop(0) # Esto lo vi por chatgpt.
              print(f"La palabra: {eliminada}, a sido eliminada correctamente.")
             else:
              print("La cola esta vacia.")
         case"3":
          print("Saliendo del programa.")
          break 

#my_queue()

# Creo que esta todo bien pero no lo e comprobado 