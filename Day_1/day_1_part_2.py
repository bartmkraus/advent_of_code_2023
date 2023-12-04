result = 0
str_to_int = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}
file_path = "feed.txt"
with open(file_path) as t:
    content = t.read()
    for digit in str_to_int.keys():
        content = content.replace(digit, str(str_to_int[digit]))

for line in content.split():
    parts = []
    for char in line:
        if char.isdigit():
            parts.append(char)
    number = int(parts[0] + parts[-1])
    result += number
print(result)
