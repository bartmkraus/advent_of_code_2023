from functools import reduce


time = 48876981
distance = 255128811171623
times = [48, 87, 69, 81]
bests = [255, 1288, 1117, 1623]


def ways_to_win(race_time, record):
    return sum((race_time - i) * i > record for i in range(1, race_time + 1))


results = [ways_to_win(t, best) for t, best in zip(times, bests)]


def multiply(rs):
    return reduce(lambda x, y: x * y, rs)


print("Results:", results)
print("Result Product:", multiply(results))
print("Result part 2:", ways_to_win(time, distance))
