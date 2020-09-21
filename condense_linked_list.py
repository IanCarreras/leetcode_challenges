# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    hashtable = {node.value: 1}
    new_list = ListNode(node.value)
    current = node.next
    new_current = new_list
    
    while current is not None:
        if current.value in hashtable:
            current = current.next
        else:
            hashtable[current.value] = 1
            new_current.next = ListNode(current.value) 
            current = current.next
            new_current = new_current.next
            
    return new_list