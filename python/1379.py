
# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree


# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        queue = [cloned]

        while len(queue) > 0:

            current = queue.pop(0)
            if current.val == target.val:
                return current
            else:
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)