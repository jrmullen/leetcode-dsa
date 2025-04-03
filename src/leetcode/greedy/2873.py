class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = float('-INF')
        N = len(nums)
        i = 0 # `i` pointer starts at the first element

        # Iterate over values from 1 to n-1 as the `j` pointer
        for j in range(1, N - 1):
            # Greedy comparison between `i` and `j` - if `j` is larger, move the `i` pointer forward to maximize `i`
            if nums[j] > nums[i]:
                i = j
            for k in range(j + 1, N):
                # Calculate the `result` and keep the maximum value found
                result = max(result, (nums[i] - nums[j]) * nums[k])
        return result
