
def get_visited_count(matrix: list[list[str]], starting_position: tuple[int, int]) -> int:
    visited_count = 1

    current_position = starting_position

    i = current_position[0]
    j = current_position[1]

    next_turn_map = {
        '^': '>',
        '>': 'v',
        'v': '<',
        '<': '^'
    }

    while len(matrix) - 1 > i > 0 and len(matrix[0]) - 1 > j > 0:

        next_point_map = {
            '^': (i - 1, j),
            '>': (i, j + 1),
            'v': (i + 1, j),
            '<': (i, j - 1)
        }

        next_point = next_point_map[matrix[i][j]]

        next_turn = matrix[i][j]

        if matrix[next_point[0]][next_point[1]] == '#':
            next_turn = next_turn_map[matrix[i][j]]
            next_point = next_point_map[next_turn]

        visited_count += 1 if matrix[next_point[0]][next_point[1]] == '.' else 0
        matrix[next_point[0]][next_point[1]] = next_turn

        matrix[i][j] = 'X'

        i = next_point[0]
        j = next_point[1]

    return visited_count



def main():
    with open("day6.txt", "r") as f:
        matrix = []

        guard_starting_position = (0, 0)

        lines = f.readlines()

        for i in range(len(lines)):
            trimmed_line = lines[i].strip()

            row = list(trimmed_line)

            matrix.append(row)

            if guard_starting_position == (0, 0):
                guard_position = trimmed_line.find('^')

                if guard_position != -1:
                    guard_starting_position = (i, guard_position)

        print(get_visited_count(matrix, guard_starting_position))


main()