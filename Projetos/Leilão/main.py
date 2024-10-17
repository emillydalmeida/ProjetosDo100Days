leilão = True

dicionario_valores = {}

def maior_oferta(oferta_dicionario):
    vencedor = ""
    oferta_mais_alta = 0
    for ofertador in dicionario_valores:
        oferta = oferta_dicionario[ofertador]
        if oferta > oferta_mais_alta:
            oferta_mais_alta = oferta
            vencedor = ofertador

    print(f"O vencedor é {vencedor}, com um total de R$ {oferta_mais_alta} ofertados.")

while leilão:
    print("Bem vindo ao leilão.")
    pessoa = input("Qual o seu nome?\n> ").lower()
    valor = int(input("Qual o valor da sua oferta?\nR$ "))

    dicionario_valores[pessoa] = valor

    continua = input("Mais alguém irá ofertar? Sim ou Não\n> ").lower()

    if continua == "não":
        leilão = False
        maior_oferta(dicionario_valores)
    elif continua == "sim":
        print("\n" *20)
    else:
        print("Resposta inválida")
        print("\n" *20)

