def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_power(a * a, n // 2)
    else:
        return a * fast_power(a, n - 1)

a = int(input("Введите число: "))
n = int(input("Введите степень: "))

result = fast_power(a, n)
print(result)