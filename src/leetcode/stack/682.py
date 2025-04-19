class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] # Initialize a stack to store scores

        for operation in operations:
            if operation == 'C': # Invalidate the previous score
                stack.pop()
            elif operation == 'D': # Record a new score that is the double of the previous score
                stack.append(stack[-1] * 2)
            elif operation == '+': # Record a new score that is the sum of the previous two scores
                stack.append(stack[-2] + stack[-1])
            else: # Record a new score of `operation`
                stack.append(int(operation))
        
        # Return the sum of all elements on the stack
        return sum(stack)
