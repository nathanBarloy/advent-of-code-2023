from math import lcm


graph = {}
current = set()
with open("input.txt") as f:
    instr = f.readline().strip()
    f.readline()
    for line in f:
        graph[line[:3]] = (line[7:10], line[12:15])
        if line[2] == 'A':
            current.add(line[:3])

def all_end_Z(nodes):
    for node in nodes:
        if node[2] != 'Z':
            return False
    return True

step = 0
mod_step = 0
length = len(instr)
loops = []
for node in current:
    print(f"start from {node}:")
    step = 0
    mod_step = 0
    seen = {}
    z_seen = []
    while (node, mod_step) not in seen:
        seen[(node, mod_step)] = step
        if node[2] == 'Z':
            z_seen.append((node, step))
        node = graph[node][0 if instr[mod_step]=='L' else 1]
        step += 1
        mod_step += 1
        if mod_step == length:
            mod_step = 0
    loop_size = step - seen[(node, mod_step)]
    _, z_shift = z_seen[-1]
    print(f"Initial loop at {node} step {seen[(node, mod_step)]}.\nCurrently step {step}, {loop_size} after.\n{z_seen}")
    print(f"init shift: {seen[(node, mod_step)]}, loop size: {loop_size}, z shift after loop: {z_shift - seen[(node, mod_step)]}\n")
    print(f"x = {z_shift} mod {loop_size}\n")
    loops.append(loop_size)

print(lcm(*loops))
