class TreeNode:
    def __init__(self, start, end) -> None:
        self.left = None # The left node should always have a `start` less than the current node's
        self.right = None # The right node should always have a `start` greater than the current node's
        self.start = start
        self.end = end


class Tree:
    def __init__(self) -> None:
        self.root = None
    
    # Insert a booking into the tree. If there are conflicts it will return `False`, otherwise `True`
    def insert(self, start, end) -> bool:
        currentNode = self.root

        # If there is not yet a root node, create one
        if not self.root:
            self.root = TreeNode(start, end)
            return True

        # Iterateover the leaf nodes of the `Tree` until a conflict is found or a new Node can be created
        while currentNode:
            # If the new booking's `start` time is greater than the `end` time of the `currentNode`, traverse right
            if start >= currentNode.end:
                # If there is no leaf node, insert one for the new booking, else continue traversing the tree
                if not currentNode.right:
                    currentNode.right = TreeNode(start, end)
                    return True
                currentNode = currentNode.right
            # If the new booking's `end` time is less than the `start` time of the `currentNode`, traverse right
            elif end <= currentNode.start:
                # If there is no leaf node, insert one for the new booking, else continue traversing the tree
                if not currentNode.left:
                    currentNode.left = TreeNode(start, end)
                    return True
                currentNode = currentNode.left
            # There is a scheduling conflict - the booking is not possible
            else:
                return False


class MyCalendar:
    def __init__(self):
        self.calendar = Tree()

    def book(self, start: int, end: int) -> bool:
        return self.calendar.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
