class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # Store the LCS at each character of both words
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)] # Add 1 row & column to pad the bottom and right with 0s

        # Iterate over each tile of the matrix in reverse order starting at the last character of both words
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] != text2[j]: # If the characters are different set the LCS in `dp` and the largest value between left & down
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                else: # If the characters match add 1 to the down-right diagonal value
                    dp[i][j] = 1 + dp[i + 1][j + 1]

        # The length of the LCS will be in the starting tile of the matrix
        return dp[0][0]
