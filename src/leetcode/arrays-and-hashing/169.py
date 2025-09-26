class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Count the number of times each number appears in the list
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # Return the key in freq with the largest value (most frequest number)
        return max(freq.keys(), key=freq.get)
