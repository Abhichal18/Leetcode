# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,ans):
        # checking if root is none or not
        if root==None:
            return ans
        # appending the value into ans
        ans.append(root.val)
        # doing the same for left and right child
        ans=self.preorder(root.left,ans)
        ans=self.preorder(root.right,ans)
        return ans
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=self.preorder(root,[])
        return ans
