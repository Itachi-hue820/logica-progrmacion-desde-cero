# EJERCICIO
# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.

# DIFICULTAD EXTRA (opcional)
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).
# - Calcular el valor de un elemento concreto (según su posición) en la 
#   sucesión de Fibonacci (la función recibe la posición).

# Mi código

# Factorial.

def factorial(number: int) -> int: # La flecha significa que retorna en lo que defines.
    if number < 0:
     print("Los numeros negativos no son validos")
     return 0 
    elif number == 0:
     return 1
    else: 
      return number * factorial(number - 1) # Se me olvido poner el return. 

print(factorial(5))
print(factorial(0))

# Fibonacci.

def fibonacci(number: int) -> int:
  if number <= 0: # Se me olvido el igual.
     print("La posicion tiene que ser mayor que cero.")
     return 0 
  elif number == 1:
    return 0 
  elif number == 2:
    return 1
  else: 
    return fibonacci(number - 1) + fibonacci(number - 2) # Se me olvido el mas.
  
print(fibonacci(5))