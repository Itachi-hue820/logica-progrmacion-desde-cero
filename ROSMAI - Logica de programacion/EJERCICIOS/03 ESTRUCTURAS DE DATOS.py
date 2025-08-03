 # EJERCICIO:
 # Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 # Utiliza operaciones de inserción, borrado, actualización y ordenación.

 # DIFICULTAD EXTRA (opcional):
 # Crea una agenda de contactos por terminal.
 # Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 # Cada contacto debe tener un nombre y un número de teléfono.
 # El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 # los datos necesarios para llevarla a cabo.
 # El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 # (o el número de dígitos que quieras)
 # También se debe proponer una operación de finalización del programa.

# Mi codigo.

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