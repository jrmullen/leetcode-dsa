class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        result = float('inf')
        topSum = sum(grid[0]) # Postfix sum of all elements from the first row
        bottomSum = 0 # Prefix sum of all elements  from the second row

        # Iterate over each column of the `grid`
        for i in range(len(grid[0])):
            topSum -= grid[0][i] # Subtract the value of column `i` from the sum of the top row
            result = min(result, max(topSum, bottomSum)) # Update the `result`
            bottomSum += grid[1][i] # Add the value of column `i` to the sum of the bottom row
        
        return result
