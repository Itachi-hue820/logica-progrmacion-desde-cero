# Esto fue hecho viendo el video de mourodev ya que no sabia como hacerlo pero fue todo entendido.

def my_agenda():
    
 agenda = {}

 while True:

     print("1. Buscar contacto")
     print("2. Insertar contacto")
     print("3. Actualizar contacto")
     print("4. Eliminar contacto")
     print("5. Salir")

     option = input("\nSeleciona una opcion: ") # Para que puedas escribir en la terminal.

     match option:
        case "1":
            name = input("Introduce el nombre del contacto a buscar: ")
            if name in agenda:
               print(f"El numero de telefono de {name} es {agenda[name]}.")
            else:
               print(f"El contacto {name} no existe.")
        case "2":
           name = input("Introduce el nombre del contacto: ")
           phone = input("Introduce el telefono del contacto: ")
           if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
              agenda[name] = phone
           else:
              print("Debes introcudir un numero de telefono con menos de 12 digitos.")
        case "3":
           name = input("Introduce el nombre del contacto a actualizar: ")
           if name in agenda:
              phone = input("Introduce el telefono del contacto: ")
              if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                agenda[name] = phone
              else:
                print("Debes introcudir un numero de telefono con menos de 12 digitos.")
           else:
                print(f"El contacto {name} no existe.")
        case "4":
         name = input("Introduce el nombre del contacto a eliminar: ")
         if name in agenda:
            del agenda[name]
         else:
            print(f"El contacto {name} no existe.")
        case "5":
          print("Saliendo de la agenda.")
          break # Sirve para salir del bucle.
        case _: 
          print("Opcion no valida. Elige una opcion del 1 al 5.")

my_agenda()