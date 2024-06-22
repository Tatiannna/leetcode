
# 993. Cousins in Binary Tree


# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        # cousins mean same grandparent
        # for every node, when pushed in queue, check grandchildren to see if == x and y
        # if you find one value and not the other, return False
        # if you find no values, continue to search tree


        ''' for every node, lvl in queue
            save parent
            if match for x or y, save parent. 
            Next match must 
            be on same level and 
            NOT have same parent
        '''
         
        grannyx = None
        grannyy = None
        parentx = None
        parenty = None
        levelx = None
        levely = None

        # queue = [(root, 1)]
        queue = deque([(root, 1)])

        while len(queue) > 0:
            current, lvl = queue.popleft()

            # if current.val = x:
            #     parent = current
            #     if parenty and parenty != parentx:
            #         return True
            # elif current.val == y:
            #     parenty = current
            #     if parentx and parentx 

            if current.left:
                if current.left.val == x:
                    parentx = current
                    levelx = lvl
                elif current.left.val == y:
                    parenty = current
                    levely = lvl

                queue.append((current.left, lvl + 1))

            if current.right:
                if current.right.val == x:
                    parentx = current
                    levelx = lvl
                elif current.right.val == y:
                    parenty = current
                    levely = lvl
                queue.append((current.right, lvl + 1))

            
        return parentx and parenty and parentx != parenty and levelx == levely
            
            #     if current.left.left:
            #         queue.append(current.left.left)
            #         if current.left.left.val == x:
            #             grannyx = current
            #             parentx = current.left
            #         elif current.left.left.val == y:
            #             grannyy = current
            #             parenty = current.left

            #     if current.left.right:
            #         queue.append(current.left.right)
            #         if current.left.right.val == x:
            #             grannyx = current
            #             parentx = current.left

            #         elif current.left.right.val == y:
            #             grannyy = current
            #             parenty = current.left

            # if current.right:
            #     queue.append((current.right, lvl + 1, current)

            #     if current.right.left:
            #         queue.append(current.right.left)
            #         if current.right.left.val == x:
            #             grannyx = current
            #             parentx = current.right
            #         elif current.right.left.val == y:
            #             grannyy = current
            #             parenty = current.right

            #     if current.right.right:
            #         queue.append(current.right.right)
            #         if current.right.right.val == x:
            #             grannyx = current
            #             parentx = current.right

            #         elif current.right.right.val == y:
            #             grannyy = current
            #             parenty = current.right





        return grannyx and grannyx == grannyy and parentx != parenty