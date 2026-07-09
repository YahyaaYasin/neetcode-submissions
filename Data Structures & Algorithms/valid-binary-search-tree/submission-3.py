# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def lowestOnRight(node: Optional[TreeNode]) -> int:
            
            num = node.val
            while node.left:
                node = node.left
                num = node.val
            return num

        def highestOnLeft(node: Optional[TreeNode]) -> int:

            num = node.val
            while node.right:
                node = node.right
                num = node.val
            return num
        
        # base case
        if not root:
            return True 

        # if only root node and no children 
        if not root.right and not root.left:
            return True
        
        # if no right node, check left
        if not root.right:
            return highestOnLeft(root.left) < root.val and self.isValidBST(root.left)

        # if no left node, check right
        if not root.left:
            return lowestOnRight(root.right) > root.val and self.isValidBST(root.right)
        
        # if all node is there, check the BST property: left < root < right
        if highestOnLeft(root.left) >= root.val or lowestOnRight(root.right) <= root.val:
            return False
        
        # iterate on both
        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)

        # use "and" since both side must be valid
        return l and r