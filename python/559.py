# 559. Maximum Depth of N-ary Tree


# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        maxDepth = 0
        queue = deque([(root, 1)]) if root else []

        while len(queue) > 0:
            current, lvl = queue.popleft()
            maxDepth = lvl if lvl > maxDepth else maxDepth

            if len(current.children) > 0:
                for child in current.children:
                    queue.append((child, lvl + 1))

        return maxDepth