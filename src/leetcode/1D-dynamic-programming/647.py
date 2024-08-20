class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        # Detect odd-length palindrome:
        # Two pointers, both starting at a midpoint, `i`, traveling outwards 
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1 # Increment the count
                # Progress pointers
                l -= 1
                r += 1
        
        # Detect even-length palindromes:
        # Two pointers, starting adjacent to one another, `i` and `i + 1`, traveling outwards
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1 # Increment the count
                # Progress pointers
                l -= 1
                r += 1

        return result
