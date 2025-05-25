def numRookCaptures(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R': rook_i, rook_j = i, j

    count = 0
    # Up
    for x in range(rook_i - 1, -1, -1):
        if board[x][rook_j] == 'B': break
        if board[x][rook_j] == 'p':
            count += 1
            break
    # Down
    for x in range(rook_i + 1, 8):
        if board[x][rook_j] == 'B': break
        if board[x][rook_j] == 'p':
            count += 1
            break
    # Left
    for y in range(rook_j - 1, -1, -1):
        if board[rook_i][y] == 'B': break
        if board[rook_i][y] == 'p':
            count += 1
            break
    # Right
    for y in range(rook_j + 1, 8):
        if board[rook_i][y] == 'B': break
        if board[rook_i][y] == 'p':
            count += 1
            break

    return count