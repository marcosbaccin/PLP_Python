import random

n = int(random.randrange(1, 49))
guess = int(input('Enter you guess '))
while n != guess:
    if guess > n:
        print('Go lower')
        guess = int(input('Enter you guess again '))
    else:
        print('Go higher')
        guess = int(input('Enter you guess again '))
print('Great! You win champ ', n)
