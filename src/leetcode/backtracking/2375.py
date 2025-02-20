class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = []
        used = set()
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def backtrack(i):
            # Base case: the result string has been successfully built
            if len(result) == n + 1:
                return True

            direction = pattern[i]

            # Iterate from smallest to largest to hit the lexicographically smallest string faster
            for num in nums:
                # Numbers may only be used once - do not allow repeats
                if num in used:
                    continue

                # Validate that the `num` meets the conditions for "I" and "D"
                if direction == 'I' and num <= result[-1]:
                    continue
                
                if direction == 'D' and num >= result[-1]:
                    continue
                
                # If the `num` is valid, append it to the `result` and mark it as used
                result.append(num)
                used.add(num)

                # Recurse to attempt to populate the rest of the `result`
                if backtrack(i + 1):
                    return True
                
                # Undo the previous decision (backtrack)
                result.pop()
                used.remove(num)

            return False
            
        # Attempt to build the string usingg the `nums` from smallest to largest
        for num in nums:
            result.append(num) # Add the number to the `result`
            used.add(num) # Mark the number as used
            if backtrack(0):
                return "".join(str(n) for n in result) # Convert the `result` list to a string and return
            
            # Revert the previous action to prepare for the next iteration
            result.remove(num)
            used.remove(num)
