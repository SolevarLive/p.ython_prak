values = input("введите значения: ")
res = 0
for i in values:
    if i != ',':
        res += 1
    else:
        break
strin = values[0:res:]
nam = values[res + 1:]

c=0
for char in strin:
    if char == nam:
        c +=1
    else:
        break
print(c)