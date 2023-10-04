def shift_alphabet(strin, nam):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if strin not in alphabet:
        print("Неверный ввод")

    index = alphabet.index(strin)
    shifted_index = (index + nam) % len(alphabet)
    shifted_character = alphabet[shifted_index]

    return shifted_character


def main():
    input_str = input("Введите символ и число: ")
    res = 0

    for i in input_str:
        if i != ',':
            res += 1
        else:
            break
    strin = input_str[0:res:]
    nam = int(input_str[res+1:])


    shifted_character = shift_alphabet(strin, nam)

    print("Символ после смещения:", shifted_character)

main()