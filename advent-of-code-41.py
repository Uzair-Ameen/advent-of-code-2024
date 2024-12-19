from functools import cmp_to_key

#There's literally nop need to convert the inputs to integers. I just did it because I wanted to

def main():
    order_map = {}

    def get_first(num1: int, num2: int) -> int:
        if order_map.get(num1) is not None and num2 in order_map.get(num1):
            return 1
        elif order_map.get(num2) is not None and num1 in order_map.get(num2):
            return -1
        return 0

    with open("day5.txt", 'r') as f:

        lines = f.read().splitlines()

        empty_string_index = lines.index("")

        page_ordering_rules = lines[:empty_string_index]
        updates = lines[empty_string_index + 1:]

        for rule in page_ordering_rules:
            [x, y] = [int(x) for x in rule.split('|')]
            if y in order_map:
                order_map[y].append(x)
            else:
                order_map[y] = [x]

        invalid_updates = []

        for update in updates:
            pages = [int(x) for x in update.split(',')]
            valid_update = sorted(pages, key=cmp_to_key(get_first))

            if valid_update != pages:
                invalid_updates.append(valid_update)

        count = 0

        for update in invalid_updates:
            middle = update[int(len(update) / 2)]
            count += middle
        print(count)
main()