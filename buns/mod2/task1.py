numbers = input("Введите числа через запятую: ")
comma_index = None
for i in range(len(numbers)):
    if numbers[i] == ",":
        comma_index = i
        break
a = int(numbers[:comma_index])
b = int(numbers[comma_index+1:])
remainder = a % b
print(remainder)