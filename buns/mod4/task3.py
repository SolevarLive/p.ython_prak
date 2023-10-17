def evklid(a, b):
    if b == 0:
        return a
    else:
        return evklid(b, a % b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = evklid(a, b)
print(result)