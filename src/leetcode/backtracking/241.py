class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Map each arithmetic operator to a lambda function performing that operation
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }

        def backtrack(left, right):
            result = []

            # Iterate over the input string
            for i in range(left, right  + 1):

                # If the input string contains an arithmetic operator, split the input string into recursive sub-problems
                operation = expression[i]
                if operation in operations:
                    nums1 = backtrack(left, i - 1) # Left side of the operator
                    nums2 = backtrack(i + 1, right) # Right side of the operator

                    # Join the arrays by performing the `operation` on each number
                    for n1 in nums1:
                        for n2 in nums2:
                            result.append(operations[operation](n1, n2))
            
            # Base case: no operator was found in the string, so it contains only a single number. Return the integer value
            if result == []:
                result.append(int(expression[left:right + 1]))

            return result
        
        # Return the resursive result starting at the first and last indexes of the `expresion` list
        return backtrack(0, len(expression) - 1)
