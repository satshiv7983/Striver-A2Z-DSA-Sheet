'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        dummy=Node(0)
        prev=dummy
        temp=head
        while temp:
            if temp.data==x:
                temp=temp.next
            else:
                prev.next=temp
                temp.prev=prev
                prev=temp
                temp=temp.next
        prev.next=temp
        return dummy.next
        
