class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        l = 0
        count = defaultdict(int)
        maxFreq = 0

        # Intuition: Maintain a sliding window. K values in the window may be replaced.
        # Therefore there may be up to K characters in the window that do not match the most frequent character.
        # So a valid window may contain up to K characters differing from the most frequent character.
        # windowLength = K + maxFreq
        for r in range(len(s)):
            count[s[r]] += 1

            maxFreq = max(maxFreq, count[s[r]])

            # If the window size - maxFreq exceeds size K, the window is no longer valid, so the left pointer must
            # be shifted to shrink the window until it is once again valid.
            # Remember windowLength = K + maxFreq, which means windowLength - maxFreq <= K
            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
            
        return result
