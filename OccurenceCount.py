# Absera #returns the number of occurence of an integer in a list
def occurence(list, item):
    count = 0

    for i in list:
        if i == int(item):
            count += 1
    
    print(count)
    
def getList():
    listLength = input('How much elements: ')
    list = []
    for i in range(int(listLength)):
        element = input(f'element: ')
        list.append(int(element))
    
    return list

def getItem():
    
    item = input('Number to be counted: ')
    return int(item)

list = getList()
item = getItem()
occurence(list, item)