

next_turn_map = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

path_map = {
    '^': '|',
    '>': '-',
    'v': '|',
    '<': '-'

}

def get_next_point(current, x, y) -> tuple[int, int]:
    match current:
        case '^':
            return x - 1, y
        case '>':
            return x, y + 1
        case 'v':
            return x + 1, y
        case '<':
            return x, y - 1

def is_in_loop(current_dir, x, y, obstacles) -> bool:

    match current_dir:
        case '^':
            col_pos = next((z for z in obstacles if z[0] == x and z[1] > y), (-1, -1))
            row_pos = next((z for z in obstacles if z[0] > x and z[1] == y - 1), (-1, -1))

            if col_pos == (-1, -1) and row_pos == (-1, -1):
                return False

            dia_pos = row_pos[0] + 1, col_pos[1] - 1
            return dia_pos in obstacles
        case '>':
            col_pos = next((z for z in obstacles if z[0] == x - 1 and z[1] < y), (-1, -1))
            row_pos = next((z for z in obstacles if z[0] > x and z[1] == y), (-1, -1))

            if col_pos == (-1, -1) and row_pos == (-1, -1):
                return False

            dia_pos = row_pos[0] - 1, col_pos[1] - 1
            return dia_pos in obstacles
        case 'v':
            col_pos = next((z for z in obstacles if z[0] == x and z[1] < y), (-1, -1))
            row_pos = next((z for z in obstacles if z[0] < x and z[1] == y + 1), (-1, -1))

            if col_pos == (-1, -1) and row_pos == (-1, -1):
                return False

            dia_pos = row_pos[0] - 1, col_pos[1] + 1
            return dia_pos in obstacles
        case '<':
            col_pos = next((z for z in obstacles if z[0] < x and z[1] == y), (-1, -1))
            row_pos = next((z for z in obstacles if z[0] == x + 1 and z[1] > y), (-1, -1))

            if col_pos == (-1, -1) and row_pos == (-1, -1):
                return False

            dia_pos = col_pos[0] + 1, row_pos[1] + 1
            return dia_pos in obstacles


def get_visited_count(matrix: list[list[str]], starting_position: tuple[int, int], obstacles: list[tuple[int, int]]) -> tuple[int, int]:

    visited_count = 1

    placed_obstacles = set()

    current_position = starting_position

    i = current_position[0]
    j = current_position[1]

    def get_next_turn_and_point(x: int, y: int) -> tuple[str, tuple[int, int]]:
        nt = next_turn_map[matrix[x][y]]
        return nt, get_next_point(nt, x, y)

    while len(matrix) - 1 > i > 0 and len(matrix[0]) - 1 > j > 0:

        next_point = get_next_point(matrix[i][j], i, j)

        next_turn = matrix[i][j]

        if matrix[next_point[0]][next_point[1]] == '#':
            next_turn, next_point = get_next_turn_and_point(i, j)

        if matrix[next_point[0]][next_point[1]] == '.':

            is_part_of_a_loop =

            visited_count += 1

        matrix[next_point[0]][next_point[1]] = next_turn

        matrix[i][j] = '+' if next_turn != matrix[i][j] else path_map[matrix[i][j]]

        i = next_point[0]
        j = next_point[1]

    for point in placed_obstacles:
        matrix[point[0]][point[1]] = 'O'
    for row in matrix:
        print(''.join(row))

    return visited_count, len(placed_obstacles)



def main():
    with open("test.txt", "r") as f:
        matrix = []

        guard_starting_position = (0, 0)
        obstacle_positions: list[tuple[int, int]] = []

        lines = f.readlines()

        for i in range(len(lines)):
            trimmed_line = lines[i].strip()

            row = list(trimmed_line)

            matrix.append(row)

            obstacles = [i for i, itr in enumerate(trimmed_line) if itr == '#']

            for obstacle in obstacles:
                obstacle_positions.append((i, obstacle))

            if guard_starting_position == (0, 0):
                guard_position = trimmed_line.find('^')

                if guard_position != -1:
                    guard_starting_position = (i, guard_position)

        print(get_visited_count(matrix, guard_starting_position, obstacles)[1])


main()