# 515. Find Largest Value in Each Tree Row

# Given the root of a binary tree, return an array of the largest 
# value in each row of the tree (0-indexed).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        
        queue = deque([(root, 1)]) if root else []

        while queue:
            current, lvl = queue.popleft()
            if len(arr) < lvl:
                arr.append(current.val)
            else:
                if arr[lvl-1] < current.val:
                    arr[lvl -1] = current.val
            
            if current.left:
                queue.append((current.left, lvl + 1))
            if current.right:
                queue.append((current.right, lvl + 1))

        return arr 