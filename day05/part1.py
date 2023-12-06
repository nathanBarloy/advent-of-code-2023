with open("input.txt") as f:
    groups = f.read().split("\n\n")

seeds = list(map(int, groups[0].split(": ")[1].split()))

def parse_group(group):
    res = group.split('\n')[1:]
    res = list(map(lambda x: list(map(int, x.split())), res))
    return res


def transform(seeds, ranges):
    res = []
    for seed in seeds:
        for dest, source, length in ranges:
            if source <= seed < source + length:
                res.append(dest + seed - source)
                break
        else:
            res.append(seed)
    return res


for group in groups:
    #print(seeds)
    ranges = parse_group(group)
    seeds = transform(seeds, ranges)

print(min(seeds))