with open("input.txt") as f:
    tot = 0
    for line in f:
        _, line = line.split(':')
        winning, numbers = line.split('|')
        winning = set(map(int, winning.strip().split()))
        numbers = list(map(int, numbers.strip().split()))
        in_winning = list(filter(lambda x: x in winning, numbers))

        if len(in_winning) > 0:
            tot += (1 << (len(in_winning)-1))
    print(tot)