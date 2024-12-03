class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = [''] * (len(spaces) + 1) # Pre-populate a list of strings to be joined into the final result string
        start = 0 # Starting index for slicing words from the string
        for i, space in enumerate(spaces):
            words[i] = s[start:space] # Slice each word from `s` and add it to the list of `words` 
            start = space # Update the `start` to begin the next slice where the current word left off

        # Add the remainder of the string `s` to the last index of the `words` list
        words[-1] += s[start:]
        
        # Finally, return all of the `words` in the list `join()`ed into a space-separated sentence
        return " ".join(words)
