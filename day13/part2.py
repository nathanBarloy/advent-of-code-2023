

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
        use_cheat = False
        while i >= 0 and  j < height:
            nb_diff = [lines[i][a]!=lines[j][a] for a in range(width)].count(True)
            if nb_diff > 0:
                if not use_cheat and nb_diff == 1:
                    use_cheat = True
                else:
                    found = False
                    break
            i -= 1
            j += 1
        if found and use_cheat:
            score = 100 * x
            break
    
    # look for vertical cut
    if score == 0:
        for x in range(1, width):
            i = x-1
            j = x
            found = True
            use_cheat = False
            while i >= 0 and  j < width:
                nb_diff = [lines[a][i]!=lines[a][j] for a in range(height)].count(True)
                if nb_diff > 0:
                    if not use_cheat and nb_diff == 1:
                        use_cheat = True
                    else:
                        found = False
                        break
                i -= 1
                j += 1
            if found and use_cheat:
                score = x
                break
    #print(score)
    tot += score

print(tot)
            
