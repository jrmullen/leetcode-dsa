class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        M, N = len(word1), len(word2)

        # Find the length of the longest string to iterate over both strings using a single pointer
        for i in range(max(M, N)):
            # If there are characters, append them to the `result` string in alternating order
            result += word1[i] if i < M else ''
            result += word2[i] if i < N else ''
        
        return result
