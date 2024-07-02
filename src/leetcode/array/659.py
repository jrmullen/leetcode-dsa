class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ''
        for s in strs:
            # number of characters followed by special character followed by the word, e.g. '4|word'
            encoded_str += str(len(s)) + '|' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '|':
                j += 1
            # i will be the start of our size block
            # j will be the location of our special character "|"
            size = int(s[i:j])  # Elements i->j will contain the length characters
            # Characters after j contain the word, with size telling us how many characters the word is
            i = j + 1 # bump `i` to the start of the actual word
            j = i + size # Bump `j` to the end of the actual word
            word = s[i:j] # Parse the actual word
            decoded.append(word)
            i = j  # Move the pointer forward to the start of the next size block
        return decoded


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
