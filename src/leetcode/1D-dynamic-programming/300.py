class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top-down approach:
        # Track the longest increasing subsequence at each index of `nums`, working backwards.
        # If an element in `nums` is smaller than another value, add 1 to the previously tracked value

        # Default each count to 1 -- a single number is a subsequence of length 1
        dp = [1] * len(nums)
        
        # Start at the end of `nums` and work backwords
        for i in range(len(nums) - 1, -1, -1):
            # Compare each value `i` to the count tracked in `dp`
            for j in range(i + 1, len(nums)):
                # If `nums[i]` is smaller than `nums[j]`, increase the count of `dp[i]`.
                # Compare all possible values, keeping the largest count encountered
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
