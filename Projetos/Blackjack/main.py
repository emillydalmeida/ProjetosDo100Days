import random
from art import logo


def dar_cartas():
    """Retorna uma carta aleatoria do baralho"""
    baralho = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(baralho)
    return carta


def calcular_pontos(cards):
    """Calcula os pontos de uma lista"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


def comparar(pontos_u, pontos_c):
    """Compara os pontos de usuario e computador"""
    if pontos_u == pontos_c:
        return "Empate :c"
    elif pontos_c == 0:
        return "Perdeu, o oponente fez um Blackjack :c"
    elif pontos_u == 0:
        return "Parabéns, você ganhou com um Blackjack :>"
    elif pontos_u > 21:
        return "Você passou de 21, perdeu :c"
    elif pontos_c > 21:
        return "O oponente passou de 21, você venceu :>"
    elif pontos_c > pontos_u:
        return "Você perdeu :c"
    else:
        return "Você venceu :>"


def jogar():
    print(logo)
    
    cartas_usuario = []
    cartas_computador = []

    pontos_computador = -1
    pontos_usuario = -1

    acabou_o_jogo = False

    for _ in range(2):
        cartas_usuario.append(dar_cartas())
        cartas_computador.append(dar_cartas())

    while not acabou_o_jogo:
        pontos_usuario = calcular_pontos(cartas_usuario)
        pontos_computador = calcular_pontos(cartas_computador)

        print(f"\nSuas cartas: {cartas_usuario}, seus pontos: {pontos_usuario}")
        print(f"\nPrimeira carta do computador: {cartas_computador[0]}")

        if pontos_usuario == 0 or pontos_computador == 0 or pontos_usuario > 21:
            acabou_o_jogo = True
        else:
            escolha = input("\nGostaria de puxar outra carta? 's' para puxar e 'n' para parar.\n> ")
            if escolha == "s":
                cartas_usuario.append(dar_cartas())
            else:
                acabou_o_jogo = True

    while pontos_computador != 0 and pontos_computador < 17:
        cartas_computador.append(dar_cartas())
        pontos_computador = calcular_pontos(cartas_computador)

    print(f"\nSua mão final: {cartas_usuario}, seus pontos finais: {pontos_usuario}")
    print(f"\nMão final do oponente: {cartas_computador}, pontos finais do oponente: {pontos_computador}\n")
    
    print(comparar(pontos_usuario, pontos_computador))


while input("\nQuer jogar Blackjack? 's' para jogar e 'n' para recusar.\n> ") == 's':
    print("\n" * 20)
    jogar()