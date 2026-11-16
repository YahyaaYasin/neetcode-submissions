# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # use in-order traversal as it gives you a sorted list of the tree in ascending order

        def inOrderTraversal(root, values):

            if not root:
                return
            
            inOrderTraversal(root.left, values)
            values.append(root.val)
            inOrderTraversal(root.right, values)

        res=[]
        inOrderTraversal(root, res)
        return res[k-1]
