def finalPositionOfSnake(self, n, commands):
    def createGrid(l):
        new = [i for i in range(l**2)]
        res = []
        for i in range(l):
            res.append(new[:l])
            new = new[l:]
        return res
        
    x, y = 0, 0
    for i in commands:
        if i.lower() == "right": x += 1
        elif i.lower() == "left": x -= 1
        elif i.lower() == "up": y -= 1
        else: y += 1
        
    return createGrid(n)[y][x]