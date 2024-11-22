class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = defaultdict(int) # Maps a tuple or string of row values to count of occurrences
        for row in matrix:
            # Favor rows that begin with a `1`. Convert to a tuple so that it is a legal key in the `count` dict,
            # and then increment the count
            if row[0] == 1:
                count[tuple(row)] += 1
            # For rows that begin with a `0` first invert the numbers in the row before incrementing the `count`
            else:
                # Invert the numbers by XORing them with 1
                for i in range(len(row)):
                    row[i] ^= 1
                count[tuple(row)] += 1
        
        # The row with the highest `count` value can be created the most
        return max(count.values())
