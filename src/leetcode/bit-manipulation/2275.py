class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = 0

        # Iterate over each bit position in a 32-bit int
        for i in range(32):
            count = 0 # Track the number of set bits at each position
            # Check the bit's position in each `candidate`
            for num in candidates:
                # Shift each candidate by `i` bits. If the bit at that position is set, increment the count
                count += 1 if num & (1 << i) else 0
            # Update the `result` with the largest number encountered
            result = max(result, count)
        
        return result
