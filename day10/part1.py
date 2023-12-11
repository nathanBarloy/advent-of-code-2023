
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

print(len(path)//2)
