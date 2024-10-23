# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree is empty, return immediately
        if not root:
            return root
        
        # BFS level order traversal. Instantiate a queue `q` and append the root node
        q = deque()
        q.appendleft(root)
        lastLevelSum = root.val # default to the value of the `root` node

        while q:
            currentLevelSum = 0

            for _ in range(len(q)):
                # Pop the current Node off of the queue and update it's value
                node = q.pop()
                node.val = lastLevelSum - node.val

                # Calculate the sum of the node's children
                childrenSum = 0
                childrenSum += node.left.val if node.left else 0
                childrenSum += node.right.val if node.right else 0

                if node.left:
                    currentLevelSum += node.left.val # Add the left node's value to the `currentLevelSum`
                    node.left.val = childrenSum # Update the left node's value to be the sum of the pair (current node + it's sibling node)
                    q.appendleft(node.left) # Add the left node to the queue
                if node.right:
                    currentLevelSum += node.right.val
                    node.right.val = childrenSum
                    q.appendleft(node.right)
            
            # Update the `lastLevelSum` to be the sum of all of the current level's child nodes
            lastLevelSum = currentLevelSum
        
        return root
