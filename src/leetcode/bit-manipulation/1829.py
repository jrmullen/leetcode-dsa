class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []

        # Calculate the cumulative XOR value of the `nums` list
        cumulativeXor = 0
        for  num in nums:
            cumulativeXor ^= num
        
        # k < 2maximumBit, so the maximum possible value is 2^maximumBit - 1
        maxK = (2**maximumBit) - 1

        # Start at the end of the array working backwards
        for i in range(len(nums) - 1, -1, -1):
            # By performing an XOR on `cumulativeXor` using `maxK` we are left with the maximum answer value
            result.append(cumulativeXor ^ maxK)

            # Remove the last element of `nums` from the cumulative XOR value
            # A number XORed with itself produces 0, so it cancels itself out, effectively removing it from the total
            cumulativeXor ^= nums[i]
        
        return result
