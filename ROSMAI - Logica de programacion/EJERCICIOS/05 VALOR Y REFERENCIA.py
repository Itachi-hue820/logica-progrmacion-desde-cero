# EJERCICIO
# Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
# su tipo de dato.
# Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
# por referencia, y cómo se comportan en cada caso en el momento de ser modificadas.
# (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

# DIFICULTAD EXTRA (opcional)
# Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
# Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
# se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
# variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
# Comprueba también que se ha conservado el valor original en las primeras.

# Mi codigo.

# Valor.

# Vi el video de mourodev lo entendi lo hice yo solo sin ver y algunas cosas pequeñas las veia porque se me olvidaban.

def value(value_a: int, value_b: int) -> tuple:
    temp = value_a  # temp , sirve para guardar algo 
    value_a = value_b
    value_b = temp 
    return value_a, value_b

my_int_a = 120
my_int_b = 460

my_int_c , my_int_d = value(my_int_a, my_int_b)
print(f"{my_int_a}, {my_int_b}")
print(f"{my_int_c}, {my_int_d}")

# Referencia.
 
def value(value_a: list, value_b: list) -> tuple:
    temp = value_a  # temp , sirve para guardar algo 
    value_a = value_b
    value_b = temp 
    return value_a, value_b

my_list_a = [10, 20]
my_list_b = [30, 40]
 
my_list_c , my_list_d = value(my_list_a, my_list_b)
print(f"{my_list_a}, {my_list_b}")
print(f"{my_list_c}, {my_list_d}")