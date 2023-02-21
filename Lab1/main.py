import functions

print("Hello World")

first = functions.getNumber(input("Введите первое целое число: "))
second = functions.getNumber(input("Введите второе целое число: "))
opr = input("Введите операцию: ")

rez, firstFromFunc, secondFromFunc = functions.operation(int(first), int(second), opr)
print("Ответ: ", rez, ".С числами ", firstFromFunc, " и ", secondFromFunc)

spis = functions.getList(input("Введите список ").split())
newSpis = []
rezult = functions.evenNumbers(spis, newSpis)
print("Список четных чисел: ", rezult)