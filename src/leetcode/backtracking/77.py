class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []

        def backtrack(i):
            # If the combination contains `k` numbers append it to the `result` list
            if len(combination) == k:
                result.append(combination.copy()) # Important to `.copy()` since the `combination` list will change
                return
            
            # Iterate over each number from the current `i` to `n`
            for num in range(i, n + 1):
                combination.append(num) # Add the current number `num`
                backtrack(num + 1) # backtrack with the next digit
                combination.pop() # Undo the previous decision in preparation for the next interation

        backtrack(1) # Begin backtracking starting at `1` to generate all combinations
        return result
