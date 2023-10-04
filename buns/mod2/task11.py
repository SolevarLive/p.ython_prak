numbers= input("Введите числа: ")
flag = False

for num in range(0, len(numbers),2):
    for digit in range(0, len(numbers),2):
        if numbers[num] == numbers[digit + 2]:
            print(True)
            flag=True
            break
        else:
            print(False)
            flag=True
            break
    if flag:
        break