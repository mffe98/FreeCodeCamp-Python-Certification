def dfs_n_queens(n: int) -> list:
    if n < 1:
        return []
    
    def is_valid(queen_col_positions, row, col):
        # Checking each row
        for y in range(row):
            # Get current value from solution list
            x = queen_col_positions[y]

            # Check: If Column already has a Queen [x == col] OR 
            # If Relative Diagonal Positions has any Queen [abs(x - col) == abs(y - row)]
            if x == col or abs(x - col) == abs(y - row):
                return False
        return True

    def dfs(n, queen_col_positions=[], row=0, solutions=[]):
        if row == n:
            solutions.append(queen_col_positions[:])
            return
        
        for col in range(n):
            if is_valid(queen_col_positions, row, col):
                queen_col_positions.append(col)
                dfs(n, queen_col_positions, row + 1, solutions)
                queen_col_positions.pop()
        return solutions

    return dfs(n)