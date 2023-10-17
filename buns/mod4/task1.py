def check_numbers(numbers):
    all_equal = True
    all_different = True
    numbers_set = set(numbers)

    if len(numbers_set) == 1:
        print("Все числа равны")
    elif len(numbers_set) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

 # Пример использования
numbers = [2, 2, 3, 4, 5]
check_numbers(numbers)