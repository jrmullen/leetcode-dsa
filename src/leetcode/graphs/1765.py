class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS = len(isWater)
        COLS = len(isWater[0])

        # Generate the `result` matrix
        result = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
        q = deque() # Contains tuples (row, col, height)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Iterate over the entire matrix and add all water tiles to the queue `q`
        for row in range(ROWS):
            for col in range(COLS):
                if isWater[row][col] == 1:
                    q.appendleft((row, col)) # The height of of land tiles adjacent to water will be 1
                    result[row][col] = 0

        # Multi-source BFS from all water tiles
        while q:
            row, col = q.pop()
            height = result[row][col]

            # Add neighboring tiles to the queue
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                
                # Stay within the bounds of the matrix and don't visit tiles that already have been assigned a value
                if newRow < 0 or newCol < 0 or newRow == ROWS or newCol == COLS or result[newRow][newCol] != -1:
                    continue

                # Set the neighbor's value in the `result` to 1 higher than the current height
                result[newRow][newCol] = height + 1

                # Add the neighbor tile to the queue
                q.appendleft((newRow, newCol))

        return result
