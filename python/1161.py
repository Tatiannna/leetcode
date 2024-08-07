# 1161. Maximum Level Sum of a Binary Tree

# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        sums = defaultdict(int)
        queue = deque([(root, 1)])

        while queue:
            current, lvl = queue.popleft()
            sums[lvl] += current.val

            # if sums[lvl] > ans[0]:
            #     ans = (sums[lvl], lvl)

            if current.right:
                queue.append((current.right, lvl + 1))
            if current.left:
                queue.append((current.left, lvl + 1))

        highest = sums[1]
        level = 1

        for lvl in sums:
            if sums[lvl] > highest:
                highest = sums[lvl]
                level = lvl
        return level