class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.stack = [0] * maxSize
        self.incrementStack = [0] * maxSize # Instead of incrementing every element in place, store increments separately

    # Adds `x` to the top of the stack if the stack has not reached the `maxSize`
    def push(self, x: int) -> None:
        # If the `maxSize` has been reached, do nothing
        if self.size == self.maxSize:
            return

        self.stack[self.size] += x # Add `x` to the stack
        self.size += 1 # Increment the size count

    # Pops and returns the top of the stack or `-1` if the stack is empty
    def pop(self) -> int:
        # If the stack is empty, default to `-1`
        if self.size == 0:
            return -1
        
        value = self.stack[self.size - 1] # Fetch the value from the top of the `stack`
        increment = self.incrementStack[self.size - 1] # Fetch the value from the top of the `incrementStack`
        
        # Update the next value in the `incrementStack`
        if self.size - 2 >= 0:
            self.incrementStack[self.size - 2] += increment
        
        # Remove the popped values from the `stack` and `incrementStack`
        self.stack[self.size - 1] = 0
        self.incrementStack[self.size - 1] = 0

        self.size -= 1 # Decrease the size count
        return value + increment # Return the sum

    # Increments the bottom `k` elements of the stack by `val`. If there are less than `k` elements in the stack, increment all the elements in the stack
    def increment(self, k: int, val: int) -> None:
        # If the stack is empty, do nothing
        if self.size == 0:
            return
        # If the `size` of the stack is less than `k`, use the `size` instead
        self.incrementStack[min(self.size - 1, k - 1)] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
