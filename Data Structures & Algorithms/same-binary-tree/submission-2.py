# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs

        queuep = deque([p])
        queueq = deque([q])

        while queuep and queueq:
            for _ in range(len(queuep)):
                nodep = queuep.popleft()
                nodeq = queueq.popleft()

                if nodep is None and nodeq is None:
                    continue
                if nodep is None or nodeq is None or nodep.val!=nodeq.val:
                    return False
                queuep.append(nodep.left)
                queuep.append(nodep.right)
                queueq.append(nodeq.left)
                queueq.append(nodeq.right)

        return True



        