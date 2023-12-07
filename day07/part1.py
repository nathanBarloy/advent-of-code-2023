from collections import Counter

values = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8,
          'J':9, 'Q':10, 'K':11, 'A':12}


hands = []
with open("input.txt") as f:
    for line in f:
        hand, bid = line.split()
        bid = int(bid)
        hands.append([hand, bid])


def hand_val(hand):
    val = 0
    for x in hand:
        val *= 13
        val += values[x]
    
    aux = 13 ** 5
    hand_set = Counter(hand)
    hand_values = list(hand_set.values())
    if 5 in hand_values:
        val += aux * 6
    elif 4 in hand_values:
        val += aux * 5
    elif 3 in hand_values:
        if 2 in hand_values:
            val += aux * 4
        else:
            val += aux * 3
    elif 2 in hand_values:
        if hand_values.count(2) == 2:
            val += aux * 2
        else:
            val += aux

    return val

hands.sort(key=lambda x: hand_val(x[0]))

fact = 0
tot = 0
for hand in hands:
    #print(hand)
    fact += 1
    tot += fact * hand[1]

print(tot)
