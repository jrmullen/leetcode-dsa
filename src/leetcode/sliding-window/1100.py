class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        result = 0
        l = 0
        r = 0
        counts = [0] * 26 # 1 element for each lowercase letter of the alphabet
        
        for r in range(len(s)):
            char = ord(s[r]) - ord('a') # Convert to an integer between 0 and 25

            # Mark the `char` as seen
            counts[char] += 1

            while counts[char] > 1:
                # Eject the leftmost element from the window and move the left pointer forward
                counts[ord(s[l]) - ord('a')] -= 1
                l += 1

            # If the window is size `k` and the `char` has not already been seen the window contains a valid substring
            if (r - l) + 1 == k:
                result += 1

                # Eject the leftmost element from the window and move the left pointer forward
                counts[ord(s[l]) - ord('a')] -= 1
                l += 1

        return result
