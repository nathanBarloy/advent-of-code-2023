
def combinaisons(springs, nums, pos=0):
    if len(nums) == 0:
        for i in range(pos, len(springs)):
            if springs[i] == '#':
                return 0
        return 1
    if pos == len(springs):
        return 0
    if sum(nums) + len(nums) - 1 > len(springs) - pos:
        return 0

    total = 0
    if springs[pos] != '#':
        total = combinaisons(springs, nums, pos+1)

    if springs[pos] != '.':
        if len(springs) < pos+nums[0]:
            return total
        for i in range(pos, pos+nums[0]):
            if springs[i] == '.':
                return total
        if len(springs) == pos+nums[0]:
            return total + 1
        if springs[pos+nums[0]] == '#':
            return total
        total += combinaisons(springs, nums[1:], pos+nums[0]+1)

    return total





tot = 0
with open("input.txt") as f:
    for line in f:
        springs, nums = line.strip().split()
        nums = list(map(int, nums.split(',')))
        res = combinaisons(springs, nums)
        #print(res)
        tot += res

print(tot)