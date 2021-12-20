def sudoku2(grid):
    # Check columns for duplicate
    for row in range(9):
        dup = set()
        for col in range(9):
            if grid[col][row] == ".":
                continue
            elif grid[col][row] in dup:
                return False
            else:
                dup.add(grid[col][row])
    # Check rows for duplicate
    for row in range(9):
        dup = set()
        for col in range(9):
            if grid[row][col] == ".":
                continue
            elif grid[row][col] in dup:
                return False
            else:
                dup.add(grid[row][col])
    # Check 3 x 3 sub grids for duplicate
    rowcount=0
    colcount=0
    for i in range(9):
        dup = set()        
        for row in range(rowcount, rowcount+3):
            for col in range(colcount, colcount+3):
                if grid[row][col] == ".":
                    continue
                elif grid[row][col] in dup:
                    return False
                else:
                    dup.add(grid[row][col])
        colcount+=3
        if colcount > 8:
            rowcount = rowcount + 3
            colcount = 0
                
    return True
