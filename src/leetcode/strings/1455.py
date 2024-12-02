class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # Split the sentence into a list of `words`
        words = sentence.split(" ")

        # Iterate over each word. If the prefix of the `word` matches the `searchWord`, return the index
        for i, word in enumerate(words, 1):
            if len(word) >= len(searchWord) and word[0:len(searchWord)] == searchWord:
                return i + 1 # Answer is expected to be 1-indexed, so add 1
        
        # Finally, once all `words` have been compared, return the default value of `-1`
        return -1
