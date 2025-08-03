# El sombrero selector [Harry potter].

# Mi codigo.

question_1 = int(input(
  "Enter your answer (1-4): \n" 
  "Q1) Do you like Dawn or Dusk?\n"
  "1) Dawn\n"
  "2) Dusk\n"
  "Respuesta: "))
question_2 = int(input(
  "Q2) When Im dead, I want people to remember me as:\n"
  "1) The Good\n"
  "2) The Great\n"
  "3) The Wise\n"
  "4) The Bold\n"
  "Respuesta: "))
question_3 = int(input(
  "Q3) Which kind of instrument most pleases your ear?\n"
  "1) The violin\n"
  "2) The trumpet\n"
  "3) The piano\n"
  "4) The drum\n"
  "Respuesta: "))

my_dict: dict = { 
  "Slytherin": 0,
  "Hufflepuff": 0,
  "Ravenclaw": 0,
  "Gryffindor": 0
}

if (question_1 < 1 or question_1 > 4 or \
question_2 < 1 or question_2 > 4 or \
question_3 < 1 or question_3 > 4):
  print("Escoge una opcion del 1 al 4, porfavor.")
else:
  if question_1 == 1:
   my_dict["Slytherin"] += 4
  if question_2 == 1:
   my_dict["Slytherin"] += 4
  if question_3 == 1:
   my_dict["Slytherin"] += 4
  
  if question_1 == 2:
   my_dict["Hufflepuff"] += 4
  if question_2 == 2:
   my_dict["Hufflepuff"] += 4
  if question_3 == 2:
   my_dict["Hufflepuff"] += 4

  if question_1 == 3:
   my_dict["Ravenclaw"] += 4
  if question_2 == 3:
   my_dict["Ravenclaw"] += 4
  if question_3 == 3:
   my_dict["Ravenclaw"] += 4

  if question_1 == 4:
   my_dict["Gryffindor"] += 4
  if question_2 == 4:
   my_dict["Gryffindor"] += 4
  if question_3 == 4:
   my_dict["Gryffindor"] += 4

print(my_dict)