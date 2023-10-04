s = input("Введите предложение: ")
vowels = 0
consonant = 0

for char in s:
        if char in ("аеёиоуыэюя"):
            vowels += 1
        elif char in ("бвгджзйклмнпрстфхцчшщ"):
            consonant += 1

print(vowels, consonant)