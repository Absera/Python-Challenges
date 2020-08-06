# Absera # this program returns a length of a string without builin functions

def length(string):
    length = 0

    for char in string:
        length += 1
        
    print(length)

while True:
    string = input('Enter string: ')
    length(string) 