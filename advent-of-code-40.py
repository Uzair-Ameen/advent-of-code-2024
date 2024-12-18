

def is_update_valid(update, order_map):
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if order_map.get(update[i]) is not None and update[j] in order_map.get(update[i]):
                return False
    return True


def main():
    with open("day5.txt", 'r') as f:
        order_map = {}

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

            if is_update_valid(pages, order_map):
                valid_updates.append(pages)

        count = 0

        for update in valid_updates:
            middle = int(update[int(len(update) / 2)])
            count += middle
        print(count)
main()