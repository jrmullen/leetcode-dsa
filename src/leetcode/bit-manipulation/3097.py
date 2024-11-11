class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        result = float('inf')
        bits = [0] * 32
        l = 0

        # Update the `bits` list to add or remove the bits of an integer `n`
        # To add, `diff` will be `1`. To remove, `diff` will be `-1`
        def updateBits(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff
        
        # Convert the `bits` list into its integer representation
        def bitsToInt(bits):
            intValue = 0
            for i in range(32):
                if bits[i]:
                    intValue += (1 << i)
            return intValue

        for r in range(len(nums)):
            # Add bits for new `r`
            updateBits(bits, nums[r], 1)
                

            # Calculate total OR
            orValue = bitsToInt(bits)

            while orValue >= k and l <= r:
                result = min(result, r - l + 1)

                # Remove bits for current `l`
                updateBits(bits, nums[l], -1)
                
                # Re-calculate `totalOr`
                orValue = bitsToInt(bits)

                # Move left pointer forward                
                l += 1

        return -1 if result == float('inf') else result
