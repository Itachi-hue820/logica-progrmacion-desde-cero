# Mi codigo freestyle.

int = 3
print(int)
float = 3.647292
print(float)
bool = True
print(bool)
bool = False
print(bool)
string = "Hola, mundo."
print(string)

"""
Hola, guapos y guapas.
"""

outher_string = "Hola, Python"
print(outher_string)

for number in range (1, 101):
    if number % 3 and number % 6:
        print(number)

my_int = 3
print(int)
my_int += 2
print(int)
my_int -= 5
print(int)
my_int *= 2
print(int)
my_int /= 9
print(int)
my_int **= 7
print(int)

print("Hola, Python")

print(f"AND: 10 + 3 == 13 and 10 + 4 == 13 es: {10 + 3 == 13 and 10 + 4 == 13}")
print(f"AND: 10 + 3 == 13 and 10 + 4 == 14 es: {10 + 3 == 13 and 10 + 4 == 14}")
print(f"OR: 10 + 3 == 13 or 10 + 4 == 12 es: {10 + 3 == 13 or 10 + 4 == 12}")
print(f"OR: 10 + 3 == 13 or 10 + 4 == 14 es: {10 + 3 == 13 or 10 + 4 == 14}")
print(f"NOT: not 10 + 3 == 13 es: {10 + 3 == 13}")

print(f"Igualdad: 10 == 3 {10 == 3}")
print(f"Desigualdad: 10 != 3 {10 != 3}")
print(f"Igual o mayor que: 10 >= 3 {10 >= 3}")
print(f"Igual o menor que: 10 <= 3 {10 <= 3}")

my_dict: dict = { 
    "name":"Paolo",
    "age":"16",
    "lenguaje":"Python"
}
print(my_dict)
del my_dict["age"]
print(my_dict)
my_dict["surname"] = "Itachi"
print(my_dict)

my_list = ["Paolo", "Christian", "Mourodev"]
print(my_list)
my_list[1] = "Thegregf"
print(my_list)
my_list.remove("Paolo")
print(my_list)
my_list.sort
print(my_list)

tuple = ["Paolo", "16", "paoloconde05@gmail.com"]
print(tuple)

s1 = "Hola"
s2 = "Python"

print(s2[2:5])
print(s1[0:2])

print(s2[0] + s2[1] + s2[2] + s2[3] + s2[4] + s2[5])
print(s1.replace("o", "a"))

my_int_a = 10
my_int_b = 20
my_int_b = my_int_a

print(my_int_a, my_int_b)
  

def my_list_func(my_list: list):
         
 my_list_c = [10, 20, 30]

 my_list.append(30)

 print(my_list_c)
 
try:
   print(10 / 0)
except: 
   print("Se a producido un error.")
finally:
   print("Ha finalizado el manejo de excepciones") 
 