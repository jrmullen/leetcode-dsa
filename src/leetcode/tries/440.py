class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        number = 1 # Start at 1
        i = 1

        # Helper function to calculate the number of steps between the current number and it's neighbor to the right
        def countSteps(current):
            steps = 0
            neighbor = current + 1
            while current <= n:
                # `neighbor - current` will give the number of steps between each value
                # `min(neighbor, n+1)` ensures that the `neighbor` value does not exceed `n`
                steps += min(neighbor, n + 1) - current
                # Move to the next level of the tree
                current *= 10
                neighbor *= 10
            return steps

        while i < k:
            # Count the number of steps between the current number and its neighbor
            steps = countSteps(number)

            # If the number of steps are <= `k`, skip the subtree
            if i + steps <= k:
                # Move to the next number and update the number of steps taken
                number += 1
                i += steps
            else:
                # Move to the next level of the tree
                number *= 10
                i += 1
        
        return number
