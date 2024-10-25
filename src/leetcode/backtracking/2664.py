class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        board = [[-1 for _ in range(n)] for _ in range(m)] # Create an `n` x `m` board pre-populated with `-1`
        board[r][c] = 0 # Set the starting point
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)] # All possible knight moves

        def backtrack(row, col, board, count):
            # Base case: The board has been filled
            if count == m * n:
                return True

            # Check every possible move from the current position
            for x, y in moves:
                x += row
                y += col

                # If the new position (x, y) is within the bounds of the board and has the default value of -1
                if  0 <= x < m and 0 <= y < n and board[x][y] == -1:
                    # Update the board
                    board[x][y] = count

                    # Recurse from the new position
                    if backtrack(x, y, board, count + 1):
                        return True
                    
                    # Undo the above decision
                    board[x][y] = -1
            
            # If no successful moves were found, return
            return False
        
        backtrack(r, c, board, 1)
        return board
