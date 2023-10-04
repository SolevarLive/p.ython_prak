barcode = input("Введите штрих-код: ")
strange_sum = 0
even_sum = 0

for i in range(len(barcode)):
    digit = int(barcode[i])

    if i % 2 == 0:
        strange_sum += digit
    else:
        even_sum += digit

if ((strange_sum + (3 * even_sum)) % 10) == 0:
     print('yes')
else:
     print('no')