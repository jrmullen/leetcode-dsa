class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        q = deque([(0, 0, 0)]) # (row, col, cost) - start at 0, 0 with cost of 0
        minCosts = {} # Track the minimum cost encountered for each point in the `grid`
        
        while q:
            row, col, cost = q.popleft()

            # If the bottom right tile has been reached, return the `cost`
            if row == ROWS - 1 and col == COLS - 1:
                return cost
            
            # Visit each neighboring tile
            for direction in directions:
                dx, dy = directions[direction]
                newRow = row + dx
                newCol = col + dy

                # If the `direction` is NOT the same as the arrow in the `grid` tile the cost must increase by 1
                newCost = cost if direction == grid[row][col] else cost + 1

                # Do not leave the bounds of the `grid` or re-visit tiles with a larger cost
                if (newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS or newCost >= minCosts.get((newRow, newCol), float('inf'))):
                    continue

                # Update the `minCosts` for the current tile
                minCosts[(newRow, newCol)] = newCost

                # If the direction is the same as the tile's arrow, the move is free
                if grid[row][col] == direction:
                    q.appendleft((newRow, newCol, newCost)) # Cost 0 is pushed onto the left side of the queue
                else:
                    q.append((newRow, newCol, newCost))
