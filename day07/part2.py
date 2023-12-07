from collections import Counter

values = {'J':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9,
          'Q':10, 'K':11, 'A':12}


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
    nb_j = hand_set['J']
    hand_set['J'] = 0
    (best_card,_), = hand_set.most_common(1)
    hand_set[best_card] += nb_j
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
    else:
        print(hand_values)

    return val

hands.sort(key=lambda x: hand_val(x[0]))

fact = 0
tot = 0
for hand in hands:
    #print(hand)
    fact += 1
    tot += fact * hand[1]

print(tot)
