class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = '' # Build the prefix string in place

        # Pick an arbitrary string from the `strs` list and iterate over each character
        for i, char in enumerate(strs[0]):
            # Iterate over every word in the list
            for word in strs:
                # If the word is shorter than the current index `i` or if the character at position `i` does not match then the prefix is no longer value
                if len(word) <= i or word[i] != char:
                    return result
            
            # Finally, if validation passed for every word, add the character to the prefix string `result`
            result += char
        return result
