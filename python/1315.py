# 1315. Sum of Nodes with Even-Valued Grandparent

# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # res = 0
        # nodes = defaultdict(list)

        # stack = [(root, 1)]

        # while stack:
        #     current, lvl = stack.pop()

        #     if current.val % 2 == 0:
        #         nodes[lvl].append(current.val)

        #     if lvl - 2 in nodes:
        #         print("adding: ", current.val)
        #         res += current.val

        #     if current.right:
        #         stack.append((current.right, lvl + 1))
        #     if current.left:
        #         stack.append((current.left, lvl + 1))
        #     if not current.left and not current.right:
        #         nodes[lvl - 2] = []
        # return res

         def getGrandSum(node):
            res = 0
            if node.left or node.right:
                if node.left:
                    if node.left.left:
                        res += node.left.left.val
                    if node.left.right:
                        res += node.left.right.val
                if node.right:
                    if node.right.left:
                        res += node.right.left.val
                    if node.right.right:
                        res += node.right.right.val
            return res

        ans = 0

        stack = [root]

        while stack:
            current = stack.pop()
            if current.val % 2 == 0:
                ans += getGrandSum(current)

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return ans