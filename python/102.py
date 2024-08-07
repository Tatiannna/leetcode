# 102. Binary Tree Level Order Traversal

# https://leetcode.com/problems/binary-tree-level-order-traversal/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = defaultdict(list)
        queue = deque([(root, 1)])
        ans = []

        while queue:
            current, lvl = queue.popleft()
            levels[lvl].append(current.val)

            if current.left:
                queue.append((current.left, lvl + 1))
            if current.right:
                queue.append((current.right, lvl + 1))

        for lvl in levels:
            ans.append(levels[lvl])
        
        return ans