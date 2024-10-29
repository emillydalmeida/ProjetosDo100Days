#Notas sobre meu aprendizado ao decorrer do curso, dia 2
numb_char = len(input("What is your name?\n> "))
#type casting é a troca de tipos de dados
new_numb_char = str(numb_char) #str muda o tipo de dado para str, float muda pra float e assim vai...
print("Your name has " + new_numb_char + " characters") #precisa ser str pq o print só usa um tipo de dado

#lissão 2 
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print( int(two_digit_number[0]) + int(two_digit_number[1]) )

#operações em python existe o ** que é a mesma coisa de elevar ao expoente 2 ** 3 = 8 em vez de 6

round(8/3, 2) #arredonda 8 dividido pra 3 em até duas casas após a virgula

score = 0
height = 1.90
isWinning = True 

print(f"Your score is {score}, your height is {height} and you are winning is {isWinning}")


