class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0

        # Count the number of each character in the string `s`
        chars = Counter(s)

        # If there are more than 2 characters, then there is a possibility for a palindrome subsequence
        for char, count in chars.items():
            if count >= 2:
                # Right the leftmost and rightmost occurrence of the current character `char`
                left = s.find(char)
                right = s.rfind(char)

                # Collect all unique characters between the `left` and `right` index
                middle = set(s[left + 1:right])

                # Each unique `middle` character will form a palindrome, so increase the `result` counter by the number of characters
                result += len(middle)
        
        return result
