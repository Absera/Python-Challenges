# Absera # This function returns a reversed string!

def reverse(string):
    
    list = [] 
    listLength, stringLength = len(string), len(string)
    newString = ''

    for i in range(stringLength):
        while listLength > 0:
            list.append(string[listLength-1])
            listLength -= 1
    for newChar in list:
        newString += newChar

    print(newString)

def run(): 
    while True:
        string = input('> ')
        reverse(string)
        
print('Enter A String To Be Reversed!\n')
while True:                
    run()





