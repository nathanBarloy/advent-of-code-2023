graph = {}
with open("input.txt") as f:
    instr = f.readline().strip()
    f.readline()
    for line in f:
        graph[line[:3]] = (line[7:10], line[12:15])

step = 0
length = len(instr)
current = "AAA"
while current != "ZZZ":
    if instr[step%length] == 'L':
        current = graph[current][0]
    else:
        current = graph[current][1]
    step += 1

print(step)