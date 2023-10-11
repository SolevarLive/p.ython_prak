size = int(input())
matrix = [[i for i in range(1, size+1)] for _ in range(size)]
transposed_matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]

for row in matrix:
    print(", ".join(map(str, row)))
print()

for row in transposed_matrix:
    print(", ".join(map(str, row)))