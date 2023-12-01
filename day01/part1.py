with open("input.txt") as f:
    tot = 0
    for line in f:
        first = None
        last = None
        for c in line:
            if c.isdigit() :
                if first is None:
                    first = c
                last = c
        tot += int(first + last)
    print(tot)