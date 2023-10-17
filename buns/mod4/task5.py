def count_letters(filename):
    letter_count = {}

    with open(filename, 'r') as file:
        for line in file:
            for letter in line:
                if letter.isalpha():
                    letter = letter.lower()
                    if letter in letter_count:
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1

    return letter_count


def write_statistics(filename, statistics):
    with open(filename, 'w') as file:
        for letter, count in statistics.items():
            file.write(f"{letter}: {count}\n")


input_filename = input("Введите имя файла: ")
output_filename = input("Введите имя файла для вывода статистики: ")

statistics = count_letters(input_filename)
sorted_statistics = dict(sorted(statistics.items(), key=lambda item: item[1]))

write_statistics(output_filename, sorted_statistics)

print("Статистика по буквам сохранена в файле.")