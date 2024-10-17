import random
from art import logo

print(logo)
print("Bem-vindo ao Adivinhe o Número!\n")
print("Estou pensando em um número entre 1 e 100\n")

numeros = list(range(1,101))

numero = random.choice(numeros)

print(numero)

def adivinhar():
    
    vida = 0
    
    nivel = input("Escolha uma dificuldade. Digite 'facil' ou 'dificil'.\n> ")
    if nivel == "facil":
        vida = 10
        print(f"\nVocê tem {vida} tentativas para adivinhar o número.")
    elif nivel == "dificil":
        vida = 5
        print(f"\nVocê tem {vida} tentativas para adivinhar o número.")
    else:
        print("Resposta não válida.")
        return

    numero_tentativa = int(input("\nChute um número: "))

    
    while numero_tentativa != numero and vida > 0:
        if numero_tentativa != numero and nivel == "facil":
            if numero_tentativa > numero:
                print("\nMenor que esse...")
            elif numero_tentativa < numero:
                print("\nMaior que esse...")
            else:
                return
                    
            vida -= 1
            print(f"Restam {vida} tentativas para adivinhar o número.")
    
        if numero_tentativa != numero and nivel == "dificil":
            if numero_tentativa > numero:
                print("\nMenor que esse...")
            elif numero_tentativa < numero:
                print("\nMaior que esse...")
            else:
                return
                    
            vida -= 1
            print(f"\nRestam {vida} tentativas para adivinhar o número.")

        numero_tentativa = int(input("\nChute um número: "))

        if vida == 1:
            vida -= 1
            print("\nVocê esgotou todas as tentativas, perdeu (╬ ˘̀^˘́ ) ")
            return
    
    if numero_tentativa == numero:
                print("\nParabéns você adivinhou. (  * ꒳ *)っ⌒♡｡．♡︎")
        
    


adivinhar()