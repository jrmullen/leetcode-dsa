class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        right = 0
        left = 0

        # Pre-calculate the total number of `1`s in the string `s` and assign them to the `right` value
        for c in s:
            right += 1 if c == '1' else 0
        
        # Iterate over each character in `s` up to the last
        for c in s[0:len(s) - 1]:
            if c == '0': # If the character is a `0`, update the count for the `left` side
                left += 1
            else:        # If the character is a `1`, decrease the count for the `right` side
                right -= 1
            
            # Finally, re-calculate the score, keeping the largest value encountered
            result = max(result, left + right)
        return result
