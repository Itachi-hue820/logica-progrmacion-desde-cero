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