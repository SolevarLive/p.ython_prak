line=input("Введите числа 0 и 1: ")
units=0
zeror=0
for l in line:
    if l == "1":
        units += 1
    if l == "0":
        zeror += 1
if units == zeror:
    print("yes")
else:
    print("no")




