class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Initialize a `dp` list to track the number of extra characters at each position in `s`.
        # Include an extra element to account for the first character potentially being an extra character
        dp = [0] * (len(s) + 1)

        # Convert the `dictionary` into a HashSet for efficient lookups
        dictionary = set(dictionary)

        for start in range(len(s) - 1, -1, -1):
            # Initialize the `start` as 1 greater than its neighboring position to account for `start`
            # being an extra character
            dp[start] = 1 + dp[start + 1]

            # Iterate over each possible substring starting at `start`
            for end in range(start, len(s)):
                if s[start:end + 1] in dictionary:
                    # If a substring exists, compare with the last word and keep the smaller value
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]
