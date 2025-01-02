class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        prefix = [0] * len(words)
        streak = 0
        vowels = { 'a', 'e', 'i', 'o', 'u' } # Store vowels in a HashSet for efficient lookups
        
        # Calculate a prefix sum of the number of words that both start and end with a vowel
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                streak += 1

            # Set the final value 
            prefix[i] = streak
        
        # Iterate over each query and calculate the rersult
        for i, (l, r) in enumerate(queries):
            result[i] = prefix[r] - (0 if l == 0 else prefix[l - 1])

        return result
