# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def check(self,p,q):
        # checking if both root are None
        if p==None and q==None:
            return True
        # if any one root is None then tree is not similar
        elif p==None or q==None:
            return False
        # if value is same check for childs
        if p.val==q.val:
            return self.check(p.left,q.left) and self.check(p.right,q.right)
        else:
            return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p,q)
