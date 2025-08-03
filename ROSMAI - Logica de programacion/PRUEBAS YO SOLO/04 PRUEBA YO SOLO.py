# Copiado por mourodev porque no sabia como hacerlo.

def check(word1 : str, word2: str): # Sirve para indicar que vas a comprobar.

# Palindromos

   print(f"{word1} es palindromo: {word1 == word1[::-1]}")  # Sirve para que lo ponga al reves y revisar si es igual.
   print(f"{word1} es palindromo: {word2 == word2[::-1]}")  # Sirve para que lo ponga al reves y revisar si es igual.

# Anagramas

   print(f"{word1} es anagrama de {word2}: {sorted(word1) == sorted(word2)}")
   # Sirve para ordenarlos y si cuando los ordenas son iguales pues da True.

# Isogrmas 

   print(f"{word1} es isograma de: {len(word1) == len(set(word1))}")
   print(f"{word2} es isograma de: {len(word2) == len(set(word2))}")


check("radar", "python")
check("amor", "roma")