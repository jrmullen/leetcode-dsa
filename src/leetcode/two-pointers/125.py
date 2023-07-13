class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNum(self, c) -> bool:
        return (ord("A") <= ord(c) <= ord("Z")) or (ord("0") <= ord(c) <= ord("9")) or (ord("a") <= ord(c) <= ord("z"))
