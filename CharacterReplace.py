# this program replaces a charcter with new character in a string

def replace(string, char, newChar):
        
    stringList = []
    itemIndex = None
    newString = ''
    # stringLength = len(string)
    for i in string:
        stringList.append(i)
    for i in stringList:
        lowerChar = char.lower()
        lowerItem = str(i).lower()
        if str(i) == lowerChar or lowerItem == lowerChar:
            index = stringList.index(i)
            itemIndex = index
            stringList[itemIndex] = newChar

    for i in stringList:
        newString += i
        
    print(newString)
    
def getInputs():
    string = input('Enter a string: ')
    char = input('Enter character to be replaced: ')
    newChar = input('New character to replace the above character: ')
    
    return [string, char, newChar]
inputs = getInputs()
replace(inputs[0], inputs[1], inputs[2])

