import functions

print("Hello World")

first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
opr = input("Введите операцию: ")

rez, firstFromFunc, secondFromFunc = functions.operation(first, second, opr)
print("Ответ: ", rez, ".С числами ", firstFromFunc, " и ", secondFromFunc)
