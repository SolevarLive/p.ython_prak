def get_armstrong_numbers():
    for num in range(10, 100000):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            yield num

armstrong_gen = get_armstrong_numbers()
def  get_armstrong_numberss():
    return next(armstrong_gen)
for i in range(8):print(get_armstrong_numberss(), end=' ')