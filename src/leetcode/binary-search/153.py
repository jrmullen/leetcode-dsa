class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[l]:
                minimum = min(minimum, nums[l])
                l = m + 1
            else:
                minimum = min(minimum, nums[m])
                r = m - 1
        return minimum
