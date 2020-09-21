# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        current_l1= l1
        current_l2 = l2
        current_l3 = l3
        remainder = 0
        hashtable = {}
        
        if l1.next is None and l2.next is None:
            l3.val = l1.val + l2.val
            if l3.val > 9:
                l3.val = l3.val - 10
                l3.next = ListNode(1)
        
        k = 0
        while current_l1 is not None:
            hashtable[k] = current_l1.val
            current_l1 = current_l1.next
            k += 1
            
        k = 0
        while current_l2 is not None:
            if hashtable[k]:
                hashtable[k] += current_l2.val + remainder
            else:
                hashtable[k] = current_l2.val + remainder
                
            if hashtable[k] > 9:
                hashtable[k] = hashtable[k] - 10
                remainder = 1
            else:
                remainder = 0
            current_l2 = current_l2.next
            k += 1
            
        print(hashtable)
            
        return l3