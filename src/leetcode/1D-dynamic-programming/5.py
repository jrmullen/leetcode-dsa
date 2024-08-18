class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''

        for i in range(len(s)):
            # Detect odd-length palindrome, e.g. `aba`:
            # Two pointers, both starting at a midpoint, `i`, traveling outwards 
            l, r = i, i

            # While within the bounds of `s` and equal letters
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r + 1] # Update the result if a longer substring palindrome is encountered
                l -= 1 # Progress the pointers
                r += 1

            # Detect even-length palindrome, e.g. abba:
            # Two pointers, starting adjacent to one another, `i` and `i + 1`, traveling outwards
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(result):
                    result = s[l:r + 1]
                l -= 1
                r += 1
        
        return result
