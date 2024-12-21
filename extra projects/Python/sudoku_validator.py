def validate_sudoku(board):
    # check row and numbers
    for row in board:
        if ([row.count(i) == 1 for i in row].count(True) != 9) or sum(row) != 45: return False

    # check columns
    for i in range(9):
        column = [board[x][i] for x in range(9)]
        if [column.count(i) == 1 for i in column].count(True) != 9: return False

    # check subgrid
    for grid_row in range(0, 9, 3):
        for grid_col in range(0, 9, 3):
            subgrid = [
                board[row][col]
                for row in range(grid_row, grid_row + 3)
                for col in range(grid_col, grid_col + 3)
            ]
            if [subgrid.count(i) == 1 for i in subgrid].count(True) != 9: return False

    return True