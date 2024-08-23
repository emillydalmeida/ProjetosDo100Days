import art

print(art.logo)

funcao = input("\nEscreva 'codificar' para criptografar, escreva 'decodificar' para descriptografar.\n>").lower()

texto = input("\nEscreva sua mensagem.\n>").lower()

indice = int(input("\nEscreva o índice.\n>"))

texto_lista = list(texto)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

criptografado = []

if indice > 26:
    indice = indice % 26
elif indice == 26:
    indice = indice + 1

def caeser(para_funcao, para_texto, para_indice):

    if para_funcao != "codificar" and para_funcao != "decodificar":
        print("Entrada inválida. Permitido somente 'codificar' ou 'decodificar'")

    for char in para_texto:
        if char in alfabeto:
            numero = alfabeto.index(char)
            if para_funcao == "codificar":
                numero += para_indice
            elif para_funcao == "decodificar":
                numero -=para_indice
            criptografado.append(alfabeto[numero])
        else:
            criptografado.append(char)

    if para_funcao == "codificar":
        print(f"\nO texto codificado é: {''.join(criptografado)}")
    else:
        print(f"\nO texto decodificado é: {''.join(criptografado)}")

caeser(para_funcao = funcao, para_texto = texto_lista, para_indice = indice)

print("\nTchauzinho", art.adeus)
