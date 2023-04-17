
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteNode(self,head, x):
        if x is 1:
            head=head.next
            head.prev=None
            return
        cur=1
        temp=head
        while True:
            if cur==x:
                break
            prev=temp
            temp=temp.next
            cur+=1
        if temp.next:
            prev.next=temp.next
            temp.next.prev=prev
        else:
            prev.next=None
            
        return head
        
