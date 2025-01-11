class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
            result = []
            
            # Count the number of characters in each word in the `words2` list
            charCounts = defaultdict(int)
            for word in words2:
                for char, count in Counter(word).items():
                    # Keep the largest required number of characters across each word
                    charCounts[char] = max(charCounts[char], count)
            
            # Iterate over each `word` in the `words1` list to determine if it is "universal"
            for word in words1:
                c1 = Counter(word) # Count the number of characters in the `word`
                universal = True

                # Compare each character in `c1` with the `charCounts` from `words2`
                for char, c2 in charCounts.items():
                    # If there are not enough characters, flag `universal` as FALSE
                    if c1[char] < c2:
                        universal = False
                        break
                
                # Append any `universal` words to the `result` list
                if universal:
                    result.append(word)

            return result
