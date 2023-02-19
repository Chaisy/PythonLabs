
def operation(x, y, z):
    if (z == 'add'):
        return x+y, x, y
    elif (z == 'div' and x > y):
        return x/y, x, y
    elif (z == 'div' and x < y):
        return y / x, x, y
    elif (z == 'mult'):
        return x * y, x, y
    elif(z == 'sub' and x > y):
        return x-y, x, y
    elif (z == 'div' and x < y):
        return y - x, x, y
    else:
        return print("Такой операции нет"), x, y

def evenNumbers(list, newList):
    for num in list:
        if int(num) % 2 == 0: newList.append(num)
        else: int(num)+1
    if len(newList)==0 : return "Нет четных"
    else : return newList
