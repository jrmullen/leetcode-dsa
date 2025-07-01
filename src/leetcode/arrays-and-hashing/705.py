class MyHashSet:

    def __init__(self):
        self.map = [False] * (10**6 + 1) # Store values in a fix-size array

    def add(self, key: int) -> None:
        self.map[key] = True # Mark the key as "added"

    def remove(self, key: int) -> None:
        self.map[key] = False # Mark the key as "removed"

    def contains(self, key: int) -> bool:
        return self.map[key] # values are stored as booleans, so just return


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
