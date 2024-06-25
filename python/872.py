
# 872. Leaf-Similar Trees


# Consider all the leaves of a binary tree, from left to right order, 
# the values of those leaves form a leaf value sequence.


# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        seq = []

        stack = [root1]

        while stack:
            current = stack.pop()

            if not current.right and not current.left:
                seq.append(current.val)
            else:
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
            

        stack = [root2]
        seq2 = []

        while stack:
            current = stack.pop()
            
            if not current.right and not current.left:
                seq2.append(current.val)
            else:
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)

        return seq == seq2