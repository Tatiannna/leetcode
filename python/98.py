# 98. Validate Binary Search Tree

# https://leetcode.com/problems/validate-binary-search-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = []

        def inorder(root):
            if not root:
                return True
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True