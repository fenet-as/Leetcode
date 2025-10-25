# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        st = [(root)]

        while st:
            n = st.pop()
            if n:
                if n.val == val:
                    return n
                elif val > n.val:
                    st.append(n.right)
                else:
                    st.append(n.left)
        
       
        