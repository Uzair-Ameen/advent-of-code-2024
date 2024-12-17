
with open("advent_of_code_input.txt") as file_in:
    first_column = []
    second_column = []

    for line in file_in:
        [x, y] = line.split()
        first_column.append(int(x))
        second_column.append(int(y))

    sorted_first_column = sorted(first_column)
    sorted_second_column = sorted(second_column)

    total = 0

    for index in range(0, len(sorted_first_column)):
        total += abs(sorted_first_column[index] - sorted_second_column[index])
    print(total)
