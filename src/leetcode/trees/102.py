# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        result = []
        queue = collections.deque()
        queue.append(root)

        # BFS
        while queue:
            level = []
            for _ in range(len(queue)):
                # Pop and add the node's value to the level array
                node = queue.popleft()
                level.append(node.val)

                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Once all nodes at a level have been visited, add the the result array
            result.append(level)    
        return result
