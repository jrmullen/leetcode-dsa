class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            j, k = i + 1, len(nums) - 1

            # Skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue

            while j < k:
                threeSum = a + nums[j] + nums[k]

                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    # Skip duplicates
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res
