def is_valid_game(cubes):
    for i in range(0, len(cubes), 2):
        color, count = cubes[i], int(cubes[i + 1])
        if (
            (color == "red" and count > 12)
            or (color == "green" and count > 13)
            or (color == "blue" and count > 14)
        ):
            return False
    return True


games = []

with open("data_p1.txt") as file:
    for line in file:
        line = line.replace(":", "").replace(",", "").replace(";", "")
        line_parts = line.split()
        game_no = int(line_parts[1])
        cubes = line_parts[2:][::-1]
        if is_valid_game(cubes):
            games.append(int(game_no))

    print(sum(games))
