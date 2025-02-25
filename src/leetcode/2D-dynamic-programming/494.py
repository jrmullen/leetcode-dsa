class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 2-D DP
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # Base case: there is 1 way to sum 0
        dp[0][0] = 1
  
        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count # + case
                dp[i + 1][total - nums[i]] += count # - case
        
        return dp[len(nums)][target]
