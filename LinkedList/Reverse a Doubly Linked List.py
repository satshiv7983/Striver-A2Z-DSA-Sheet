'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

def reverseDLL(head):
    dummy=Node(0)
    dummy.prev=head
    temp=head
    prev=dummy
    while head:
        temp=head.next
        head.next=prev
        head.prev=temp
        prev=head
        head=temp
    dummy.prev.next=None
    return prev
