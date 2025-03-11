class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0
        l = 0 # Sliding window - left pointer
        counts = defaultdict(int) # Track the number of times each letter appears in the window

        # Expand the window from left to right across the entire string
        for r in range(len(s)):
            counts[s[r]] += 1 # Increment the counter for the new letter

            # Once the window is valid, it will remain valid until the end of the string
            while len(counts) == 3:
                result += len(s) - r # Add each substring to the end of the string to the `result` counter
                counts[s[l]] -= 1 # Shrink the window
                if counts[s[l]] == 0: # Once the count of a letter reaches 0, remove it from the dictionary
                    del counts[s[l]]
                l += 1 # Shift the left pointer forward
        
        return result
