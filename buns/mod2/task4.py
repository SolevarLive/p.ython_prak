number = int(input("Введите число: "))


def make_notation(number, notation):
    num = ""
    while number > 0:
        remainder = number % notation
        num = str(remainder) + num
        number //= notation

    return num

def make_hexadecimal(number):
    num = ""
    while number > 0:
        remainder = number % 16
        if remainder < 10:
            num = str(remainder) + num
        else:
            if remainder == 10:
                num = 'A' + num
            elif remainder == 11:
                num = 'B' + num
            elif remainder == 12:
                num = 'C' + num
            elif remainder == 13:
                num = 'D' + num
            elif remainder == 14:
                num = 'E' + num
            elif remainder == 15:
                num = 'F' + num
        number //= 16

    return  num

binary = make_notation(number, 2)
octan = make_notation(number, 8)
hexa = make_hexadecimal(number)

if number < 1:
    print("Неверный ввод")
else:
    print(binary, octan, hexa, sep=", ")
