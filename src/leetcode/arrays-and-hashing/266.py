class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Count the number of times each character appears in `s`
        frequencies = Counter(s)
        singles = 0 # Count the number of times

        # Iterate over the count of each character in the `frequencies` map
        for number, count in frequencies.items():
            # If a character has an odd count
            if count % 2 == 1:
                # If `s` has an even number of characters there cannot be any characters with an odd count
                if len(s) % 2 == 0:
                    return False
    
                # If `s` has an odd number of characters that can be at most 1 character with an odd count
                singles += 1
                if singles > 1:
                    return False
        return True
