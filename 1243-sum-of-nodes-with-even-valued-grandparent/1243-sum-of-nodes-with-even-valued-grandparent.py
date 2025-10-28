# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def chgc(root):
            vs = 0
            if root.left :
                if root.left.left:
                    vs += root.left.left.val
                if root.left.right:
                    vs += root.left.right.val
            if root.right :
                if root.right.left:
                    vs += root.right.left.val
                if root.right.right:
                    vs += root.right.right.val
            return vs
        
        def alls(root):
            sma = 0
            if not root: 
                return 0
            
            if root.val % 2 == 0:
                sma += chgc(root)
    

            ls = alls(root.left)
            rs = alls(root.right)
            sma += ls
            sma += rs
            return sma
        return alls(root)


                

