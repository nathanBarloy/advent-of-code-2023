

with open("input.txt") as f:
    cases = f.read().split('\n\n')

tot = 0
for pattern in cases:
    lines = pattern.split('\n')
    height = len(lines)
    width = len(lines[0])

    # look for horizontal cut
    score = 0
    for x in range(1, height):
        i = x-1
        j = x
        found = True
        while i >= 0 and  j < height:
            if lines[i] != lines[j]:
                found = False
                break
            i -= 1
            j += 1
        if found:
            score = 100 * x
            break
    
    # look for vertical cut
    if score == 0:
        for x in range(1, width):
            i = x-1
            j = x
            found = True
            while i >= 0 and  j < width:
                if any([lines[a][i]!=lines[a][j] for a in range(height)]):
                    found = False
                    break
                i -= 1
                j += 1
            if found:
                score = x
                break
    
    tot += score

print(tot)
            
