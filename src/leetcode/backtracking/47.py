class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = [] # Each permutation will be recursively built

        # Count the number of times each number occurs in the list of `nums`
        # Intuition: by pushing the `nums` into a frequency map, duplicate descisions will be removed since the keys must all be unique
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        def backtrack():
            # Base case: all numbers have been used
            if len(permutation) == len(nums):
                result.append(permutation.copy()) # Append a snapshotted copy of the current `permuation` list

            # Continue iterating until the base case in met, then backtrack and continue down the next decision path, etc.
            for num, count in freq.items():
                # Skip unavailable numbers
                if count == 0:
                    continue
                
                # Append the new num to the current `permutation` and update the counter
                permutation.append(num) 
                freq[num] -= 1
                
                # Continue recursing until the base case it met
                backtrack()

                # Undo the above decision
                freq[num] += 1
                permutation.pop() 

        # Kick off the DFS to recursively generate all unique permutations
        backtrack()

        return result
