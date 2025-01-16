class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = num1

        # Count the number of bits in `num1`
        count1 = 0
        while num1:
            count1 += num1 & 1
            num1 >>= 1

        # Count the number of set bits in `num2`
        count2 = 0
        while num2:
            count2 += num2 & 1
            num2 >>= 1 # Shift left

        i = 0

        # If `num2` has more set bits than `num1`, set the extra bits to the least significant place possible
        while count2 > count1:
            # If the bit in the `i`th place is NOT set, set it
            if not result & (1 << i):
                result = result | (1 << i)
                count2 -= 1
            i += 1
            
        # If `num2` has less bits than `num1`, set the available bits in the most significant place possible,
        # which implies un-setting the least significant bits in `nums1`
        while count2 < count1:
            # If the bit in the `i`th place is set, un-set it
            if result & (1 << i):
                result = result ^ (1 << i) # Un-set the bit (1 ^ 1 = 0)
                count1 -= 1
            i += 1

        return result
