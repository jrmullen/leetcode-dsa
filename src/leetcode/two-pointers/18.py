class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        Iterative hard-coded 4Sum solution
        '''
        N = len(nums)
        nums.sort() # Sort the input so it's easier to skip duplicate quadruplets
        result = set() # Store the result as a HashSet to eliminate duplicates

        for i in range(N - 3): # Iterate until the 3rd to last element
            if i > 0 and nums[i] == nums[i - 1]: # Skip duplicate values to keep quadruplets unique
                continue
            for j in range(i + 1, N - 2): # Iterate until the 2nd to last element
                if j > i + 1 and nums[j] == nums[j - 1]: # Skip duplicate values to keep quadruplets unique
                    continue

                # For the final 2 pointers start them at opposite ends of the list
                l = j + 1
                r = N - 1
                while l < r: # Iterate until the pointers meet
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target: # If the total is less than the target, increment the left pointer
                        l += 1
                    elif total > target: # If the total is greater than the target, decrement the right pointer
                        r -= 1 
                    else: # If the total is equal to the target add the quadruplet to the result set and move the pointers inward
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1 # Move both pointers inward at least 1 time
                        r -= 1
                        while l < r and nums[l - 1] == nums[l]: # Skip duplicate values to keep quadruplets unique
                            l += 1
                        while l < r and nums[r + 1] == nums[r]:
                            r -= 1
        
        # # Finally, return the final set of quadruplets as a list
        return list(result)

        '''
        Recursive arbitrary Ksum solution
        '''
        result = []
        N = len(nums)
        nums.sort()
        quad = []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, N - k + 1):
                    if i > start and nums[i] == nums[i - 1]: # Skip duplicate values to keep quadruplets unique
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            # Base case: k == 2, use 2 pointer approach
            l = start
            r = N - 1
            while l < r: # Iterate until the pointers meet
                if nums[l] + nums[r] < target: # If the total is less than the target, increment the left pointer
                    l += 1
                elif nums[l] + nums[r] > target: # If the total is greater than the target, decrement the right pointer
                    r -= 1
                else: # If the total is equal to the target add the quadruplet to the result set and move the pointers inward
                    result.append(quad + [nums[l], nums[r]])
                    l += 1 # Move an arbitrary pointer inward
                    while l < r and nums[l] == nums[l - 1]: # Skip duplicate values to keep quadruplets unique
                        l += 1
                
        # Begin recursing with a `k` of 4 since we want to find unique quadruplets. Starting index of 0, targeting a value of `target`
        kSum(4, 0, target)
        return result