class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.q = self.q1 # Pointer to track which queue is currently being populated

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        if len(self.q) == 0:
            return
        
        other_q = self.q1 if self.q == self.q2 else self.q2

        # Transfer all but the last element into the other queue
        while len(self.q) > 1: 
            other_q.appendleft(self.q.pop())
        
        popped = self.q.pop() # Remove the final remaining element to "pop" it
        self.q = other_q # Update the q pointer to point to the full queue
        return popped

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
