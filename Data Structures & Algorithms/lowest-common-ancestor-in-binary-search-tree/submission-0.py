# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        sol = root

        while sol:
            if p.val>sol.val and q.val>sol.val:
                sol = sol.right
            if p.val<sol.val and q.val<sol.val:
                sol = sol.left
            else:
                return sol
