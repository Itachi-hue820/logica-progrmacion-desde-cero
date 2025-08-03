# 🧠 Proyecto: Sistema Ultra Completo de Gestión de Academia Virtual  
# 🔧 Python puro | ❌ Sin GUI | ❌ Sin DB | ✅ Terminal + Archivos `.json/.txt`  

# ----------------------------------------------------

# ✅ FASE 1: Registro y Login de Usuarios

# 🎯 Objetivo:
# Crear un sistema que permita a usuarios registrarse e iniciar sesión.

# 🛠️ Qué tiene que hacer:

# - Crea una función que pida por consola: nombre, email y contraseña.
# - Simula la verificación del email mostrando un mensaje tipo "email verificado".
# - Comprueba que la contraseña sea segura: mínimo 8 caracteres, una mayúscula, un número.
# - Identifica si el usuario es estudiante, profesor o administrador al registrarse.
# - Permite iniciar sesión verificando los datos (email + contraseña).
# - Si fallan 3 veces, bloquea (simulado por consola). 
# - Guarda el usuario actual como “sesión activa”.

# ----------------------------------------------------

# ✅ FASE 2: Roles y Permisos

# 🎯 Objetivo:
# Controlar lo que puede ver y hacer cada tipo de usuario.

# 🛠️ Qué tiene que hacer:

# - Crea clases separadas para estudiante, profesor y admin.
# - Cada clase debe tener métodos según lo que puede hacer cada rol.
# - Al iniciar sesión, muestra un menú diferente dependiendo del rol.
# - Si es admin, permite cambiar de rol a otro usuario (simulado).

# ----------------------------------------------------

# ✅ FASE 3: Gestión de Cursos

# 🎯 Objetivo:
# Crear y gestionar cursos.

# 🛠️ Qué tiene que hacer:

# - Crea una función que permita crear cursos (nombre, código único, cupo).
# - Permite ver todos los cursos disponibles con su info.
# - Permite editar el nombre/cupo o eliminar un curso.
# - Permite asignar un profesor a un curso.
# - Muestra qué cursos están activos o inactivos.

# ----------------------------------------------------

# ✅ FASE 4: Inscripción de Estudiantes

# 🎯 Objetivo:
# Permitir a los alumnos inscribirse en cursos.

# 🛠️ Qué tiene que hacer:

# - Función para inscribirse a un curso.
# - Permite cancelar la inscripción.
# - Muestra los cursos a los que está inscrito el alumno.
# - Muestra los alumnos inscritos en cada curso.

# ----------------------------------------------------

# ✅ FASE 5: Evaluaciones y Certificados

# 🎯 Objetivo:
# Asignar y calificar tareas.

# 🛠️ Qué tiene que hacer:

# - Crear tareas por curso.
# - Profesores califican las tareas de cada estudiante.
# - Calcula la nota final por curso.
# - Si supera el 60%, genera un certificado (texto en consola).

# ----------------------------------------------------

# Mi codigo.

# ✅ FASE 1

def regristro():
     
   while True:
     option = int(input(
       "Antes de nada digame que eres y escoja una de estas tres opciones, porfavor: \n" 
       "1) Añadir usuario\n"
       "2) Añadir email\n"
       "3) Añadir contraseña\n"
       "4) Registrarse con email y contraseña\n"
       "5) salir\n"
     ))

     match option:
      case"1":
       identificacion = int(input(
       "Antes de nada digame que eres y escoja una de estas tres opciones, porfavor: \n" 
       "1) Estudiante\n"
       "2) Profesor\n"
       "3) Administrador\n"
       ))
       print(f"Se a guardado el nombre de identificacion: {identificacion}")
       usuario = input("Introduzca su nombre de usuario: ")
       print(f"Se a guardado el nombre de usuario: {usuario}")
       sesion_activa = usuario
       print(f"Se a iniciado sesion con el usuario: {sesion_activa}")
      case"2":
       email = input("Introduzca su email: ")
       print(f"Se a guardado el email: {email}")
      case"3":
       contraseña = input("Introduzca su contraseña: ")
       tiene_mayus = False
       tiene_numeros = False      # Desde la linea 175 - 185 osea lo de comprobar la contraseña,
       for letra in tiene_numeros:  
        if letra.isupped():       # Lo vi por chatgpt porque no se me ocurria pero no lo copie tal cual lo modifique un poco.
         tiene_mayus = True
        elif letra.isdigit():
         tiene_numeros = True
       if len(contraseña) >= 8 and tiene_mayus and tiene_numeros:
        print("Contaseña valida.")
       else:
        print("Contaseña invalida necesita tener 8 caracteres una mayuscula y numeros.")
      case"4":
         email = input("Introduzca su email: ")
         print(f"Se a guardado el email: {email}")
         contraseña = input("Introduzca su contraseña: ")
         tiene_mayus = False
         tiene_numeros = False
         for letra in tiene_numeros:
          if letra.isupped():
            tiene_mayus = True
          elif letra.isdigit():
           tiene_numeros = True
         if len(contraseña) >= 8 and tiene_mayus and tiene_numeros:
          print("Contaseña valida.")
         else:
          print("Contaseña invalida necesita tener 8 caracteres una mayuscula y numeros.")
      case"5":
        print("Saliendo del programa.")
        break
      case _:
         print("Opcion no valida, escoja una del 1 al 5 porfavor.")

# Esto de abajo lo vi por chatgpt porque no se me ocurria pero no lo copie tal cual lo modifique un poco.

intentos = 0 

while True:
 if intentos == 1:
   print("Te quedan dos intentos.")
 elif intentos == 2:
   print("Te queda un intento.")
 else: 
   intentos == 3
   print("Usuario bloqueado por demasiados intentos.")

# ✅ FASE 2

 class Jerarquia:
    def __init__(self, name: str):
        self.name = name

 class Estudiante(Jerarquia):
   usuario = input("Introduzca su nombre de usuario: ")
   contraseña = input("Introduzca su contraseña: ")
   identificacion = input("Introduzca su identificacion: ")

   while True:
     option = int(input(
     "Selecione una de estas cuatro opciones: \n" 
     "1) Ver perfil.\n"
     "2) Enviar trabajo.\n"
     "3) Ver calificaciones\n"
     "4) Salir\n"
     ))

     match option:
      case"1":
       print(f"Tu nombre de usuario es: {usuario}, tu contraseña: {contraseña} y tu rol: {identificacion}.")
      case"2":
        trabajo = input("Introduzca el nombre del trabajo: .")
        print(f"El trabajo: {trabajo}, se a guardado correctamente.")
      case"3":
        print("Tus calificaciones son: Excelentes bro muy bien hecho maquina.")
      case"4":
        print("Saliendo del programa.")
        break
      case _:
        print("Opcion no valida, escoja una del 1 al 4 porfavor.")

 class Profesor(Jerarquia):
   usuario = input("Introduzca su nombre de usuario: ")
   contraseña = input("Introduzca su contraseña: ")

   while True:
     option = int(input(
     "Selecione una de estas cuatro opciones: \n" 
     "1) Ver listado de alumnos.\n"
     "2) Enviar trabajo.\n"
     "3) Ver calificaciones\n"
     "4) Salir\n"
     ))

     match option:
      case"1":
       print("Tus alumnos son: Juan, Pablo, Martina, Christian y Hector.")
      case"2":
        alumno = input("Introduzca el nombre del alumno a calificar: .")
        nota = input("Introduzca la nota a dar: .")
        print(f"El alumno: {alumno}, tiene la nota: {nota}.")
      case"3":
        aviso = input("Introduzca el aviso para el alumnado: .")
        print(f"El aviso: {aviso}, a sido enviado correctamente.")
      case"4":
        print("Saliendo del programa.")
        break
      case _:
        print("Opcion no valida, escoja una del 1 al 4 porfavor.")

 class Administrador(Jerarquia):
   usuario = input("Introduzca su nombre de usuario: ")
   contraseña = input("Introduzca su contraseña: ")

   while True:
     option = int(input(
     "Selecione una de estas cuatro opciones: \n" 
     "1) Ver listado de alumnos.\n"
     "2) Ver personas registradas.\n"
     "3) Cambiar de identificacion\n"
     "4) Salir\n"
     ))

     match option:
      case"1":
       eliminado = input("Introduzca el usuario a eliminar: .")
       print(f"El usuario: {eliminado}, a sido eliminado correctamente.")
      case"2":
        print("Usuarios registrados: Paolo (Estudiante), Carla (Profesor), Martina (Admin).")
      case"3":
        indentificacion = input("Introduzca la nueva identificacion: .")
        print(f"Ahora eres parte de: {indentificacion}, enorabuena.")
      case"4":
        print("Saliendo del programa.")
        break
      case _:
        print("Opcion no valida, escoja una del 1 al 4 porfavor.")

# ✅ FASE 3

 class Dictionary:
    
    def __init__(self):
        self.dict = ()

 my_dict_1: dict = {        
    "name":"Python desde cero", 
    "codico_unico":"63028157", 
    "cupo":"60 personas", 
    "name":"Java desde cero", 
    "codico_unico":"93529618", 
    "cupo":"40 personas",
    "name":"C# desde cero", 
    "codico_unico":"84530275", 
    "cupo":"120 personas",
   }

 while True:
     option = int(input(
       "Antes de nada digame que eres y escoja una de estas tres opciones, porfavor: \n" 
       "1) Asignar profesores\n"
       "2) Ver los cursos disponibles\n"
       "3) Cambiar curso\n"
       "4) Cambiar cupo\n"
       "5) Eliminar curso\n"
       "6) Salir\n"
     ))

     match option:
       case"1":
        profesor = input("Introduzca al profesor: .")
        my_dict() = {profesor}
        print(f"El profesor: {profesor}, a sido añadido correctamente.")
        Curso = input("Introduzca el curso para el profesor: .")
        my_dict() = {Curso}
        print(f"El curso: {Curso}, a sido añadido correctamente.")
        print(f"El profesor: {profesor} a sido asigando al curso: {Curso}.")
       case"2":
         print(f"Estos son los cursos disponibles: {my_dict_1}.")
       case"3":
         curso_2 = input("Introduzca el curso a cambiar: .")
         if curso_2 in my_dict_1:
          del dict[curso_2]
         else:
           print(f"El curso: {curso_2}, no existe.")
         curso_new = input("Introduzca el curso a nuevo: .")
         my_dict() = {curso_new}
         print(f"As cambiado el curso: {curso_2}, por el curso: {curso_new}.")
       case"4":
         cupo_2 = input("Introduzca el cupo a cambiar: .")    
         if cupo_2 in my_dict_1:
          del dict[cupo_2]
         else:
           print(f"El curso: {cupo_2}, no existe.")   # Esto lo de si no existe lo sabia pero se me oldivo por eso lo vi por chatgpt pero no lo copie tal cual lo modifique un poco.
         cupo_new = input("Introduzca el cupo nuevo: .")
         if cupo_new == isnumeric():    # Esto lo de si es numerico lo vi por chatgpt porque no sabia como hacerlo pero no lo copie tal cual lo modifique un poco.
           my_dict_1[cupo_2] = cupo_new
           print(f"As cambiado el cupo: {cupo_2}, por el cupo: {cupo_new}.")
         else:
          print("Tiene que ser numerico, intentalo otra vez.") 
       case"5":
         eliminado = input("Introduzca el curso a eliminar: .")
         if curso_2 in my_dict_1:
          del dict[eliminado]
         else:
           print(f"El curso: {eliminado}, no existe.")
         print(f"El curso: {eliminado}, a sido eliminado correctamente.")
       case"6":
        print("Saliendo del programa.")
        break
       case _:
        print("Opcion no valida, escoja una del 1 al 6 porfavor.")
       
# ✅ FASE 4

 def inscricion():
   
  my_dict_cursos: dict =()

  my_dict_alum: dict = {        
    "Paolo", 
    "Andreina", 
    "Gabriel", 
    "Eduardo", 
    "Carolina", 
    "Martina",
    "Sofia", 
    "Christian", 
    "Hector",
   }

  while True:
     option = int(input(
       "Escoja una de estas opciones: \n" 
       "1) Curso al que estas inscrito\n"
       "2) Ingresar un curso\n"
       "3) Inscribirse a un curso\n"
       "4) Alumnos totales\n"
       "5) Salir\n"
     ))

     match option:
       case"1":
         name = input("Introduzca su nombre: .")
         # Desde aqui lo vi por chatgpt.
         encontrado = False  # Esto lo vi por chatgpt pero lo entendi.
         for curso, my_dict_alum in curso.items(): # Esto lo vi por chatgpt pero lo entendi.
          if name in my_dict_alum: # Esto lo vi por chatgpt pero lo entendi.
           print(f"El usuario: {name}, esta en el curso: {curso}.") # Esto lo vi por chatgpt pero lo entendi.
           encontrado = True # Esto lo vi por chatgpt pero lo entendi.
           break
         if not encontrado: # Esto lo vi por chatgpt pero lo entendi.
          # Hasta aqui lo vi por chatgpt.
          print(f"El usuario: {name}, no se a encontrado su curso asegurate de estar inscrito antes.")  
       case"2":
         curso = input("Introduzca el curso a añadir: .")
         my_dict_cursos() = {curso}
         print(f"A añadido el curso: {curso}.")
       case"3":
         name = input("Introduzca su nombre: .")
         my_dict_alum() = {name} 
         curso = input("Introduzca el curso: .")
         if curso in my_dict_cursos:
          print(f"El usuario: {name}, a inscresado al curso: {curso}.")
         else:
           print(f"El curso al que estas intentado inscribirte: {curso}, no existe primero añadalo.")
       case"4":
         print(f"Todos los usuarios inscritos son estos: {my_dict_alum}.")
       case"5":
        print("Saliendo del programa.")
        break
       case _:
        print("Opcion no valida, escoja una del 1 al 5 porfavor.")

# ✅ FASE 5

 def nota():
   
   my_dict: dict =()
   
   while True:
     option = int(input(
       "Escoja una de estas opciones: \n" 
       "1) Añadir tu nota\n"
       "2) Ver la media\n"
       "3) Ver si estas aprobado\n"
       "4) Salir\n"
     ))

     match option:
       case"1":
         notas = input("Introduzca su nota: .")
         my_dict() = {notas}
         print(f"La nota: {notas}, a sida guardada.")
       case"2":
         if my_dict == 0:
           print("Necesitas dos o mas notas para poder calcular la media.")
         else:
          media = sum(notas) / len(notas) # Necesite un poco de ayuda porque me lie poniendo un elif.
          print(f"Tu media es: {media}.")
       case"3":
         if my_dict == 0:
           print("Necesitas una nota primero.")
         elif nota <= 6:
           print("Felicidades has aprobado la signatura :) .")
         else:
           print("Lo siento has suspendido mas suerte la proxima vez :( .")
       case"4":
        print("Saliendo del programa.")
        break
       case _:
        print("Opcion no valida, escoja una del 1 al 3 porfavor.")
