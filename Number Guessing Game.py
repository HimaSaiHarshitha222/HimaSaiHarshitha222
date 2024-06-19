from random import *
secnum = randint(1,50)
print("Hey... I'm thinking of a number between 1 and 50")
print("Can you Guess it in 5 Chances")
c = 0
for i in range(5):
    c += 1
    num = int(input('Your Guess: '))
    if num>secnum:
        print("Guess is High")
    elif num<secnum:
        print("Guess is Low")
    else:
        break
if num==secnum:
    print(f"Congratulations :-) You have Guessed the Number in {c} chances")
else:
    print("Better Luck Next Time :-( ")
    print("Secret Number is",secnum)
