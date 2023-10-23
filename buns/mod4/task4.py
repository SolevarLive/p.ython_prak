def check_palindrome(word):

    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1


    odd_count = 0
    for count in letter_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return None


    palindrome = ''
    odd_letter = ''
    for letter, count in letter_count.items():
        if count % 2 != 0:
            odd_letter = letter
        palindrome += letter * (count // 2)

    return palindrome + odd_letter + palindrome[::-1]


word = input("Введите слово: ")
result = check_palindrome(word)
if result is None:
    print("Невозможно составить палиндром")
else:
    print("Палиндром:", result)
