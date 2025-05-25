def transpose(matrix):
    res = []
    for i in range(len(matrix[0])): 
        new_i = []
        for x in range(len(matrix)):  new_i.append(0)
        res.append(new_i)
        
    for i in range(len(matrix)):
        for x in range(len(matrix[0])):
            res[x][i] = matrix[i][x]
        
    return res