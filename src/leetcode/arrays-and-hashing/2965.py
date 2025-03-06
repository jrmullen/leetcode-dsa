class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result = [0, 0]
        n = len(grid)
        seen = set() # Track the numbers in the `grid`

        # Iterate over each cell in the `grid`
        for row in range(n):
            for col in range(n):
                num = grid[row][col]
                if num in seen:
                    result[0] = num # If the `num` has already been seen previously, it is the repeat number
                seen.add(num) # Add `num` to the `seen` set

        # Iterate over each number from 1 to n^2 until the number that is not in the `seen` set is found
        for i in range(1, (n * n) + 1):
            if i not in seen:
                # Set the value in the `result` array and return immediately
                result[1] = i
                return result
