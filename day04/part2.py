with open("input.txt") as f:
    lines = list(f)

copies = [1] * len(lines)
for line in lines:
    card, line = line.split(':')

    _, card = card.split()
    card = int(card)-1

    winning, numbers = line.split('|')
    winning = set(map(int, winning.strip().split()))
    numbers = list(map(int, numbers.strip().split()))
    in_winning = list(filter(lambda x: x in winning, numbers))

    for i in range(card+1, card+1+len(in_winning)):
        copies[i] += copies[card]

print(sum(copies))