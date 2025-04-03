class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        # Move left and right pointers inward from the ends of the string `s` until they meet
        while l < r:
            s[l], s[r] = s[r], s[l] # Swap left and right values
            l += 1 # Move pointers
            r -= 1

        # Do not return anything
