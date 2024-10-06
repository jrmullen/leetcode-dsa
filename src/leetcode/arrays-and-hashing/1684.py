class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0

        # Add the list of allowed characters to a hashSet `allowedChars`
        allowedChars = set(allowed)
        
        # Iterate over each character in each word. If all characters are present in `allowedChars`, increment the `result` counter
        for word in words:
            isDistinct = True
            for char in word:
                if char not in allowedChars:
                    isDistinct = False
                    break # Move on to the next word once an invalid character is encountered
            if isDistinct:
                result += 1
        
        return result
