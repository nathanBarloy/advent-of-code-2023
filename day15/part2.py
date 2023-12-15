
boxes = [[] for _ in range(256)]

def str_hash(string):
    res = 0
    for x in string:
        res += ord(x)
        res *= 17
        res %= 256
    return res

with open("input.txt") as f:
    init = f.read().strip().split(',')


for s in init:
    if s[-1] == '-':
        label = s[:-1]
        box_id = str_hash(label)
        for i, (lab, val) in enumerate(boxes[box_id]):
            if label == lab:
                boxes[box_id].pop(i)
                break
    
    else:
        label, value = s.split('=')
        value = int(value)
        box_id = str_hash(label)
        for i, (lab, val) in enumerate(boxes[box_id]):
            if label == lab:
                boxes[box_id][i][1] = value
                break
        else:
            boxes[box_id].append([label, value])

tot = 0
for i, box in enumerate(boxes):
    for j, (_, val) in enumerate(box):
        tot += (i+1) * (j+1) * val
print(tot)