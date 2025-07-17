class StockSpanner:

    def __init__(self):
        self.stack = [] # (price, span)
        

    def next(self, price: int) -> int:
        span = 1 # The minimum span value is 1 day (today)

        # Monotonic decreasing stack. Elements are ordered in strictly decreasing order.
        # When pushing a new element, smaller elements at the top are removed until the decreasing order is maintained
        while self.stack and self.stack[-1][0] <= price:
            # Pop the top of the stack and add the previous span's length to the current span total
            prev_price, prev_span = self.stack.pop() 
            span += prev_span
        
        self.stack.append((price, span)) # Push today's price and the final span onto the stack
        return span     


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
