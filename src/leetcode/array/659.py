class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded_str = ''
        for s in strs:
            # number of characters followed by special character followed by the word, e.g. '4|word'
            encoded_str += str(len(s)) + '|' + s
        return encoded_str

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decoded = []
        i = 0

        while i < len(str):
            j = i
            while j < len(str) and str[j] != '|':
                j += 1
            # i will be the start of our size block
            # j will be the location of our special character "|"
            size = int(str[i:j])  # Elements i->j will contain the length characters
            # Characters after j contain the word, with size telling us how many characters the word is
            word = str[j + 1: j + 1 + size]
            decoded.append(word)
            i += j + 1 + size  # Move the pointer forward to the start of the next size block
        return decoded
