cansado = ''' 
___▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄_____
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
'''
bem = '''
┈┈┈☆┈┈┈┈
╭╭╮╭╭╮┈┈
┃┃┃┃┃┃☆┈
┃┃┃┃┃┃┈┈
┃┛┻┛┛┃╭╮
┃┈┈╱▔┃┃┃
┃┈╱┈┈┗╯┃
╰┳┊┊┳━━╯
┏┻━━┻┓┈☆
┃┈┈┈┈┃┈┈
┃┈┈┈┈┃┈┈
'''
mal = ''' 
♥ ღ ♥ ღ ♥ ღ ♥ ღ ♥ ღ
♥ ╔══╗ ╔╗╔═╦╦╦═╗ ╔╗╔╗
♥ ╚╗╔╝ ║╚╣║║║║╩╣ ║╚╝║
♥ ╔╝╚╗ ╚═╩═╩═╩═╝ ╚══╝
♥ ╚══╝ …… ღ ♥ kiss ღ
♥ ღ ♥ ღ ♥ ღ ♥ ღ ♥ ღ'''

def greet(name, location = ""):
    resposta = input("Bom dia, como está se sentindo hoje?\nDigite 'cansado' para incentivos fofos, 'bem' para mensagem alegre ou 'mal' para mensagens de motivação.\n>").lower()
    if resposta == "cansado":
        print(f"Um ursinho pra te alegrar {name} de {location} <3\n{cansado}")
    elif resposta == "bem":
        print(f"Toca aqui parceiro! Continue assim {name} de {location}.\n{bem}")
    elif resposta == "mal":
        print(f"Eu te amo, nunca se esqueca disso {name} de {location}!\n{mal}")
    else:
        print("Mensagem inválida.")

greet(location = "Quixadá", name = "Emilly")     