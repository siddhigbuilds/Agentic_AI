import random
numrand=random.randint(1,50)

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 50")

for ch in range(3,0,-1):
    n=int(input("\n Guess the number "))
    if(n>50 or n<1):
        print("enter number between 1 to 50 !!")
    elif(n==numrand):
        print("congrats u gussed the number")
    elif(n>numrand):
        print("try again no is small!try smaller one")
        ch-=1
        print("Remaining chances:", ch)
    elif(n<numrand):
        print("try again no is to big! try larger one")
        ch-=1
        print("Remaining chances:", ch)
    
    else:
        break

if ch == 0:
    print("😢 Game Over!")
    print("The correct number was:", numrand)



