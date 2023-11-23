import re


def is_valid_web_color(color):
    """
    Функция проверяет корректность переданного web цвета.

    Принимает строку, содержащую цвет в одном из трех web форматов: rgb, hex или hsl.
    Возвращает True, если переданный цвет является корректным, иначе - False.

    >>> is_valid_web_color('#21f48D')
    True
    >>> is_valid_web_color('#888')
    True
    >>> is_valid_web_color('rgb(255,255,255)')
    True
    >>> is_valid_web_color('rgb(10%,20%,0%)')
    True
    >>> is_valid_web_color('hsl(200,100%,50%)')
    True
    >>> is_valid_web_color('hsl(0, 0%, 0%)')
    True
    >>> is_valid_web_color('#2345')
    False
    >>> is_valid_web_color('ffffff')
    False
    >>> is_valid_web_color('rgb(257, 50, 10)')
    False
    >>> is_valid_web_color('hsl(20, 10, 0.5)')
    False
    >>> is_valid_web_color('hsl(34%, 20%, 50%)')
    False
    """

    hex_regex = r'^#([0-9a-fA-F]{3}){1,2}$'
    if re.match(hex_regex, color):
        return True

    rgb_regex = r'^rgb\((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%) ?, ?(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%) ?, ?(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5]|0%|100%)\)$'
    if re.match(rgb_regex, color):
        return True

    hsl_regex = r'^hsl\((\d{1,2}|[1-2]\d{2}|3[0-5]\d) ?, ?(100%|\d{1,2}%) ?, ?(100%|\d{1,2}%)\)$'
    if re.match(hsl_regex, color):
        return True

    #тут отдельная проверка на %
    rgb_regex = r"rgb\(\s*((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%\s*,\s*){2}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)%\s*\)"
    return bool(re.fullmatch(rgb_regex, color))

    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(is_valid_web_color('rgb(30%,20%,50%)'))
print(is_valid_web_color('hsl(30%, 20%, 50%)'))