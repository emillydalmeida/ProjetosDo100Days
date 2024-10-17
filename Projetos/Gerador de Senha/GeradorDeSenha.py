import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas!")
num_letras= int(input("Quantas letras você gostaria de ter na sua senha?\n> ")) 
num_simbolos = int(input(f"Quantos simbolos você gostaria de ter na sua senha?\n> "))
num_numeros = int(input(f"Quantos números você gostaria de ter na sua senha?\n> "))

password = ""

for i in range(1, num_letras + 1):
    password = password + random.choice(letras)

for i in range(1, num_simbolos + 1):
    password = password + random.choice(simbolos)

for i in range(1, num_numeros + 1):
    password = password + random.choice(numeros)

quantidade = int(num_letras)+ int(num_simbolos) + int(num_numeros)

new_password = ""

for i in range (1, quantidade + 1):
    new_password = new_password + random.choice(password)

print(f"Sua nova senha é : {new_password}")  