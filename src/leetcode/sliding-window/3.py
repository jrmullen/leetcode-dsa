class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        charset = set()

        while r <= len(s) - 1:
            if s[r] not in charset:
                charset.add(s[r])
                longest = max(longest, len(charset))
                r += 1
            else:
                charset.remove(s[l])
                l += 1
        return longest
