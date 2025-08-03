# Tuve que ver dos pequeños detalles que no me acuerdo que fue exactamente pero fueron cosas pequeñas.
# 1 Fallo 

# Factorial.

def factorial(number: int) -> int:
    if number < 0:
     print("Los numeros negativos no son validos")
     return 0
    elif number == 0: 
      return 1
    else:
      return number * factorial(number - 1)
    
print(factorial(5))
print(factorial(0))

# Fibonacci.

def fibonacci(number: int) -> int:
  if number <= 0:
     print("La posicion tiene que ser mayor que cero.")
     return 0
  elif number == 1:
    return 0
  elif number == 2:
    return 1
  else:
    return fibonacci(number - 1) + fibonacci(number - 2) # Me confundi y puse multiplicar el numero por el fibonacci osea puse esto, 
  # return number * fibonacci(number - 1) + fibonacci(number - 2) pero era esto return fibonacci(number - 1) + fibonacci(number - 2),
  # Lo supe cuando revise es codigo con el de mourodev y vi que era diferente esa parte.

print(fibonacci(5))
print(fibonacci(0))