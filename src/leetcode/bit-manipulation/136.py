class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach: XOR bitwise operation
        # a XOR 0 = a
        # a XOR a = 0
        # By performing an XOR operation on every element in `nums`, the final value of `a` will be the singular number
        a = 0
        for n in nums:
            a ^= n
        return a
