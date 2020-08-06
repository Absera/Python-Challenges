
import random

number = int(random.randint(1, 9))
count = 0
runnig = True
while runnig:
    guessedNumber = int(input('> '))
    if guessedNumber < number:
        print('Too low')
        count += 1
    elif guessedNumber > number:
        print('Too high')
        count += 1
    elif guessedNumber == number:
        print('Exactly')
        print(f'You have tried {count} times.')
        