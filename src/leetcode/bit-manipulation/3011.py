class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        currentMin = currentMax = nums[0]
        prevMax = float('-inf')

        for num in nums:
            # If the current `num` has the same number of set bits as the current "group"
            # Update the current group's min/max values
            if num.bit_count() == currentMin.bit_count():
                currentMin = min(currentMin, num)
                currentMax = max(currentMax, num)
            # Else the number of set bits does not match, so a new "group" must be started
            else:
                # If the minimum value from the current group is ever less than the maximum value from the previous group
                # it is impossible to sort the array since the values cannot be swapped due to differing set bits
                if currentMin < prevMax:
                    return False
                
                # Update `prevMax` to point to the current maximum
                prevMax = currentMax
                # Update the min/max to be the `num` in the new "group"
                currentMin = num
                currentMax = num
        
        # Edge case: the final "group" must be manually checked since it will never hit the `else` block above
        if currentMin < prevMax:
            return False

        # Finally, if all previous checks have passed return True
        return True
