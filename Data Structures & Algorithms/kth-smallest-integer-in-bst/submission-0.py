# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # THIS IS A O(nlogn) SOLN, THIS IS NOT ACCEPTABLE

        # define a function that captures all the items in the bst
        def capture(node: Optional[TreeNode], arr: list) -> None:
            if not node:
                return
            arr.append(node.val)
            capture(node.left, arr)
            capture(node.right, arr)

        # store them in lst
        lst = []
        capture(root, lst)

        # sort lst
        srtd = sorted(lst)

        #return the k-1 th index
        return srtd[k - 1]
