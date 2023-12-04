total_points = 0
file_path = "feed.txt"

def convert_to_lists(line):
    lists = line[8:].split("|")
    my_numbers = [int(i) for i in lists[0].split() if i.isdigit()]
    winning_numbers = [int(i) for i in lists[1].split() if i.isdigit()]
    return my_numbers, winning_numbers


def calculate_points(my_numbers, winning_numbers):
    seen_numbers = set()
    for num in my_numbers:
        if num in winning_numbers and num not in seen_numbers:
            seen_numbers.add(num)
    if len(seen_numbers) > 0:
        points = 2 ** (len(seen_numbers) - 1)
        return points
    return 0


file = open("feed.txt").readlines()

cards = [1 for card in file]

for index, line in enumerate(file):
    my_numbers, winning_numbers = convert_to_lists(line)
    n = len(set(my_numbers) & set(winning_numbers))
    points = calculate_points(my_numbers, winning_numbers)
    total_points += points
    for i in range(n):
        cards[index + i + 1] += cards[index]

print(total_points)
print(sum(cards))
