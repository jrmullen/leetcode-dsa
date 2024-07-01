class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        candidates.sort() # Sort `candidates` so we can skip duplicate numbers

        def backtrack(i, target):
            # Base case - the target sum has been exceeded or all `candidates` have been used
            if target <= 0 or i >= len(candidates):
                if target == 0:
                    res.append(combination.copy())
                return

            previous = -99
            # Actions - use each value in `candidates`
            for j in range(i, len(candidates)):
                # Skip duplicates
                if candidates[j] == previous:
                    continue
                combination.append(candidates[j])
                # Backtrack using the next number & calculating the new target
                backtrack(j + 1, target - candidates[j])
                combination.pop()
                previous = candidates[j]

        backtrack(0, target)
        return res
