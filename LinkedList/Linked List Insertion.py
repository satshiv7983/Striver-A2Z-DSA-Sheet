'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        temp=Node(x)
        temp.next=head
        head=temp
        return head
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        if not head:
            return Node(x)
        temp=head
        while temp:
            prev=temp
            temp=temp.next
        prev.next=Node(x)
        return head
            
