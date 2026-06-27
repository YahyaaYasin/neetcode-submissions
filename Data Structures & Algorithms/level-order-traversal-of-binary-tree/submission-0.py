# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # define a helper for collecting based on level
        def helper(node: Optional[TreeNode], level: int, lst: List):
            
            # return when node is None (end of BST)
            if not node:
                return 

            # if a empty list for that level doesnt exist, add a new list
            if len(lst) <= level:
                out.append([])
            
            # add the value on the specific level
            lst[level].append(node.val)

            # iterate on left and right node
            helper(node.left, level+1, lst)
            helper(node.right, level+1, lst)
            
        # pass empty list and level 0
        out = []
        helper(root, 0, out)
        return out

        