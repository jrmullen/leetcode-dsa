class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        i = target - 1
        
        while i >= 0:
            if nums[i] + i >= target:
                target = i
            i-= 1

        return target == 0
