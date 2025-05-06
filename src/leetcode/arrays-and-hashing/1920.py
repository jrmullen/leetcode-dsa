class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Push the value of `nums[num]` into the `result` list for each element in the `nums` list
        return [nums[num] for num in nums]
