class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Base case: if there k is larger than the available numbers, there will be none left
        if not num or len(num) < k:
            return '0'
        
        stack = [] # Monotonic decreasing stack

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If there are still digits needed to be removed, remove the leading (most significant) digits
        if k > 0:
            stack = stack[:-k] # Strip the most significant k digits

        result = ''.join(stack) # Convert back to a string
        result = result.lstrip('0') # Strip any leading 0's

        # If there are no digits left, return the default value of 0 instead
        return result if result else '0'
