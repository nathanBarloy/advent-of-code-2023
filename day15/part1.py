
def str_hash(string):
    res = 0
    for x in string:
        res += ord(x)
        res *= 17
        res %= 256
    return res

with open("input.txt") as f:
    init = f.read().strip().split(',')

tot = 0
for s in init:
    tot += str_hash(s)
print(tot)