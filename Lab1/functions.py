
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