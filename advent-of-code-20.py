import re

with open("day3.txt") as f:
    pattern = r'mul\([0-9]+,[0-9]+\)'

    text = f.read()
    matches = re.findall(pattern, text)

    total = 0

    for match in matches:
        numbers = re.findall(r'[0-9]+', match)

        [x, y] = numbers

        total += int(x) * int(y)

    print(total)