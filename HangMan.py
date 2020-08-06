import random

score = 0
listOfStrings = ['STRING', 'GAMERS', 'EXTORTION', 'PLAYER', 'GUESSING', 'HOOK', 'GOOD']
displayedString = ''
hiddenCharacter = ''
while True:
    string = random.choice(listOfStrings)
    stringLength = len(string)
    list = [char for char in string]
    randomIndex = random.randint(0, stringLength-1)
    hiddenCharacter += list[randomIndex]
    list[randomIndex] = '_'
    for char in list:
        displayedString += char


    userInput = input(f'{displayedString} ')
    if userInput.capitalize() == hiddenCharacter:
        print('Nice!')
        score += 1
    else:
        print(f'The character was {hiddenCharacter}.')
        print(f'You scored {score}')
        break