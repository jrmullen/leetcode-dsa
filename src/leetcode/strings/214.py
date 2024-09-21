class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        reversedString = s[::-1]  # Reverse the string

        # Iterate through the string to find the longest palindromic prefix
        for i in range(length):
            # Compare the prefix of `s` with the suffix of `reversedString`
            # If they are equal, the prefix of `s` is a palindrome
            if s[: length - i] == reversedString[i:]:
                # Knowing that the prefix of `s` from 0 to `len(s) - i` is a palindrome, the rest of the string
                # can be made a palindrome by prepending the remaining `i` characters in reverse order,
                # which would be the first `i` characters in the `reversedString`
                # e.g. consider the string `aaaaaaaabcd`
                # The above check would determine that after decrementing `i` from the `len(s)` 3 times the remaining prefix
                # of `s` is a palindrome.
                # `aaaaaaaa` `bcd`
                # The 3 (determined by `i`) suffix characters `bcd` prevent the entire string from being a palindrome. To make the entire string
                # a palindrome those 3 (`i`) suffix characters must be appended to the front of the string in reverse order
                # `dcb` `aaaaaaaa` `bcd`
                return reversedString[:i] + s
        
        # If no palindrome is found, return an empty string
        return ""
