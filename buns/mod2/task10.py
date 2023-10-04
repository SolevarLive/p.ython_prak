string = input("Введите строку: ")
new_str = ""
_letter = ""
for i in range(len(string)):
    if string[i] == " ":
        new_str = new_str + _letter
        _letter = ""
    else:
        _letter = string[i]
new_str = new_str + _letter
print(new_str)