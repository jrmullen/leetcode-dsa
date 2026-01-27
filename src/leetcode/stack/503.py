class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] # Monotonic increasing stack, storing index value
        result = [-1] * len(nums)

        # 2 passes to account for the circular array
        for _ in range(2):
            for i, num in enumerate(nums):
                # Anything on the stack that is less than the current number has found their next greater element
                while stack and num > nums[stack[-1]]:
                    result[stack.pop()] = num # Update the number's corresponding index in the result list
                stack.append(i)
        return result
