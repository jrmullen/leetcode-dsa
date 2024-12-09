class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result = []
        prefix = [0] * len(nums)

        # Pre-process the list of `nums` to track the invalid indexes
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                prefix[i] = prefix[i - 1] + 1 # If the elements have the same parity increase the invalid index count
            else:
                prefix[i] = prefix[i - 1] # If the parity is different do not increase the invalid index count

        # Iterate over the list of `queries` and deterrmine if each subarray is special using the list of `prefix`es
        for start, end in queries:
            # Intuition: the `prefix` list contains a count of the number of invalid indexes from the beginning of the `nums` list.
            # If the elements `start` and `end` have the same count in the `prefix` list, then there are no invalid elements 
            # between them.
            result.append(prefix[start] == prefix[end])

        return result
