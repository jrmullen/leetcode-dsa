class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        l = 0
        # Two pointer quick sort approach: pick a single character `0` and iterate over the list with 2 pointers.
        # `l` is the target position, and `r` moves through `s` until a `0` is found. Each swap would move the character
        # 1 place, so the difference `r - l` is the number of swaps it would take to put the 0 into the `l` pointer's position
        for r in range(len(s)):
            if s[r] == '0': # If the right pointer is at a 0, it should be swapped down to the `l` pointer's position
                result += (r - l) # Increase the `result` count by the difference between the pointers
                l += 1 # Move the `l` pointer forward

        return result
