"""
Restate:
    Reverse a linked list so that the head is the now the tail, and the tail is now the head and all elements are reversed.
Assumations:
    Not Broken
"""
def reverse(head):
    previous = None
    current = head
    
    while current is not None:
        next_ptr = current.next
        current.next = current
        previous = current
        current = next_ptr
    # swap final node
    head = previous
        
    # return the new head(the actual tail)
    return head

