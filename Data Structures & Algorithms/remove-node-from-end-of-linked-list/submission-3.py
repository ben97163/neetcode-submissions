# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = dum = cur = ListNode(-1, head)
        for i in range(n):
            cur = cur.next
        

        
        while cur.next:
            cur = cur.next
            dum = dum.next
        
        dum.next = dum.next.next

        return dummy.next