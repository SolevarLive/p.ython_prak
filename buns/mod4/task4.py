def palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return False

word = input("Введите слово: ")

if palindrome(word):
    print("Можно составить палиндром")
else:
    print("Нельзя составить палиндром")