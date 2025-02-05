class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        diff = 0

        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]

            # Increase the `freq` count for both characters
            freq1[char1] += 1
            freq2[char2] += 1

            # If the characters are different, increment the `diff` counter
            if char1 != char2:
                diff += 1
            
            # If there are more than 2 differing characters, more than 1 swap would be needed
            if diff > 2:
                return False
        
        # Finally, if the strings have the same number of characters they will be identical after 1 swap
        return freq1 == freq2
