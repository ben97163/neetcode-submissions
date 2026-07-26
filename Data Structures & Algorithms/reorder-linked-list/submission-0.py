# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        count = 0
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
            count += 1
        
        cur = head
        
        for i in range(count // 2):
            temp = cur.next
            cur.next = stack.pop()
            cur.next.next = temp
            cur = cur.next.next
        
        cur.next = None

        return 
        