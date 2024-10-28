# Requisitos
# - Printar os recursos
# - Checar se tem recursos o suficiente
# - Processar moedas
# - Checar se a transação foi válida
# - Fazer o café
# - Atualizar os recursos

MENU = {
    "expresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "custo": 1.5,
    },  
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "custo": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 18,
        },
        "custo": 3.0,
    }
}

moedas = 0 

recursos = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}


def recursos_suficientes(ingredientes_bebida):
    for item in ingredientes_bebida:
        if ingredientes_bebida[item] >= recursos[item]:
            print(f"Desculpa, não há {item} o suficientes.")
            return False
    return True


def checar_moedas():
    print("Por favor, insira as moedas. ->Expresso R$1.5 ->Latte R$2.5 ->Cappuccino R$3.0")
    total = int(input("Quantas moedas de 1 real?")) *1.00
    total += int(input("Quantas moedas de 50 centavos?")) *0.50
    return total


def transacao_sucedida(dinheiro_recebido, valor_bebida):
    if dinheiro_recebido >= valor_bebida:
        troco = round(dinheiro_recebido - valor_bebida, 2)
        if troco > 0:
            print(f"Aqui está o troco: R${troco}")
        global moedas
        moedas += valor_bebida
        return True
    else: 
        print("Desculpa, não há dinheiro o suficiente. Dinheiro devolvido.")
        return False


def fazer_cafe(nome_bebida, ingredientes_bebida):
    for item in ingredientes_bebida:
        recursos[item] -= ingredientes_bebida[item]
    print(f"Aqui está o seu {nome_bebida}☕. Aproveite!")


ligar = True

while ligar:
    comando = input("Qual café você gostaria de tomar? (expresso/latte/cappuccino)\n> ")

    if comando == "off":
        ligar = False
    elif comando == "report":
        print(f"Água: {recursos['agua']}ml")
        print(f"Leite: {recursos['leite']}ml")
        print(f"Café: {recursos['cafe']}g")
        print(f"Dinheiro: R${moedas}")
    else:
        bebida = MENU[comando]
        if recursos_suficientes(bebida["ingredientes"]):
            pagamento = checar_moedas()
            if transacao_sucedida(pagamento, bebida['custo']):
                fazer_cafe(comando, bebida["ingredientes"])
