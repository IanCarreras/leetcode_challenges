# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        curr = head
        r = 0
        
        while l1 or l2 or r:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            result = v1 + v2 + r
            if result > 9:
                r = 1
                result = result - 10
            else: 
                r = 0
                
            curr.next = ListNode(result)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next