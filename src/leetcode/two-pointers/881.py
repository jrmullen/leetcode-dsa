class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort() # Sort the input in ascending order
        l, r = 0, len(people) - 1 # Two pointers. One at each end of the list

        # Continue iterating until the pointers meet
        while l <= r:
            # Greedily choose the heaviest person if possible to minimize pairs
            result += 1

            # If the lightest person available can also fit, include them to minimize the number of pairs
            if people[r] + people[l] <= limit:
                l += 1 # Move pointers inward
            r -= 1

        return result
