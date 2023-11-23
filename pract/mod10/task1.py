import re


def check_password(password):
    """
    Функция проверяет корректность пароля.

    >>> check_password("rtG3FG!Tr^e")
    True
    >>> check_password("aA1!*!1Aa")
    True
    >>> check_password("oF^a1D@y5e6")
    True
    >>> check_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$$W0Rd")
    False
    """

    if re.search(r'[^a-zA-Z0-9^$%@#&*!?]', password):
        return False

    if len(re.findall(r'[A-Z]', password)) < 2:
        return False

    if re.search(r'\d', password) is None:
        return False

    if len(set(re.findall(r'[^a-zA-Z0-9]', password))) < 2:
        return False

    if re.search(r'(.)\1\1', password):
        return False

    if not (re.fullmatch(r'^.{6,}$', password)):
        return False

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
password = "aA1!*!1Aa"
result = check_password(password)
print(result)