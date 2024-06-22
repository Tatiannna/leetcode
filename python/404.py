
# 404. Sum of Left Leaves

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        queue = [root]

        while len(queue) > 0:
            current = queue.pop(0)

            if current.left:
                if not current.left.left and not current.left.right:
                    total += current.left.val
                else:
                    queue.append(current.left)

            if current.right:
                queue.append(current.right)
        return total