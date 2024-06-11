class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = [] # modified subset that will be actively changing
        def backtrack(i):
            # Base case
            if(i >= len(nums)):
                # Append a copy of the `subset` array since is is being actively manipulated
                res.append(subset.copy())
                print(f'Appending {subset} to the result array')
                return

            # Actions:
            # 2 desicions - either add nums[i] to the subset, or do not

            # Action #1 - include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Action #2 - do NOT include nums[i]
            subset.pop() # nums[i] was previously appended to `subset`, so pop it off
            backtrack(i + 1)

        # Start at `nums[0]`
        backtrack(0)
        return res
