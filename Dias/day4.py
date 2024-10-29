#aprender sobre a aleatoriedade

#import random

#random_integer = random.randint(1, 10)
#print(random_integer)

#main_no_lol = ["Nami", "Ahri", "Lulu", "Morgana", "Soraka", "Janna", "Karma", "Lux", "Sona", "Seraphine"]
#main_no_lol.append("Le'Blanc") #adiciona um objeto ao final da lista
#main_no_lol.insert(2, "Yone") #adiciona um objeto num lugar especifico
#main_no_lol.remove("Yone") #remove um objeto da lista
#main_no_lol.pop() #remove o ultimo objeto da lista, pode ser a posição dele também
#main_no_lol.clear() #limpa a lista inteira
#main_no_lol.sort() #sorteia os elementos da lista
#main_no_lol.reverse() #ordem decrescente dos elementos
#champhions_preferidos = main_no_lol.copy() #cria uma copia da lista
#print(main_no_lol)
#print(champhions_preferidos)
#print(main_no_lol.pop)

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

map = [["⬜️","️⬜️","️⬜️"], ["⬜️","⬜️","️⬜️"], ["⬜️️","⬜️️","⬜️️"]]

if position == "A1":
  line1[0] = "X"
elif position == "A2":
  line2[0] = "X"
elif position == "A3":
  line3[0] = "X"
elif position == "B1":
  line1[1] = "X"
elif position == "B2":
  line2[1] = "X"
elif position == "B3":
  line3[1] = "X"
elif position == "C1":
  line1[2] = "X"
elif position == "C2":
  line2[2] = "X"
else :
  line3[2] = "X"
  

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
