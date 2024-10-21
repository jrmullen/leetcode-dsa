class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = {}
        self.q = deque()

        # Add the list of `nums` to the queue
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        # Since there is not a `self.remove()` function, once an item is non-unique it will never be unique again.
        # Pop non-unique values off the queue so that they do not have to be checked again in repeat calls
        while self.q and not self.unique[self.q[-1]]:
            self.q.pop()
        # Once a non-unique value is found, return its value. If no value is found, return the default `-1`
        return self.q[-1] if self.q else -1

    def add(self, value: int) -> None:
        # If the value exists in the `self.unique` map, then the value must exist in the `self.q` queue.
        # In order to reduce the number of elements to check in `showFirstUnique()`, DO NOT add duplicate values to the queue
        if value not in self.unique:
            self.unique[value] = True
            self.q.appendleft(value)
        else:
            # If the `value` was previously unique, it now has a duplicate so flag it as `False`
            self.unique[value] = False


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
