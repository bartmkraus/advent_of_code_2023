def read_lines_from_file(file_path):
    with open(file_path) as file:
        return [line.rstrip() for line in file.readlines()]


def process_data(lines):
    m, n = len(lines), len(lines[0])
    counts = [[0] * n for _ in range(m)]
    prods = [[1] * n for _ in range(m)]
    total_sum = 0

    for i in range(m):
        j = 0
        while j < n:
            ctr = 1
            while j < n - 1 and lines[i][j].isdigit() == lines[i][j + 1].isdigit():
                ctr += 1
                j += 1
            if lines[i][j].isdigit():
                num = int(lines[i][j - ctr + 1: j + 1])
                valid = False
                for x in range(i - 1, i + 2):
                    for y in range(j - ctr, j + 2):
                        if 0 <= x < m and 0 <= y < n and lines[x][y] != "." and not lines[x][y].isdigit():
                            valid = True
                        if 0 <= x < m and 0 <= y < n and lines[x][y] == "*":
                            counts[x][y] += 1
                            prods[x][y] *= num
                            break
                if valid:
                    total_sum += num
            j += 1

    ratios_sum = 0

    for i in range(m):
        for j in range(n):
            if counts[i][j] == 2:
                ratios_sum += prods[i][j]

    return total_sum, ratios_sum


if __name__ == "__main__":
    file_path = "feed.txt"
    lines = read_lines_from_file(file_path)
    result_sum, result_ratios = process_data(lines)

    print("Total Sum:", result_sum)
    print("Sum of Ratios:", result_ratios)
