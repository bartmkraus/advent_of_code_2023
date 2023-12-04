result = 0
file_path = "feed.txt"
with open(file_path) as t:
    for line in t:
        parts = []
        for char in line:
            if char.isdigit():
                parts.append(char)
        number = int(parts[0]+parts[-1])
        result += number
print(result)
