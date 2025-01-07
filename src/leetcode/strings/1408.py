class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        # Nested iteration to compare each with with each other word in the `words` list
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: # Skip comparing the string to itself
                    continue
                
                # If a substring is found, add it to the `result` list and break the current loop
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        
        return result
