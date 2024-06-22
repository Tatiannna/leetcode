






# 653. Two Sum IV - Input is a BST

# Given the root of a binary search tree and an integer k, return true if there exist two elements
# in the BST such that their sum is equal to k, or false otherwise.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        queue = [root]

        while len(queue) > 0:
            current = queue.pop(0)

            if k - current.val in nums:
                return True
            else:
                nums.add(current.val)

            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
