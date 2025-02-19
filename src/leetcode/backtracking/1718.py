class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * ((2 * n) - 1) # There will be 2 of each number, but only a single 1
        used = set() # Track number that have been successfully placed

        def backtrack(i):
            # Base case: if the final `result` string has been fully populated, a solution has been found
            if i == len(result):
                return True
            
            # Iterate over each number backwards from N to 1
            for num in reversed(range(1, n + 1)):
                # Skip numbers that have already been placed
                if num in used:
                    continue
                
                # Do not go out of bounds or overwrite pre-existing non-zero values
                if num > 1 and (i + num >= len(result) or result[i + num] != 0):
                    continue
                
                used.add(num) # Mark `num` as used
                result[i] = num # Populate the `result` list
                if num > 1:
                    result[i + num] = num
                
                # Find the next unfilled element in the `result` list
                j = i + 1
                while j < len(result) and result[j]:
                    j += 1
                
                # Recurse to attempt to fill the next unfilled element
                if backtrack(j):
                    return True
                
                # Un-do the previous decision (backtrack)
                used.remove(num) # Un-mark `n` as used
                result[i] = 0
                if num > 1:
                    result[i + num] = 0
            
            # Finally, return `False` if no previous operations were successful
            return False

        # Begin backtracking starting at index `0`
        backtrack(0)

        return result
