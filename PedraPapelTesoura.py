import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
resposta = int(input("Bem vindo(a) ao joguinho!\nQual você escolhe? Escreva 0 para pedra, 1 para papel e 2 para tesoura.\n>"))
if resposta == 0:
    print(rock)
elif resposta == 1:
    print(paper)
else:
    print(scissors)

aleatoriedade = [rock, paper, scissors]

numero_aleatorio = random.randint(0,2)

print("O Computador escolheu:\n")

if numero_aleatorio == 0:
    print(aleatoriedade[0])
elif numero_aleatorio == 1:
    print(aleatoriedade[1])
else:
    print(aleatoriedade[2])

if resposta == 0 and numero_aleatorio == 1:
    print("PERDEUU KKKKKKKKK")
elif resposta == 0 and numero_aleatorio == 2:
    print("Você venceu =D")
elif resposta == numero_aleatorio:
    print("Empate :/")
elif resposta == 1 and numero_aleatorio == 0:
    print("Você venceu =D")
elif resposta == 1 and numero_aleatorio == 2:
    print("PERDEUU KKKKKKKKK")
elif resposta == 2 and numero_aleatorio == 0:
    print("PERDEUU KKKKKKKKK")
elif resposta == 2 and numero_aleatorio == 1:
    print("Você venceu =D")
else:
    print("Esse numero não pode")



