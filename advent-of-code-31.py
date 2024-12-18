
def validate_sub_matrix(matrix: list[list[str]], i: int, j: int) -> bool:
    str1 = matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2]
    str2 = matrix[i + 2][j] + matrix[i + 1][j + 1] + matrix[i][j + 2]

    return (str1 == 'MAS' or str1 == 'SAM') and (str2 == 'MAS' or str2 == 'SAM')

def get_x_mas_count(matrix: list[list[str]]) -> int:

    count = 0

    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            if matrix[i][j] == 'S' or matrix[i][j] == 'M':
                count += 1 if validate_sub_matrix(matrix, i, j) else 0

    return count

def main():
    with open("day4.txt") as f:
        matrix = []

        for line in f:
            matrix.append(list(line))
        count = get_x_mas_count(matrix)

        print(count)

main()