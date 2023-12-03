numbers = []
symbols = set()

with open("day03/input.txt") as f:
    for (num_line, line) in enumerate(f):
        line = line.strip()
        current_number = ""
        current_size = 0
        start_num = -1
        for (num_char, c) in enumerate(line):
            if c.isdigit():
                if start_num < 0:
                    start_num = num_char
                current_number += c
                current_size += 1
            else:
                if current_size > 0:
                    numbers.append((int(current_number), current_size, (num_line, start_num)))
                current_number = ""
                current_size = 0
                start_num = -1
                if c != '.':
                    symbols.add((num_line, num_char))
        if current_size > 0:
            numbers.append((int(current_number), current_size, (num_line, start_num)))

tot = 0
for num, size, (line, start_pos) in numbers:
    found = False
    for i in range(start_pos-1, start_pos + size + 1):
        if (line-1, i) in symbols or (line+1, i) in symbols:
            tot += num
            found = True
            break
    if found:
        continue
    if (line, start_pos-1) in symbols or (line, start_pos+size) in symbols:
        tot += num
        continue

print(tot)