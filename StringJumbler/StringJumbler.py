# Jumble up a given string
import random
import json

print('''
                            WELCOME TO THIS GAME
        TAKE A GUESS OF THE BELOW WORD BASED ON THE HINT IN FRONT OF IT  
          ''')

score = 0
def jumble(string, hint) :
    global score
    firstLetter = string[0]
    lastLetter = string[-1]
    stringList = [char for char in string] 
    stringList.pop(0)
    stringList.pop(-1)

    randomizedStringList = []
    for i in range(0, len(stringList)) :
        randomChar = random.choice(stringList)
        randomizedStringList.append(randomChar)
        stringList.pop(stringList.index(randomChar))


    randomizedString = ''
    for char in randomizedStringList :
        randomizedString += char
    firstLetter += randomizedString
    firstLetter += lastLetter
    
    print(firstLetter + ' ---- ' + hint)
    userGuess = input('> ')
    if userGuess == string :
        print('+1')
        score += 1
    elif userGuess.lower() == string.lower() :
        print('small letter - do not do it again')
        
    else:
        print(f'GAME OVER -- YOU SCORE {score}')
        quit()
    
# wordList = ['Hello', 'Brother', 'Example', 'Graduation', 'Nitrogen', 'Jumbling', 'Vocablury']
# wordDict = {
#     'Hello':'Hi', 
#     'Brother':'Sister', 
#     'Example':'Instance', 
#     'Graduation':'College', 
#     'Nitrogen': '71%', 
#     'Jumbling' : 'This game',
#     'Vocablury' : 'Related to this game'
#     }   
with open('StringJumbler\words.json') as file:
    wordDict = json.load(file)
    wordDict = wordDict['words']
randomItems = [item for item in wordDict]
items = []

for item in wordDict :
    items.append(random.choice(randomItems)) # needs review
    
for item in items:
    jumble(item, wordDict[item])
print('YOU WON ALL!')