class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        result = float('inf')
        count = [0] * 3 # The count of characters OUTSIDE of the window

        # Count the total number of characters in the string `s`
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # If there are not at least `k` of every character it will be impossible to find a valid solution
        if min(count) < k:
            return -1

        # Sliding window technique while inverting the problem
        # Rather than finding the minimum number of characters to form a valid window, find the maximum
        # number of characters that form an INVALID window
        l = 0
        for r in range(len(s)):
            # Decrease the count of characters OUTSIDE the window
            count[ord(s[r]) - ord('a')] -= 1

            # If the window becomes invalid (number of occurences of a character OUTSIDE of the window drop below `k`)
            # shift the left pointer to shrink the window until it is once again valid
            while min(count) < k:
                # The character is not leaving the window, so INCREASE the count OUTSIDE of the window
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            
            # Update the `result` with the smallest VALID window, which would be calculated by taking the
            # largest INVALID window  and subtracting it from the total number of characters in the string
            result = min(result, len(s) - (r - l + 1))
        
        return result
