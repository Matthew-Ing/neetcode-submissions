# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sol = dummy

        lp = dummy
        rp = head

        while n>0 and rp:
            rp = rp.next
            n-=1

        while rp:
            lp = lp.next
            rp = rp.next

        lp.next = lp.next.next

        return dummy.next