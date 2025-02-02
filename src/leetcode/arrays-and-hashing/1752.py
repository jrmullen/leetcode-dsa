class Solution:
    def check(self, nums: List[int]) -> bool:
        shifted = False # Track whether or not the array has been shifted due to the rotation

        # First, compare the first and last elements to check for rotation
        if nums[0] < nums[len(nums) - 1]:
            shifted = True # If there was a rotation, update the flag

        # For every pair, count the number of inversions.
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if shifted: # If a second shift is detected there is more than one rotation and the input is invalid
                    return False
                shifted = True # Flag as shifted if it has not yet been done

        return True
