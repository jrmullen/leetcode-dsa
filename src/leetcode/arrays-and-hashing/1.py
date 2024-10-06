class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in map:
                return [map[difference], i]
            map[n] = i
