# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        goodCount=0
        
        def helper(root, greatest):

            nonlocal goodCount

            if not root:
                return 0

            if root.val >= greatest:
                goodCount += 1

            greatest=max(greatest, root.val)

            helper(root.right, greatest)
            helper(root.left, greatest)
        
        helper(root, greatest=-100000)
        return goodCount

        


        