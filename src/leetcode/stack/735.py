class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        # Iterate over the list of asteroids from left to right
        for asteroid in asteroids:
            # If the asteroid is moving to the right, add it to the stack and continue iterating
            if asteroid > 0:
                stack.append(asteroid)
                continue

            # If the asteroid is moving to the left while there are 1 or more asteroids moving to the right
            while stack and stack[-1] > 0:
                if stack[-1] < abs(asteroid): # The `asteroid` destroys any existing right-moving asteroids with a smaller size
                    stack.pop()
                    continue # Continue to check if the next right-moving asteroid in line will also be destroyed
                elif stack[-1] == abs(asteroid): # Both asteroids are destroyed
                    stack.pop()
                break # Stop iterating
            else: # While .. else -- will execute when the `while` condition evaluates to `False`
                stack.append(asteroid)
        
        # Return the list containing the remaining asteroids
        return stack
