# 257. Binary Tree Paths

# https://leetcode.com/problems/binary-tree-paths/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# todo

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        stack = [(root, '')]
        ans = []

        while stack:
            current, path = stack.pop()
            path += str(current.val)

            if not current.left and not current.right:
                ans.append(path)
            if current.left:
                stack.append((current.left, path))
            if current.right:
                stack.append((current.right, path))

        output = []
        for s in ans:
            output.append('->'.join(list(s)))

        return output
