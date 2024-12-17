
def check_if_sorted(l: list[int]) -> bool:
    return all(3 >= l[i + 1] - l[i] > 0 for i in range(len(l) - 1)) or all(3 >= l[i] - l[i + 1] > 0 for i in range(len(l) - 1))

def check_if_really_sorted(l: list[int]) -> bool:
    safe = check_if_sorted(l)

    if safe:
        return True

    if not safe:
        for i in range(len(l)):
            if check_if_sorted(l[: i] + l[i + 1:]):
                return True
        return False

def main():
    stable_count = 0
    with open("day-2-input.txt") as file_in:
        for line in file_in:
            l = line.split()
            if check_if_really_sorted([int(i) for i in l]):
                print([int(i) for i in l])
                stable_count += 1
        print(stable_count)

main()