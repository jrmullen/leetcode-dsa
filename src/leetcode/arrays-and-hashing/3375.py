class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()

        for num in nums:
            # Only numbers greater than the valid number `h` can be updated, so if there are any numbers less than
            # `k` it will be impossible to make every element equal to `k`
            if num < k:
                return -1
            
            # If the `num` is greater than `k` it can be transformed by performing the operation
            if num > k:
                # Add the `num` to the set of encountered numbers
                seen.add(num)
        
        # The count of unique numbers will equal the minimum number of operations needed
        return len(seen)
