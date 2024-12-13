class Solution:
    def maximumLength(self, s: str) -> int:
        substrings = defaultdict(int)

        # Sliding window to find substrings of repeating characters
        l = r = 0
        while r < len(s):
            # If the left point and right pointer are the same character increase the count of all possible substrings
            if s[r] == s[l]:
                for i in range(l, r + 1):
                    substrings[s[l:i+1]] += 1
                # Move the right pointer forward to increase the size of the window
                r += 1
            # Otherwise move the left pointer forward
            else:
                l = r

        result = -1

        # Find all substrings with a count >= 3
        for string, count in substrings.items():
            # Set the `result` to be equal to the longest substring encountered
            if count >= 3 and len(string) > result:
                result = len(string)
        
        return result
