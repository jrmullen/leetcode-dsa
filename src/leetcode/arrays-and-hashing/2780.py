class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count_left = defaultdict(int) # num: count
        count_right = defaultdict(int) # num: count

        # Count the numbers in the `nums` list
        for num in nums:
            count_right[num] +=  1
        
        # Iterate over each index `i` to find the minimum index of a valid split
        for i in range(len(nums)):
            # Split at index `i`
            num = nums[i]
            count_right[num] -= 1 # Remove the `num` from the right side count
            if count_right[num] == 0: # If the count hits 0, remove it from the list
                del count_right[num]

            count_left[num] += 1 # Add the `num` to the left side count

            if count_left[num] * 2 > i + 1 and count_right[num] * 2 > len(nums) - i - 1:
                return i # Return as soon as a valid index is found to guarantee the minimum index

        # Default case: no valid index is found
        return -1
