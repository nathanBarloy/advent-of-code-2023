
with open("input.txt") as f:
    tot = 0
    for line in f:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        game, line = line.split(":")
        grabs = line.split(";")
        for grab in grabs:
            cubes = grab.split(",")
            for cube in cubes:
                number, color = cube.strip().split()
                number = int(number)
                min_cubes[color] = max(min_cubes[color], number)
                  
        tot += min_cubes["green"] * min_cubes["red"] * min_cubes["blue"]

print(tot)