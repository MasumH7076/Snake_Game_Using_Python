# import random

# def game():
#     pass 

# randNo = random.randint(1,5)
# print(randNo)

import random
# Snake Water Gun or Rock paper Scissors
def gamewin(comp, you):

    # If two value are equal, declare a tie!
    if comp == you:
        return None
    
    # Check for all posibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
        
     # Check for all posibilities when computer chose w
    elif comp == 'w':
        if  you == 'g':
            return False
        elif you == 's':
            return True
        
    # Check for all posibilities when computer chose g
    elif comp == 'g':
            if you == 's':
                return False
            elif you == 'w':
                return True
            
print("comp turn: Sanke(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input ("your turn: Sanke(s) Water(w) or Gun(g)?: ")
a = gamewin(comp, you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")