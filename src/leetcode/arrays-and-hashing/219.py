class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        used = set() # Track the last `k` numbers in a HashSet for efficient lookups

        # Iterate over the list of numbers, adding each seen number to the `used` set. Older records outside 
        # of the last `k` numbers will be removed to limit the search to only the window of size k.
        for i, num in enumerate(nums):
            # If the `num` is already in the window, the condition is satisfied
            if num in used:
                return True
            
            # Otherwise add the number to the `used` HashSet
            used.add(num)
            
            # Finally, shrink the window if it's exceeding size `k`
            if len(used) > k:
                used.remove(nums[i - k]) # Eject the number from the list `k` indexes back
        
        # If all previous checks have failed, there does not exist a duplicate
        return False
