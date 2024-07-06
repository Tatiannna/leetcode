# 1302. Deepest Leaves Sum

# Given the root of a binary tree, return the sum of values of its deepest leaves.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        deepestLvl = 1
        total = 0
        # if you are a leaf AND you are on deepest level, add to sum
        stack = [(root,1)]

        while stack:
            current, lvl = stack.pop()

            if not current.left and not current.right:
                if lvl == deepestLvl:
                    total += current.val
                elif lvl > deepestLvl:
                    total = current.val
                    deepestLvl = lvl
            if current.right:
                stack.append((current.right, lvl +1))
            if current.left:
                stack.append(( current.left, lvl +1))

        return total  