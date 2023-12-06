with open("input.txt") as f:
    groups = f.read().split("\n\n")

seeds = list(map(int, groups[0].split(": ")[1].split()))
seeds = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]


def parse_group(group):
    res = group.split('\n')[1:]
    res = list(map(lambda x: list(map(int, x.split())), res))
    return res


def transform(seeds, ranges):
    res = []
    for start, end in seeds:
        for dest, source, length in ranges:
            delta = dest - source

            # Cas 1 : dedans et fin
            if source <= start  and end < source + length:
                res.append((delta + start, delta + end))
                break

            # Cas 2 : autour, sépare en 2
            if start < source and end >= source + length:
                res.append((dest, dest + length - 1))
                seeds.append((source + length, end))
                end = source - 1
                continue

            # Cas 3 : chevauche gauche
            if source <= end and end < source + length:
                res.append((dest, end + delta))
                end = source - 1
                continue

            # Cas 4 : chevauchement droite
            if source <= start and start < source + length:
                res.append((start + delta, dest + length - 1))
                start = source + length
                continue
        else:
            res.append((start, end))
    return res


for group in groups[1:]:
    #print(seeds)
    ranges = parse_group(group)
    seeds = transform(seeds, ranges)

print(min(seeds, key=lambda x: x[0]))