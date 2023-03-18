import sys
matrix = []
for _ in range(9):
    matrix.append(list(map(int, sys.stdin.readline().split())))
_max, x, y = 0, 0, 0
for i, j in enumerate(matrix):
    for k, l in enumerate(matrix):
       if _max <= matrix[i][k]:
            _max = matrix[i][k]
            x = i + 1
            y = k + 1
print(_max)
print(f"{x} {y}")