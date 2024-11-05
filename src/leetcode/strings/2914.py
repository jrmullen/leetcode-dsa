class Solution:
    def minChanges(self, s: str) -> int:
        result = 0

        # Iterate over the number as pairs
        for i in range(0, len(s), 2):
            # If the pair of numbers are not equal, a change is requred
            if s[i] != s[i + 1]:
                result += 1

        return result
