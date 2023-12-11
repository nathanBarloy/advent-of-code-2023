
height = 0
width = 0
galaxies = []
used_lines = set()
used_columns = set()
with open("input.txt") as f:
    for i, line in enumerate(f):
        line = line.strip()
        height = i
        width = len(line)
        for j, x in enumerate(line):
            if x == "#":
                galaxies.append([i, j])
                used_columns.add(j)
                used_lines.add(i)
height += 1

empty_lines = sorted(list(set(range(height)).difference(used_lines)))
empty_columns= sorted(list(set(range(width)).difference(used_columns)))

def find_index(elem, list_, start=-1, end=-1):
    if end == -1:
        end = len(list_)
    if end-start == 1:
        return end
    middle = (start + end) // 2
    if elem < list_[middle]:
        return find_index(elem, list_, start, middle)
    else:
        return find_index(elem, list_, middle, end)

#print(galaxies)
factor = 1_000_000 - 1
for galaxy in galaxies:
    galaxy[0] += factor * find_index(galaxy[0], empty_lines)
    galaxy[1] += factor * find_index(galaxy[1], empty_columns)

#print(galaxies)

tot = 0
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        tot += abs(x1-x2) + abs(y1-y2)

print(tot)