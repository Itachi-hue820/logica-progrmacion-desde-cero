class Jerarquia:
    def __init__(self, name: str):
        self.name = name

    def jerarquia(self):
     pass

class Gerentes(Jerarquia):
    name = "Jose"
    identificador = "86043718"
    def jerarquia(self):
        print("Gerente: supervisa la estrategia global del sitio web.")
    def empleados(self):
        print("Empleados a su cargo: ")
        print("1. Jose Luis - Desarolla la app movil.")
        print("2. Andrea - Diseña el fornted.")
        print("3. Mario - Se encarga de la base de datos.")

class Gerentes_de_proyectos(Jerarquia):
    name = "Mourodev"
    identificador = "29402674"
    def jerarquia(self):
        print("Gerente de proyectos: lidera el equipo de desarollo del sitio web.")
    def empleados(self):
        print("Empleados a su cargo: ")
        print("1. Martina - Programador - Se encarga de la interfaz del usuario de la aplicacion.")
        print("2. Gabriel - Programador - Programa las funciones del sistema de regristro.")
        print("3. Carolina - Programador - Realiza pruebas y corrige errores del codigo.")

class Programadores(Jerarquia):
    name = "Paolo"
    identificador = "54530264"
    def jerarquia(self):
        print("Programador: escribe codigo en Python para la aplicacion movil.")

# La asignacion.

g1 = Gerentes()
g2 = Gerentes_de_proyectos()
p3 = Programadores()

# La llamada.

g1.jerarquia()
g2.jerarquia()
p3.jerarquia()