class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = 0
        counts = Counter(tiles)

        def backtrack(i):
            nonlocal result

            # Base case: all tiles have been used
            if i == len(tiles):
                return
            
            for letter, count in counts.items():
                # If there are no available letters to use, skip it
                if count == 0:
                    continue
                
                counts[letter] -= 1 # Decrease the `counts` counter to mark the tile as used
                result += 1 # Increase the `result` counter to account for the new combination

                # Recurse to use the next tile
                backtrack(i + 1)

                # Un-do the above decision (backtrack)
                counts[letter] += 1
        
        # Backtrack starting at index 0
        backtrack(0)

        return result
