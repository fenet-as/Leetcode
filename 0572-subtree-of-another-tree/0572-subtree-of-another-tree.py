# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def ec(root,sub):
            if not root and  not sub:
                return True
            if not root or not sub:
                return False
            
            le = ec(root.left,sub.left)
            re = ec(root.right,sub.right)
            return le and re and (root.val == sub.val)
        
        def chk(root,sub):
            if not root:
                return False

            r = ec(root,sub)
             
            return r or chk(root.left,sub) or chk(root.right,sub) 



        return chk(root,subRoot) 

        


        