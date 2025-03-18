class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counts = Counter(nums)

        for num, count in counts.items():
            # If any of the numbers have an odd count, it will be impossible to create a pair
            if count % 2 != 0:
                return False
        
        return True
