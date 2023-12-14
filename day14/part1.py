

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
    
    def load(self):
        tot = 0
        for i in range(self.height):
            tot += self.plat[i].count('O') * (self.height - i)
        return tot
    
    def __str__(self):
        return '\n'.join([''.join(line) for line in self.plat])


with open("input.txt") as f:
    plateform = Plateform(f.read())


plateform.tilt_north()
print(plateform)
print(plateform.load())