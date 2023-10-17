def check_winner(board, k):
    lines = []

    # Гориз линии
    for row in board:
        for i in range(len(row) - k + 1):
            lines.append(row[i:i + k])

    # Верт линии
    for i in range(len(board[0])):
        for j in range(len(board) - k + 1):
            line = ''
            for l in range(k):
                line += board[j + l][i]
            lines.append(line)

    # Диаг линии (сл-нп)
    for i in range(len(board) - k + 1):
        for j in range(len(board[0]) - k + 1):
            line = ''
            for l in range(k):
                line += board[i + l][j + l]
            lines.append(line)

    # Диагональные линии (сп-нл)
    for i in range(len(board) - k + 1):
        for j in range(k - 1, len(board[0])):
            line = ''
            for l in range(k):
                line += board[i + l][j - l]
            lines.append(line)

    for line in lines:
        if line.count('X') == k:
            return 'X'
        elif line.count('O') == k:
            return 'O'

    return 'Ничья'


board = input("Введите игровое поле: ").split() #пример ввода: X_X O__ XO_ (все в одну строку
k = int(input("Введите количество символов в линии для победы: ")) #если смотрет ьв нашем случае то 3

winner = check_winner(board, k)
print("Победитель:", winner)
