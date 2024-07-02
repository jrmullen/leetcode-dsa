class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current, total):
            # Base case
            if total == target:
                res.append(current.copy())

            if i >= len(candidates) or total >= target:
                return

            # Actions
            # 2 decisions - Use the current `candidate` again, or use the next available `candidate`

            # Action #1 - use the current candidate again
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])

            # Action #2 - use the next candidate
            current.pop()
            backtrack(i + 1, current, total)

        backtrack(0, [], 0)
        return res
