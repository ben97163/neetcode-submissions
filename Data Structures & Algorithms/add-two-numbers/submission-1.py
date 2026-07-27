# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        cur = head
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            cur.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            cur = cur.next
            
        while l1.next:
            l1 = l1.next
            cur.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            cur = cur.next
        while l2.next:
            l2 = l2.next
            cur.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            cur = cur.next
        
        if carry:
            cur.next = ListNode(1)
        
        return head
