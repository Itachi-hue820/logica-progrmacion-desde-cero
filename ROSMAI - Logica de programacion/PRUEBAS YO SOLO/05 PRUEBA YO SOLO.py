# Valor.

def value(value_a: int, value_b: int) -> tuple: # lo de tuple porque lo puse con a envez de con e.
    temp = value_a 
    value_a = value_b
    temp = value_b 
    return value_a, value_b # Se me habia olvidado.

my_int_a = 120
my_int_b = 340

my_int_c, my_int_d = value (my_int_a, my_int_b) # Se me habia olvidado lo de los parentesis.
print(f"{my_int_a}, {my_int_b}")
print(f"{my_int_c}, {my_int_d}")

# Referencia.

def value(value_a: list, value_b: list) -> tuple:
    temp = value_a 
    value_a = value_b
    temp = value_b 
    return value_a, value_b

my_list_a = [10, 20]
my_list_b = [30, 40]

my_list_c, my_list_d = value (my_list_a, my_list_b) 
print(f"{my_list_a}, {my_list_b}")
print(f"{my_list_c}, {my_list_d}")