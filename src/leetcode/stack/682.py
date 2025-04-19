class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == 'C': # Invalidate the previous score
                stack.pop()
            elif operation == 'D':
                stack.append(stack[-1] * 2)
            elif operation == '+': # Record a new score that is the sum of the previous two scores
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(operation))
        return sum(stack)
