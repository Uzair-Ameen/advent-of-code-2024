
def get_count_map(number_list: list[int]) -> dict[int, int]:
    count_map = {}

    for x in number_list:
        count_map[x] = count_map.get(x, 0) + 1

    return count_map


def main():
    with open("advent_of_code_input.txt") as file_in:
        first_column = []
        second_column = []

        for line in file_in:
            [x, y] = line.split()
            first_column.append(int(x))
            second_column.append(int(y))

        total = 0

        count_map = get_count_map(second_column)

        for x in first_column:
            total += x * count_map.get(x, 0)

        print(total)

main()

