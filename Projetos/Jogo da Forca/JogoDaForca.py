import random
import lista
import artes

mostrar = []
resposta = random.choice(lista.campeoes).lower()
tamanho = len(resposta)
erros = []
vida = 6

print(f"\nBem vindo(a) ao {artes.logo} de League of Legends\n")

for _ in range (tamanho):
    mostrar += "_"

fim_de_jogo = False

while not fim_de_jogo:

    letra_escolhida = input("\nQual letra você escolhe?\n> ").lower()

    if letra_escolhida in mostrar:
        print(f"\nVocê ja digitou {letra_escolhida}, tente outra.")

    for posicao in range(tamanho):
        letra = resposta[posicao]
        if letra  == letra_escolhida:
            mostrar[posicao] = letra 

    if letra_escolhida not in resposta:
        print(f"\nVocê chutou '{letra_escolhida}' e não está na palavra, perdeu uma vida")
        vida -= 1
        if vida == 0:
            fim_de_jogo = True
            print(f"\nVocê perdeu... :c {artes.perdeu}")

    print(f"\n{' '.join(mostrar)}")

    if "_" not in mostrar:
        fim_de_jogo = True

    if fim_de_jogo == True and vida > 0:
        print(f"\nVocê venceu!! :D {artes.venceu}")
    
    print(f"{artes.forca[vida]}\nVidas restantes: {vida}")



    
