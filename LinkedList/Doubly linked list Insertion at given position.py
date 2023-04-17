'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    if not head :
        return Node(data)
    temp=head
    cur=0
    while True:
        if cur==p:
            break
        temp=temp.next
        cur+=1
    node=Node(data) 
    if temp.next is not None:
        node.next=temp.next
        temp.next.prev=node
    temp.next=node
    node.prev=temp
    
    return head
    
