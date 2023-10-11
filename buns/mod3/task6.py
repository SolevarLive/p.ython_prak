words = input("Введите слова ").split()
output = ''.join(word[-1] for word in words)
print(output)