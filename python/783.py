
# 783. Minimum Distance Between BST Nodes


# Given the root of a Binary Search Tree (BST), return the minimum difference between 
# the values of any two different nodes in the tree.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        min1 = float('inf')
        min2 = float('inf')
        nums = []

        # if min1 > min2:
        #     temp = min1
        #     min1 = min2
        #     min2 = temp

        # print(min1, min2)

        queue = [root] if root else []

        while len(queue) > 0:
            current = queue.pop(0)
            nums.append(current.val)

            # if current.val < min2:
            #     if current.val < min1:
            #         min2 = min1
            #         min1 = current.val
            #     else:
            #         min2 = current.val

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        # print( min1, min2)
        # return min2 - min1

        nums.sort()

        minDistance = abs(nums[0] - nums[1])

        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) < minDistance:
                minDistance = abs(nums[i] - nums[i+1])

        return minDistance