
def extrapolate(sequence):
    for x in sequence:
        if x != 0:
            break
    else:
        return 0
    
    return sequence[-1] + extrapolate([sequence[i+1] - sequence[i] for i in range(len(sequence)-1)])

tot = 0
with open("input.txt") as f:
    for line in f:
        tot += extrapolate(list(map(int, line.split())))

print(tot)