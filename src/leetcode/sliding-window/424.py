class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        frequencies = {}

        for r in range(len(s)):
            frequencies[s[r]] = 1 + frequencies.get(s[r], 0)

            while (r - l + 1) - max(frequencies.values()) > k:
                frequencies[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        return longest
