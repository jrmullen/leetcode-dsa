class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        l = r = 0

        while r <= len(word):
            # If `r` hits the end of list, encounters a new character, or if the window size is `9` characters
            if r == len(word) or word[r] != word[l] or (r - l) == 9:
                comp += str(r - l) + word[l] # Append the length prefix and character to the `comp` string
                l = r # Move the left pointer forward to start a new window

            # Move the right pointer forward
            r += 1         

        return comp
