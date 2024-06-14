class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        def backtrack():
            # Base case - if `permutation` is the same length as `nums` all possible values have been used
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            # Actions - use every value in `nums` that has not yet been used
            for n in nums:
                if n not in permutation:
                    permutation.append(n)
                    backtrack()
                    # Undo the above decision
                    permutation.pop()

        backtrack()
        return res
