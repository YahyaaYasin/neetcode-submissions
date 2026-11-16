# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # do a leveled level order
        # return the -1 indexed num of every level

        def levelorder(root, level, lst):

            if not root:
                return []

            if level >= len(lst)  :
                lst.append([])

            lst[level].append(root.val)

            if root.left:
                levelorder(root.left, level+1, lst)

            if root.right:    
                levelorder(root.right, level+1, lst)
        
        res=[]
        level=0
        levelorder(root, level, res)
        out=[]

        for everyLevel in res:
            
            if len(everyLevel) > 0:
                out.append(everyLevel[-1])

        return out
        

            
            





        
        