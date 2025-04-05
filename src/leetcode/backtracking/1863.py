class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, total):
            # Base case: all numbers have been considered
            if i == len(nums):
                return total
            
            # 2 options: either use the current number, or don't
            # Case #1: use the number, so add it's XOR value to the `total`
            # Case #2: do not use the number, so pass on the current `total`
            # Return the new `total` -- the sum of the two subtrees
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)
        
        # DFS to find the total XOR value of all subsets starting at the first index of the list of `nums`
        return dfs(0, 0)
