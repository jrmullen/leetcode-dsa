class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If `t` is a longer string than `s` it cannot be a substring
        if len(t) > len(s):
            return result
        
        # Count characters in `t` and `s` respectively
        countT = defaultdict(int)
        countS = defaultdict(int)
        shortest = float('inf') # Track the length of the shortest `result` string encountered
        result = ''

        # Populate the count dict `ct` of characters in `t`
        for c in t:
            countT[c] += 1
        
        found = 0
        l = 0

        # Intuition: sliding window technique expanding the window until all characters in `t` have been found,
        # then move the left pointer forward to shrink the window until it no longer contains all characters in `t`
        for r in range(len(s)):
            countS[s[r]] += 1

            # Once the correct number of a specific character in `t` have been found, increment the `found` counter
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                found += 1

            # Once all the needed characters in `t` have been found shrink the window to find the smallest valid substring
            while current == len(countT):
                # If the window is smaller than the shortest valid window encountered, update the `result` string
                if (r - l + 1) < shortest:
                    result = s[l:r + 1]
                    shortest = len(result)
                
                countS[s[l]] -= 1

                # If the number of any characters in `t` drops below the required amount, decrement the `found` counter
                # to break out of the loop
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    found -= 1

                # Finally, move the left pointer forward to shrink the window
                l += 1

        return result
