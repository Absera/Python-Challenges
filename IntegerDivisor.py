number = input('Number: ')
for i in range(int(number) + 1):
    if i != 0:
        if int(number) % int(i) == 0:
            print(i)
        