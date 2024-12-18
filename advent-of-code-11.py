def check_if_sorted(l: list[int], sign: int) -> bool:

    is_stable = True

    i = 0
    skipped = False

    while i < len(l) - 1 and is_stable:
        diff = l[i + 1] - l[i] if sign > 0 else l[i] - l[i + 1]

        if diff > 3 or diff < 1:
            if skipped:
                is_stable = False
            else:
                diff = l[i + 1] - l[i - 1] if sign > 0 else l[i - 1] - l[i + 1]
                if i > 0:
                    print(l[i + 1], l[i - 1], diff, i)
                if i > 0 and 3 >= diff > 0:
                    skipped = True
                else:
                    if i + 1 == len(l) - 1:
                        is_stable = not skipped
                    else:
                        diff = l[i + 2] - l[i] if sign > 0 else l[i] - l[i + 2]
                        if 3 >= diff > 0:
                            skipped = True
                            i += 1
                        else:
                            if i == 0:
                                skipped = True
                            else:
                                is_stable = False

        i += 1

    return is_stable

def main():
    stable_count = 0
    with open("test.txt") as file_in:
        for line in file_in:
            split_l = line.split()
            l = [int(i) for i in split_l]
            valid = check_if_sorted(l, 1) or check_if_sorted(l, -1)
            if valid:
                print(l)
                stable_count += 1
        print(stable_count)

main()
