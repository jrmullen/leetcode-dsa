class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        result = [0] * len(nums)
        groups = [] # List of deques
        groupsMap = {}

        # Sort all of the numbers, then group them together into queues
        for num in sorted(nums):
            # add a new group if there are none, or if the difference is greater than the allowed limit
            if not groups or abs(num - groups[-1][0]) > limit:
                groups.append(deque())
            
            # Add the current `num` to the most recent group
            groups[-1].appendleft(num)
            # Map the `num` to its assigned group
            groupsMap[num] = len(groups) - 1
        
        # Create the final `result` list
        for i, num in enumerate(nums):
            # Determine which group the `num` belongs to by checking the `groupsMap`
            group = groupsMap[num]
            # Pop the smallest number from the `group` and assign it to element `i` in the `result` list
            result[i] = groups[group].pop()

        return result
