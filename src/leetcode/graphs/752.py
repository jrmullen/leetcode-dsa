class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        result = -1 # Start at -1 so the first iteration will bump the counter to the expected value of 0
        q = deque()

        # Create a set to prevent re-visiting combinations
        visited = set(deadends) # Add the list of deadends so they're unvisitable

        # Base case: if the starting state is a dead end, the combination is impossible to solve
        if '0000' in deadends:
            return -1
        
        q.append('0000') # Push the starting sequence onto the queue
        visited.add('0000') # Mark the starting combination as visited

        # Standard BFS
        while q:
            # Process the current "level" of the decision tree
            result += 1 # Increment the number of moves
            for _ in range(len(q)):
                combination = q.pop()
                
                # The decision tree is explored 1 level at a time. As soon as the `target` is found we can be confident it is the minimum value
                if combination == target:
                    return result

                # 8 total moves possible. Each index 0-3 has 2 possible moves -- up or down the number wheel
                for i in range(4):
                    up = ((int(combination[i]) - 1 + 10) % 10) # Scroll the wheel up, e.g. 0 -> 9
                    up_combination = combination[:i] + str(up) + combination[i+1:] # Create the updated combination
                    if up_combination not in visited:
                        q.appendleft(up_combination) # Add the combination to the queue
                        visited.add(up_combination) # Mark the combination as visited

                    down = (int(combination[i]) + 1) % 10 # Scroll the wheel down, e.g. 9 -> 0
                    down_combination = combination[:i] + str(down) + combination[i+1:]
                    if down_combination not in visited:
                        q.appendleft(down_combination) # Add the combination to the queue
                        visited.add(down_combination) # Mark the combination as visitedd
        
        # If the `target` was never hit during the BFS, return the default value
        return -1
