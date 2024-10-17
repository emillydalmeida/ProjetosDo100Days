import art 

def soma(a,b):
    return a+b

def diminuicao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

operacoes = {
    "+": soma,
    "-": diminuicao,
    "*": multiplicacao,
    "/": divisao,
}

def calculadora():
    print(art.logo)

    coontinuar_calculando = True

    prime_numero = float(input("Qual o primeiro número?\n> "))

    while coontinuar_calculando:
        
        operador = input("Qual o operador?\n+\n-\n*\n/\n> ")
        segun_numero = float(input("Qual o número?\n> "))

        resposta = operacoes[operador](prime_numero, segun_numero)

        print(f"{prime_numero} {operador} {segun_numero} = {resposta}")

        escolha = input("Digite 's' para continuar calculando, ou 'n' para recomeçar.\n> ")

        if escolha == "s":
            prime_numero = resposta
        else:
            coontinuar_calculando = False
            print("\n" *20)
            calculadora()

calculadora()
