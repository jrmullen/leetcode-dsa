class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Copy the input list
        result = prices.copy()
        stack = deque() # Monotonic decreasing stack containing indexes of `prices`

        # Iterate over each index
        for i in range(len(prices)):
            # Process all items that can be discounted by the current price of `i`
            while stack and prices[stack[-1]] >= prices[i]:
                # Pop the item from the top of the stack and apply the current price as the discount
                result[stack.pop()] -= prices[i]
            
            # Push the current index into the stack
            stack.append(i)

        return result
