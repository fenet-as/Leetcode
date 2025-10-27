# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfsr(root,target):
            if not root:
                return False
            if not root.left and not root.right:
                if target == root.val:
                    return True
                return False
            
            
            target -= root.val
            return dfsr(root.right,target) or dfsr(root.left,target)
      
        return dfsr(root,targetSum)
