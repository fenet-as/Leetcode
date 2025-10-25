# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findMd(rootN):
            if not rootN:
                return 0
            return 1 + max(findMd(rootN.left),findMd(rootN.right))
        return findMd(root)
        