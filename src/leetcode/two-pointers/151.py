class Solution:
    def reverseWords(self, s: str) -> str:
        # Cheater solution using Python built-ins
        # ---------------------------------------
        return " ".join(reversed(s.split()))

        # Two pointer solution
        # ---------------------------------------
        l, r = 0, len(s) - 1
        
        # Trim leading whitespace
        while l <= r and s[l] == ' ':
            l += 1
        
        # Trim trailing whitespace
        while r >= l and s[r] == ' ':
            r -= 1
        
        # Add words to a list so they can be modified
        words = []
        while l <= r:
            if s[l] != ' ': # Append non-word characters
                words.append(s[l])
            elif words[-1] != ' ': # Append spaces, but only allow 1 at a time
                words.append(s[l])
            l += 1
        
        # Reverse the entire string
        words = words[::-1]

        # Reverse each individual word to read forwards again
        l, r, nextWord = 0, 0, 0
        while r <= len(words) - 1:
            # Move the right pointer until the end of a word (a space) is reached
            if r + 1 > len(words) - 1 or words[r + 1] == ' ':
                nextWord = r + 2 # Save the index of the start of the next word
                while l < r:
                    # Swap characters and move the pointers inward
                    words[r], words[l] = words[l], words[r]
                    l += 1
                    r -= 1
                # Once all characters have been swapped, move the pointers to the start of the next word
                r, l = nextWord, nextWord
            else:
                r += 1
        
        # Convert the `words` list back into a string
        return "".join(words)
