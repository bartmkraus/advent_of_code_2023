def clean_data(line):
    cleaned_line = line.replace(":", "").replace(",", "").replace(";", "")
    game = cleaned_line.split()[2:]
    return game[::-1]


def fewest_number_of_cubes_of_each_color(game):
    cube_counts = {"red": 0, "green": 0, "blue": 0}
    for color, count_str in zip(game[::2], game[1::2]):
        count = int(count_str)
        cube_counts[color] = max(cube_counts[color], count)

    return cube_counts


def the_power_of_a_set_of_cubes(cube_counts):
    return cube_counts["red"] * cube_counts["green"] * cube_counts["blue"]


result = 0
file_path = "feed.txt"

with open(file_path) as file:
    for line in file:
        game = clean_data(line)
        cube_counts = fewest_number_of_cubes_of_each_color(game)
        result += the_power_of_a_set_of_cubes(cube_counts)

print(result)
