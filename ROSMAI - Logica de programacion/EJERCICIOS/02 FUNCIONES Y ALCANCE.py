 # EJERCICIO:
 # Crea ejemplos de funciones básicas que representen las diferentes
 # posibilidades del lenguaje:
 # Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 # Comprueba si puedes crear funciones dentro de funciones.
 # Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 # Pon a prueba el concepto de variable LOCAL y GLOBAL.
 # Debes hacer print por consola del resultado de todos los ejemplos.
 # (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 # DIFICULTAD EXTRA (opcional):
 # Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 # La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 # Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 # Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 # Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 # La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 # Mi codigo.

def countSometing (texto1, texto2): # Hecho por chatgpt lo de Someting.
   
    contador_numeros = 0 # Hecho por chatgpt.

    for number in range (1, 101):
        if number % 3 == 0 and number % 5 == 0: # Ayuda de chatgpt por los espacios que no lo sabia. 
             print(texto1 + texto2)
        elif number % 3 == 0:      # Ayuda de chatgpt por los espacios que no lo sabia. 
             print (texto1)
        elif number % 5 == 0:      # Ayuda de chatgpt por los espacios que no lo sabia. 
             print (texto2)
        else:                       
             print(number) 
             contador_numeros +=1 # Ayuda de chatgpt porque no se me acurria como hacerlo.

    return contador_numeros 

resultado = countSometing("texto1", "texto2") # Hecho por chatgpt. 
print(resultado)
