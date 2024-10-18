class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        largestOr = 0

        # OR all values in `nums` together to get the `largestOr` target value
        for num in nums:
            largestOr |= num

        def dfs(i, currentOr, largestOr):
            # Base case: the bottom of the decision tree has been reached.
            # If the total OR result `currentOr` is equal to the `largestOr` value, return 1
            # to increase the result count
            if i == len(nums):
                return 1 if currentOr == largestOr else 0

            # Backtrack, returning the sum of all subsets with a total OR value that is equal to `largestOr`
            return(
                dfs(i + 1, currentOr, largestOr) + # Don't include the current number
                dfs(i + 1, currentOr | nums[i], largestOr) # Include the current number
            )
        
        return dfs(0, 0, largestOr)
