length = float(input("Введите длину: "))
perimeter = length * 4
area = length ** 2
diagonal = round((2 * length ** 2) ** 0.5, 2)

print('%.2f' % perimeter,'%.2f' % area, diagonal)