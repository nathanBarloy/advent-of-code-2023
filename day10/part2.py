
graph = []
current_position = None
start_position = None
with open("input.txt") as f:
    i = 0
    for line in f:
        line = line.strip()
        ind = line.find('S')
        if ind >= 0:
            start_position = (i, ind)
        graph.append(line)
        i += 1
height = len(graph)
width = len(graph[0])

# initialiser la loop
i, j = start_position
if 0<= (i-1) < height:
    if graph[i-1][j] in ['|', '7', 'F']:
        current_position = (i-1, j)
if current_position is None and 0<= (i+1) < height:
    if graph[i+1][j] in ['|', 'J', 'L']:
        current_position = (i+1, j)
if current_position is None and 0<= (j-1) < width:
    if graph[i][j-1] in ['-', 'L', 'F']:
        current_position = (i, j-1)
if current_position is None and 0<= (j-1) < width:
    if graph[i][j-1] in ['-', '7', 'J']:
        current_position = (i, j+1)

prev_i, prev_j = i, j
i, j = current_position

path = [start_position]
exits = {'|': [(-1, 0), (1, 0)],
         '-': [(0, -1), (0, 1)],
         'L': [(-1, 0), (0, 1)],
         'F': [(1, 0), (0, 1)],
         'J': [(-1, 0), (0, -1)],
         '7': [(1, 0), (0, -1)]}

while (i,j) != start_position:
    for dep_i, dep_j in exits[graph[i][j]]:
        next_i, next_j = i + dep_i, j + dep_j
        if (next_i, next_j) != (prev_i, prev_j):
            break
    path.append((i, j))
    prev_i, prev_j = i, j
    i, j = next_i, next_j

# Change start position
i, j = path[0]
next_i, next_j = path[1]
prev_i, prev_j = path[-1]
char = None
if next_i == i + 1:
    if prev_i == i - 1:
        char = '|'
    elif prev_j == j - 1:
        char = '7'
    elif prev_j == j + 1:
        char = 'F'
elif next_i == i - 1:
    if prev_i == i + 1:
        char = '|'
    elif prev_j == j - 1:
        char = 'J'
    elif prev_j == j + 1:
        char = 'L'
elif next_j == j + 1:
    if prev_j == j - 1:
        char = '-'
    elif prev_i == i - 1:
        char = 'L'
    elif prev_i == i + 1:
        char = 'F'
elif next_j == j - 1:
    if prev_j == j + 1:
        char = '-'
    elif prev_i == i - 1:
        char = 'J'
    elif prev_i == i + 1:
        char = '7'
    
assert(char is not None)
graph[i] = graph[i].replace('S', char)


path = set(path)
tot = 0
for i in range(height):
    inside = False
    entering_down = None
    for j in range(width):
        if (i, j) in path:
            if graph[i][j] == '|':
                inside = not inside
            elif graph[i][j] == 'L':
                entering_down = False
            elif graph[i][j] == 'F':
                entering_down = True
            elif graph[i][j] == '7' and not entering_down:
                inside = not inside
            elif graph[i][j] == 'J' and entering_down:
                inside = not inside
        else:
            if inside:
                tot += 1
print(tot)

