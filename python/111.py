# 111. Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        lvl = 1 if root else 0
        queue = deque([(root, 1)]) if root else []

        while queue:
            current, lvl = queue.popleft()

            if not current.left and not current.right:
                return lvl
            else:
                if current.left:
                    queue.append((current.left, lvl + 1))
                if current.right:
                    queue.append((current.right, lvl +1))

        return lvl 