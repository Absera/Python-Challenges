# Absera # maximum() returns maximum number in a list

def maximum(list) :
    listLength = len(list)
    if listLength >= 2 :
        if list[0] >= list[1] :
            list.pop(1)
        else :
            list.pop(0)
        try :
            maximum(list)
        except :
            pass
    else :
        return list[0]
    
    return list[-1]


def minimum(list):
    listLength = len(list)
    if listLength >= 2:
        if list[0] <= list[1]:
            list.pop(1)
        else:
            list.pop(0)
        try:
            minimum(list)
        except:
            pass
    else:
        return list[0]
    
    return list[-1]


list1 = [1, 3, 5, 4, 8, 9, -3, 2, 10, 123]
list2 = list1.copy()
print(f'List: {list1}')
print(f'Maximum: {maximum(list1)}')
print(f'Minimum: {minimum(list2)}')






