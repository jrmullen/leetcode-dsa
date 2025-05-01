class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Fancy one-liner
        #return sum(1 if len(str(num)) % 2 == 0 else 0 for num in nums)
        
        result = 0 # Track the number of `nums` with an even number of digits

        # Iterate over the list of `nums`
        for num in nums:
            # Cast the `num` to a string type, and leverage the `len()` function to determine the number of digits
            if len(str(num)) % 2 == 0:
                result += 1 # If there are an even number of digits, increment the `result` counter
        
        return result
