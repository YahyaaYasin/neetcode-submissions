# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        balanced=True

        def height(node) -> int:

            nonlocal balanced

            left=0
            right=0

            if not node:
                return 0 
            
            left += height(node.left)
            right += height(node.right)

            if left-right not in {-1,0,1}:
                balanced=False

            return 1 + max(right, left)
            
        right_height = height(root.right)
        left_height = height(root.left)

        if (left_height - right_height) not in {-1,0,1}:
            balanced=False
        
        return balanced