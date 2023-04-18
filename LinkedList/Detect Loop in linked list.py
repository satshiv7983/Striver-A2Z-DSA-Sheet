'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        slow=head
        fast=head.next
        while fast and fast.next:
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False
            
