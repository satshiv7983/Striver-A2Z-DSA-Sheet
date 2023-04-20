
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def sort(h1):
    s1=[]
    
    while h1:
        s1.append(h1.data)
        h1=h1.next
    
    
    ll=Llist()
    tail=None
    for e in sorted(s1):
        tail=ll.insert(e,tail)
        
    return ll.head
    
