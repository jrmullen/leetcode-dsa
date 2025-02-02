class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = defaultdict(int)

        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1

            # Once the window is of length `k`, start populating the `result` list
            if (r - l) + 1 == k:
                # Calculate the result
                result.append(len(count))

                # Update the `count` to remove the left element to account for the window shifting
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]] # If the count is 0, delete the key from the map
                    
                # Shift the left pointer forward
                l += 1
        
        return result
