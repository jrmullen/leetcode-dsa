class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Intuition: looking at the end result it becomes obvious that by rotating the array by `k` elements, the last `k` elements
        # of the array will end up at the front, and the first `n - k` elements will end up at the end.
        # To get them into their places by updating the array in-place we can first reverse the original array in place to put the end of the
        # array at the front, then rotate the first `k` elements again to put them in the correct order, and then reverse the last `n - k` elements
        # to put them in the correct order.

        # Helper function to reverse elements of the array in-place starting at the `l` pointer and ending at the `r` pointer
        def reverse_in_place(l: int, r: int) -> None:
            # Continue iterating until the pointers meet in the middle
            while l < r:
                nums[l], nums[r] = nums[r], nums[l] # Swap values in place
                l += 1 # Shift the left pointer inwards
                r -= 1 # Shift the right pointer inwards
        
        N = len(nums)

        # Edge case: `k` could be larger than the list of `nums`, in which case the entire array would be rotated multiple times
        # e.g. if `k` is equal to the number of elements in the list, they would be shifted all the way back to their original locations.
        # By modding `k` by the length of the list, the extra work of rotating past their original location is eliminated
        k = k % N

        # Rotate the entire array in place
        reverse_in_place(0, N - 1)
        
        # Rotate the first `k` elements so they're in their original order
        reverse_in_place(0, k - 1)
        
        # Rotate the last `n - k` elements so they're in their original order
        reverse_in_place(k, N - 1)
