class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom-up approach:
        # Iterate over each character in `s`, comparing sub-strings against the words in `wordDict`
        
        # Initialize a `dp` list to represent each character/substring in `s` and pre-populate with False, 
        # but include an extra element at the end that is set to `True` as a base case
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        # Start at the end of `s` and work backwards decrementing `i`
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # Create a substring starting at `i`, and compare it against all words in the `wordDict`
                substring = s[i:i + len(word)]

                # If the `word` and `substring` do not match, continue
                if substring != word:
                    continue
                
                # If the next character after `substring` is also a word in `wordDict` we still have a valid
                # solution, so set `dp[i]` to `True`
                if dp[i + len(substring)]:
                    dp[i] = True
                    break
        
        # If the first element is `True` after working backwards, then all words after it must also be True,
        #  and therefore the entire input string `s` can be broken up into words contained in `wordDict`
        return dp[0]
