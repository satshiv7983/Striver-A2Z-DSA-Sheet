'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        dummy=Node(0)
        prev=dummy
        for i in arr:
            temp=Node(i)
            prev.next=temp
            temp.prev=prev
            prev=temp
        return dummy.next
