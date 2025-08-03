import os

my_dict: dict = ()

file_name = "gestion_de_ventas.txt"

my_dict = int(input("Añada un producto con su cantidad y su precio."))

while True:
     option = int(input(
     "Selecione una de estas tres opciones: \n" 
     "1) Añadir.\n"
     "2) Actualizar.\n"
     "3) Eliminar.\n"
     "4) Calcular total de ventas.\n"
     "5) Imprimir todos los productos.\n"
     "6) Salir.\n"
     ))
    
     match option:
      case"1":
         insercion = input("Indique el producto a añadir: ")
         objeto_2 = my_dict["insercion"] = ()
         print(f"El producto: {objeto_2}, a sido añadido correctamente.")
      case"2":
         if len(my_dict) > 0:
          objeto_2 = input("Indique el producto a actualizar: ")
          objeto_3 = my_dict["objeto_2"] = ()
          print(f"El producto: {objeto_2}, a sido actualizado correctamente.")
          print(f"El producto: {objeto_3}, ahora esta en la lista.")
      case"3":
         if len(my_dict) > 0:
          objeto = input("Indique el producto a eliminar: ") 
          del my_dict["objeto"]
          print(f"El producto: {objeto}, a sido eliminada correctamente.")
      case"4":
         if len(my_dict) > 0:
          calculo_1 = int(input("Indique el producto a calcular: "))
          calculo_2 = int(input("Indique el producto a calcular con el otro: "))
          calculo_total = calculo_1 + calculo_2
          print(f"La suma de esos dos productos es: {calculo_total}")
      case"5":
         if len(my_dict) > 0: 
          with open(file_name, "r") as file:
           print(file.read())  
      case"6":
         os.remove(file_name)
         break
      case _:
         print("Opcion no valida.")