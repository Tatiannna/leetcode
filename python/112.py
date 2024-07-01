# 112. Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals targetSum.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0
        stack = deque([(root, 0)]) if root else []

        while stack:
            current = stack.pop()
            currentSum = current[1] + current[0].val 

            #print(f'current node: {current[0].val} Current sum: {currentSum}')

            if not current[0].right and not current[0].left:
                #print('Leaf sum check:', currentSum)
                if currentSum == targetSum:
                    return True
            else:
                if current[0].left:
                    stack.append((current[0].left, currentSum ))
                if current[0].right:
                    stack.append((current[0].right, currentSum))
        return False