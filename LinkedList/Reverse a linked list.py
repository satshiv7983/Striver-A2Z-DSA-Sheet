"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        prev=None
        temp=head
        while temp:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev
            
