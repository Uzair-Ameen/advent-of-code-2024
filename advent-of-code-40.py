from functools import cmp_to_key

def main():
    order_map = {}

    def get_first(num1: str, num2: str) -> int:
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
            [x, y] = rule.split('|')
            if y in order_map:
                order_map[y].append(x)
            else:
                order_map[y] = [x]

        valid_updates = []

        for update in updates:
            pages = update.split(',')

            sorted_pages = sorted(pages, key=cmp_to_key(get_first))

            if sorted_pages == pages:
                valid_updates.append(pages)

        count = 0

        for update in valid_updates:
            middle = int(update[int(len(update) / 2)])
            count += middle
        print(count)
main()