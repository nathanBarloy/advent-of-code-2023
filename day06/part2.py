from math import sqrt, ceil, floor


with open("input.txt") as f:
    lines = f.readlines()

times, distances = list(map(lambda x: x.split()[1:], lines))


t = int(''.join(times))
d = int(''.join(distances))
sqrt_delta = sqrt(t*t - 4*d)
r1 = (t - sqrt_delta)/2
r2 = (t + sqrt_delta)/2

if r1.is_integer():
    r1 += 1
if r2.is_integer():
    r2 -= 1

res = (floor(r2) - ceil(r1) + 1)

print(res)