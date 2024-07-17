# 938. Range Sum of BST

# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        queue = deque([root]) if root else []
        total = 0

        # while queue:
        #     current = queue.popleft()
        #     val = current.val

        #     if val >= low and val <= high:
        #         total += val

        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)

        # return total

        stack = [root] if root else []

        while stack:
            current = stack.pop()
            val = current.val

            if val >= low and val <= high:
                total += val

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return total