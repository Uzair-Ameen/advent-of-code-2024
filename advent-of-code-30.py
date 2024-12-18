

def get_xmas_count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                if j + 3 < len(matrix[i]):
                    if matrix[i][j + 1] == 'M' and matrix[i][j + 2] == 'A' and matrix[i][j + 3] == 'S':
                        count += 1
                if i + 3 < len(matrix):
                    if matrix[i + 1][j] == 'M' and matrix[i + 2][j] == 'A' and matrix[i + 3][j] == 'S':
                        count += 1
                if j - 3 >= 0:
                    if matrix[i][j - 1] == 'M' and matrix[i][j - 2] == 'A' and matrix[i][j - 3] == 'S':
                        count += 1
                if i - 3 >= 0:
                    if matrix[i - 1][j] == 'M' and matrix[i - 2][j] == 'A' and matrix[i - 3][j] == 'S':
                        count += 1
                if i + 3 < len(matrix) and j + 3 < len(matrix[i]):
                    if matrix[i + 1][j + 1] == 'M' and matrix[i + 2][j + 2] == 'A' and matrix[i + 3][j + 3] == 'S':
                        count += 1
                if i - 3 >= 0 and j - 3 >= 0:
                    if matrix[i - 1][j - 1] == 'M' and matrix[i - 2][j - 2] == 'A' and matrix[i - 3][j - 3] == 'S':
                        count += 1
                if i - 3 >= 0 and j + 3 < len(matrix[i]):
                    if matrix[i - 1][j + 1] == 'M' and matrix[i - 2][j + 2] == 'A' and matrix[i - 3][j + 3] == 'S':
                        count += 1
                if i + 3 < len(matrix) and j - 3 >= 0:
                    if matrix[i + 1][j - 1] == 'M' and matrix[i + 2][j - 2] == 'A' and matrix[i + 3][j - 3] == 'S':
                        count += 1

    return count

def main():
    with open("day4.txt") as f:
        matrix = []

        for line in f:
            matrix.append(list(line))
        count = get_xmas_count(matrix)

        print(count)

main()