MAX_COLOR = {"red": 12,
             "green": 13,
             "blue": 14}


with open("input.txt") as f:
    tot = 0
    for line in f:
        go_next = False
        game, line = line.split(":")
        game_id = int(game[5:])
        grabs = line.split(";")
        for grab in grabs:
            cubes = grab.split(",")
            for cube in cubes:
                number, color = cube.strip().split()
                number = int(number)
                if number > MAX_COLOR[color]:
                    #print(f"erreur : game {game_id}, {number} {color}")
                    go_next = True
                    break
            if go_next:
                break
        if go_next:
            continue
        #print(game_id)
        tot += game_id

print(tot)