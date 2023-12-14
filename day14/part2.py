

class Plateform:

    def __init__(self, string):
        lines = string.split()
        self.height = len(lines)
        self.width = len(lines[0])
        self.plat = list(map(list, lines))
    
    def tilt_north(self):
        for j in range(self.width):
            block = 0
            for i in range(self.height):
                obj = self.plat[i][j]
                if obj == '.':
                    continue
                elif obj == '#':
                    block = i + 1
                elif obj == 'O':
                    if block != i:
                        self.plat[block][j] = 'O'
                        self.plat[i][j] = '.'
                    block += 1
    
    def tilt_south(self):
        for j in range(self.width):
            block = self.height - 1
            for i in range(self.height - 1, -1, -1):
                obj = self.plat[i][j]
                if obj == '.':
                    continue
                elif obj == '#':
                    block = i - 1
                elif obj == 'O':
                    if block != i:
                        self.plat[block][j] = 'O'
                        self.plat[i][j] = '.'
                    block -= 1
    
    def tilt_west(self):
        for i in range(self.height):
            block = 0
            for j in range(self.width):
                obj = self.plat[i][j]
                if obj == '.':
                    continue
                elif obj == '#':
                    block = j + 1
                elif obj == 'O':
                    if block != j:
                        self.plat[i][block] = 'O'
                        self.plat[i][j] = '.'
                    block += 1
    
    def tilt_east(self):
        for i in range(self.height):
            block = self.width - 1
            for j in range(self.width-1, -1, -1):
                obj = self.plat[i][j]
                if obj == '.':
                    continue
                elif obj == '#':
                    block = j - 1
                elif obj == 'O':
                    if block != j:
                        self.plat[i][block] = 'O'
                        self.plat[i][j] = '.'
                    block -= 1
    
    def cycle(self, nb_iter=1):
        seen = {str(self): 0}
        start = None
        cycle = None
        for i in range(1, nb_iter+1):
            self.tilt_north()
            self.tilt_west()
            self.tilt_south()
            self.tilt_east()

            string = str(self)
            if string in seen:
                start = seen[string]
                cycle = i - start
                print(f"break at {i}, start {start}")
                break
            else:
                seen[string] = i
        reste = (nb_iter - start) % cycle
        print(f"{reste} more")
        for _ in range(reste):
            self.tilt_north()
            self.tilt_west()
            self.tilt_south()
            self.tilt_east()


    
    def load(self):
        tot = 0
        for i in range(self.height):
            tot += self.plat[i].count('O') * (self.height - i)
        return tot
    
    def __str__(self):
        return '\n'.join([''.join(line) for line in self.plat])


with open("input.txt") as f:
    plateform = Plateform(f.read())


plateform.cycle(1_000_000_000)
print(plateform.load())