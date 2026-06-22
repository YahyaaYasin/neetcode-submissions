# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # define a helper which once found a matching root, checks if the whole subtree 
        # matches or not and returns the result

        def helper(main: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:

            # base case: if both are none, it means we reached end of the tree
            if not main and not sub:
                return True

            # base case: if main exists but subtree is none, then it means the subtree 
            # matches but the main tree extends further so returns false
            if not main or not sub:
                return False

            # main checker
            if main.val != sub.val:
                return False

            # recursive calls
            return helper(main.right, sub.right) and helper(main.left, sub.left)

        # base case
        if not root:
            return False

        # if we find a match, we call the helper to verify the whole subtree and return
        if root.val == subRoot.val and helper(root, subRoot):
            return True

        # iterate over both right and left subtrees
        r1 = self.isSubtree(root.right, subRoot)
        r2 = self.isSubtree(root.left, subRoot)

        # Use "or" since the subroot can only be in either of them, not both
        return r1 or r2

        


        
