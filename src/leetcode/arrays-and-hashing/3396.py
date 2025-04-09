class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()

        # Iterate over the list of numbers in reverse order
        for num in reversed(nums):
            # If the `num` has already been seen, the number is no longer distinct
            if num in seen:
                break # Exit the loop
            
            seen.add(num) # Add the `num` to the set of numbers
        
        # The length of the `seen` set is the number of distinct elements at the tail of the array
        nondistinct_count = len(nums) - len(seen)
        
        # The remaining nondistinct indexes must be removed 3 at a time, so round up
        return ceil(nondistinct_count / 3)
