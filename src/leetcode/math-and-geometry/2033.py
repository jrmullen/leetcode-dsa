class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        result = 0
        nums = [] # The numbers from the `grid` in 1-D list form

        # Iterate over each `num` in the `grid`
        for row in range(ROWS):
            for col in range(COLS):
                num = grid[row][col]
                
                # If the remainders when divided by `x` are not the same for all elements, a uni-value grid is not possible
                if num % x != grid[0][0] % x:
                    return -1
                
                # Push the `num` into the list of `nums`
                nums.append(num)
        
        # Sort the list of `nums`
        nums.sort()

        # The `target` value will be the half-way point (median) of the `nums` array
        target = nums[len(nums) // 2]

        # Finally, iterate over the list of `nums` and calculate the number of operations needed to reach the `target`
        for num in nums:
            result += abs(target - num) // x

        return result
