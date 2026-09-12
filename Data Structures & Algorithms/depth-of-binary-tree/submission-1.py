# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def mD(rt, depth: int) -> int:
            if rt is None:
                return 0
            
            return(1+ max(mD(rt.left, depth), mD(rt.right, depth)))
        return (mD(root, 0))