
def operation(x, y, z):
    if (z == 'add'):
        return x+y, x, y
    elif (z == 'div' and x > y):
        if not y : return print("делить на 0 нельзя!!!"), x, y
        return x/y, x, y
    elif (z == 'div' and x < y):
        if not x: return print("делить на 0 нельзя!!!"), x, y
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
    if not len(newList) : return "Нет четных либо вы не ввели список"
    else : return newList

def getNumber (a):
    while True:
        if a.isdigit() : return a
        else: return getNumber(input("Попробуйте снова: "))


def getList (a):
    while True:
        for num in a:
            if not num.isdigit() : return getList(input("Был введен некорректный список, попробуйте снова: ").split())
        return a