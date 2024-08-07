
# 572. Subtree of Another Tree

# https://leetcode.com/problems/subtree-of-another-tree/description/




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root1, root2):
            if not root1 and not root2: 
                return True
            elif root1 and root2 and root1.val == root2.val:
                l = sameTree(root1.left, root2.left)
                r = sameTree(root1.right, root2.right)
                return l and r
            else:
                return False

        stack = [root]
        
        while stack:
            current = stack.pop()
            if sameTree(current, subRoot):
                return True
            else:
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

        return False