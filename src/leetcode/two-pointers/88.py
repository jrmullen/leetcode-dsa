class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1 # p1 pointer starts at the largest value in nums1
        p2 = n - 1 # p2 pointer starts at the largest value in nums2

        # Work backwards, populating nums1 from largest to smallest
        for end in range(m + n - 1, -1, -1):
            if p2 < 0: # If all values in `nums2` have been used, the nums1 list will be full
                break

            if p1 >= 0 and nums1[p1] > nums2[p2]: # If the value in the `nums1` list is larger, use its value
                nums1[end] = nums1[p1]
                p1 -= 1 # Move the pointer inward
            else: # Otherwise the value in `nums1` is greater than or equal the value in nums1, so use its value
                nums1[end] = nums2[p2]
                p2 -=1 # Move the pointer inward

        return nums1 # Return the nums1 list after it has been updated in place
