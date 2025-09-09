class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1 # Move pointers inward
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            # If a mismatched pair is found, try deleting one of them and re-checking if it's a palindrome
            if s[l] != s[r]:
                return is_palindrome(s, l, r - 1) or is_palindrome(s, l + 1, r)
            l += 1 # Move pointers inward
            r -= 1
        
        return True
