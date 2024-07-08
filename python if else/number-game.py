from random import randint

number = randint(0,10)

while True:
    guess = input('What is your guess?  ')
    guess = int(guess)

    if guess > number:
        print(f'{guess} is Too High')
    elif guess < number:
        print(f'{guess} Too Low')
    else:
        print(f'{guess} is RIGHT')
        break