print('''
        |\    o""O, /\/\ \ .
         \|   (..< B /  ) | )
          \\__|\-| {/  _| '
           \__| `||/\,-
        _____ '((: \ \      ___
   __--- o . ---__  )|     >_-
 _-.  O   o   . o -=/ )-_ //
(_---___________---_)_____/
       /vwwwv\     \  |
        |   |       \ \___
    ____|   |  _     \c_-.\
   |/ \ \   |/| \         \>
_|___\_\ \__\_|__.__/~_______
''')
print("Welcome to Fairy Forest.")
print("Your mission is to find the fairy.") 

choice1 = input('You\'re at a fairy forest. Where do you want to go? Type "left" or "right" \n>').lower()
if choice1 == "left" :
    choice2 = input('You\'ve come to a beautiful tree. There is an light in the middle of the tree. Type "scream" to wait someone response. Type "ignore" to move away. \n>').lower()
    if choice2 == "scream" :
     choice3 = input("You get into the tree. There is a fairy with 3 potions. One white, one pink and one violet. Which colour do you choose? \n>").lower()
     if choice3 == "white" :
           print("You felt sick and then didn't remember anything, Do fairies exist? Game Over >:c")
     elif choice3 == "pink" :
           print("You became a beautiful and cute fairy! You Win!!!! <3")
     else :
           print("You became a gothic and charm fairy. Great choice... You win?")
    else :
       print("You left the forest and missed the opportunity of see fairies. Game Over. ;v")
else :
   print("You got lost. Game Over :c ")