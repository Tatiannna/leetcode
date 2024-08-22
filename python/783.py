
# 783. Minimum Distance Between BST Nodes


# Given the root of a Binary Search Tree (BST), return the minimum difference between 
# the values of any two different nodes in the tree.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        nums = []
        # queue = [root] if root else []

        # while len(queue) > 0:
        #     current = queue.pop(0)
        #     nums.append(current.val)

        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)
        # nums.sort()

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        inorder(root)

        minDistance = abs(nums[0] - nums[1])

        for i in range(len(nums)-1):
             minDistance = min(nums[i] - nums[i+1], minDistance)
        return minDistance