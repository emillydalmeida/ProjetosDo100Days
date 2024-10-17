# Local Scope

def drink_potion():
    potion = 2
    print(potion)

drink_potion()
print(drink_potion) #não consegue acessar a variável potion dentro do escopo local

#Global Scope

player_health = 10
 
def drink_potion():
    potion = 2
    print(player_health)

drink_potion() 

#Modificando variáveis globais

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")