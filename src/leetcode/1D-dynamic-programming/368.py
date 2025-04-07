class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)

        # Sort the input list in ascending order to simplify finding pairs
        nums.sort()

        # Each element of `dp` will contain the longest subset starting with `nums[i]`
        dp = [[num] for num in nums] # Each number will be divisible by itself, so default each subset to contain the starting number

        result = dp[-1] # Track the largest subset
        
        # Work backwords starting at the end oof the list
        for i in range(N - 1, -1, -1):
            # `j` is always larger than `i` since the list of `nums` has been sorted
            for j in range(i + 1, N):
                # If j is divisible by i
                if nums[j] % nums[i] == 0:
                    combined = [nums[i]] + dp[j] # Combine j's subset into i
                    # If the new `combined` subset is larger than i's current subset, overwrite it
                    if len(combined) > len(dp[i]):
                        dp[i] = combined

            # Update the `result` with the largest subset encountered
            if len(dp[i]) > len(result):
                result = dp[i]
        
        return result
