'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    if k==1:
        return head.next
    temp=head
    t=1
    while True:
        if t==k:
            break
        t+=1
        prev=temp
        temp=temp.next
    prev.next=temp.next
    return head
    
