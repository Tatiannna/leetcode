
# 104. Maximum Depth of Binary Tree


# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        maxDepth = 1
        currLevel = 1

        if not root:
            return 0
        else:
            queue = [(root, currLevel)]

            while len(queue) > 0:
                current = queue.pop(0)

                if current[0].left:
                    queue.append((current[0].left, current[1] + 1))
                if current[0].right:
                    queue.append((current[0].right, current[1] + 1))
                maxDepth = current[1] if current[1] > maxDepth else maxDepth

            return maxDepth 