# 1469. Find All The Lonely Nodes
# https://leetcode.com/problems/find-all-the-lonely-nodes/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque([root])
        res = []

        while queue:
            current = queue.popleft()

            if current.left and current.right:
                queue.append(current.left)
                queue.append(current.right)
            elif current.left and not current.right:
                res.append(current.left.val)
                queue.append(current.left)
            elif current.right and not current.left:
                res.append(current.right.val)
                queue.append(current.right)

        return res