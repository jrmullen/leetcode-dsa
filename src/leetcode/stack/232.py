class MyQueue:

    def __init__(self):
        self.stack = deque() # The main stack that will always keep the first element added on top
        self.stack2 = deque() # Utility stack for reversing the order of the elements in the main stack

    def push(self, x: int) -> None:
        # Push everything on the stack onto the second stack to reverse their order
        while len(self.stack) > 0:
            self.stack2.append(self.stack.pop())
        
        self.stack2.append(x) # Append the new integer x to the reversed stack2

        # Finally, push everything back into the original stack so the new value x is at the bottom
        while len(self.stack2) > 0:
            self.stack.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1] # The front of the queue will be at the top of the stack

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
