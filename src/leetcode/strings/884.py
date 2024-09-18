class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        counts = defaultdict(int)

        # Count the occurence of each word in `s1`
        for word in s1.split(' '):
            counts[word] += 1
        
        # Count the occurence of each word in `s2`
        for word in s2.split(' '):
            counts[word] += 1
        
        # Iterate over the `counts` and build a list of all words that occur only once
        for word in counts:
            if counts[word] == 1:
                result.append(word)
        
        return result
