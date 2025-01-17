class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0 # Start with 0 since anything XORed with 0 is itself
        
        # Intuition: Each element in `num1` will be XORed with each element from `nums2`.
        # e.g. nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[0] ^ nums2[2], ..... nums1[0] ^ nums2[n]
        # Therefore the resulting array will have `nums1[0]` XORed `len(nums2)` times.
        # Knowing that along with the properties of XOR, if `nums2` has an even number of elements, all of the XORs
        # of `nums1[0]` will cancel out. If `nums2` has an odd number of elements, all of the `nums[0]` will be canceled
        # out except for 1 of them.

        # If there are an odd number of elements in `nums2`, each number in `nums1` will occur once in the final `nums3` list
        if len(nums2) % 2 == 1:
            # XOR each element in `nums1` with the `result`
            for num in nums1:
                result ^= num
        
        # If there are an odd number of elements in `nums1`, each number in `nums2` will occur once in the final `nums3` list
        if len(nums1) % 2 == 1:
            # XOR each element in `nums2` with the `result`
            for num in nums2:
                result ^= num

        return result
