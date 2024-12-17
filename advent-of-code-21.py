import re

with open("day3.txt") as f:
    pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"

    text = f.read()
    matches = re.findall(pattern, text)

    total = 0

    last_cond = "do()"

    for match in matches:

        if match == "do()" or match == "don't()":
            last_cond = match
            continue

        numbers = re.findall(r'[0-9]+', match)

        [x, y] = numbers

        total += (int(x) * int(y)) if last_cond == "do()" else 0

    print(total)