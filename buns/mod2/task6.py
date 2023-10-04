domain = input("Введите имя сайта: ")
_domain = ""
_char = ""
_position = len(domain) - 1

while _position >= 0:
    char = domain[_position]
    if char == ".":
        if _char != ".":
            print(_domain[::-1])
            _domain = ""
    else:
        _domain =_domain + char
    _char = char
    _position = _position - 1

print(_domain[::-1])