class Solution:
    def numDecodings(self, s: str) -> int:
        # If the first character of `s` is `0`, it is not decodable
        if s[0] == '0':
            return 0
        
        # Initialize `dp` to store results of each sub-problem
        # `dp[i]` represents the number of ways to decode `s` from `0` to `i - 1`
        dp = [0] * (len(s) + 1)
        # Base case: first and second elements of `dp` will always be 1
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            # Check if `s[i - 1]` contains a valid number 1-9
            if 1 <= int(s[i - 1]) <= 9:
                dp[i] += dp[i - 1]
            
            # Check if s[i - 1] and s[i - 2] together make a valid 2-digit number 10-26
            if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]
        
        # Return the last element of `dp` containing the total sum of all sub-problems
        return dp[-1]
