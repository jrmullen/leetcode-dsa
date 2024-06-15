class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort() # Sort the input so that duplicates can be skipped

        def backtrack(i):
            # Base case
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Actions - 2 actions, either add the next number, or do not add a number

            # Action 1 - Add the next number
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop() # Undo the above action

            # Action 2 - Do not add the next number
            # If a number is not being added, do not add any duplicates of that number either
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0) # Start at the beginning of `nums`
        return res
