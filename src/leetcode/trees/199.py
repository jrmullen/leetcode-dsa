# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        
        result = []
        q = collections.deque()
        q.append(root)

        # BFS
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()

                # Add the rightmost node at each level to the result
                if i == length - 1:
                    result.append(node.val)

                # Add child nodes to the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
