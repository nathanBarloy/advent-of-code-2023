
numbers = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]

with open("input.txt") as f:
    tot = 0
    for line in f:
        first = None
        first_pos = -1
        last = None
        last_pos = -1
        i = 0
        for c in line:
            if c.isdigit() :
                if first is None:
                    first_pos = i
                    last_pos = i
                    first = c
                last = c
                last_pos = i
            i += 1

        positions = [(line.find(x), line.rfind(x)) for x in numbers]
        if first is not None:
            first = int(first)
            last = int(last)
        else:
            i = 0
            while positions[i][0] == -1:
                i += 1
            first = i
            last = i
            first_pos = positions[i][0]
            last_pos = positions[i][1]

        for i in range(10):
            (p1, p2) = positions[i]
            if p1 == -1:
                continue
            if p1 < first_pos:
                first_pos = p1
                first = i
            if p2 > last_pos:
                last_pos = p2
                last = i

        tot += 10*first + last
    print(tot)