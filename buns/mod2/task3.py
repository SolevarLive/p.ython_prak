numbers = input("Введите числа: ")
_index_1 = None
_index_2 = None
for i in range(len(numbers)):
    if numbers[i] == " ":
        if _index_1 is None:
            _index_1 = i
        else:
            _index_2 = i
            break
a = int(numbers[:_index_1])
b = int(numbers[_index_1+1:_index_2])
c = int(numbers[_index_2+1:])
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(b)