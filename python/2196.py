# 2196. Create Binary Tree From Descriptions

# https://leetcode.com/problems/create-binary-tree-from-descriptions/description/?envType=daily-question&envId=2024-07-14



# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        nodes = defaultdict(list)
        vals = {}
        parents = set()
        children = set()

        for description in descriptions:

            parent_val = description[0]
            child_val = description[1]
            isleft = True if description[2] == 1 else False

            # Child node may already exist as parent of a diff node
            if child_val not in vals:
                c = TreeNode(child_val)
                vals[child_val] = c

            # Check if parent is already a key (in vals), because if its an unseen key, you must create a new Treenode object
            if parent_val not in vals:
                p = TreeNode(parent_val)
                vals[parent_val] = p

            # Both Treenode objects now exist for sure, add to children and parent sets
            children.add(vals[child_val])
            if vals[parent_val] not in children:
                parents.add(vals[parent_val])

            # make parent-child connection in dictionary
            nodes[vals[parent_val]].append(nodes[vals[child_val]])
            
            # made TREE connection
            if isleft:
                vals[parent_val].left = vals[child_val] 
            else:
                vals[parent_val].right = vals[child_val]

        # If node is child, then it cannot be root

        root = next(iter(parents - children))

        return root