
# Following is the structure of node 
class Node:
    def __init__(self):  
        self.data = None
        self.next = None

class Solution:
    def divide(self, N, head):
        end = head
        prev = None
        curr = head
      
        # Get pointer to last Node 
        while (end.next != None):
            end = end.next
      
        new_end = end
      
        # Consider all odd nodes before getting first even node
        while (curr.data % 2 !=0 and curr != end):
              
            new_end.next = curr
            curr = curr.next
            new_end.next.next = None
            new_end = new_end.next
              
        # do following steps only if there is an even node
        if (curr.data % 2 == 0):
              
            head = curr
      
            # now curr points to first even node
            while (curr != end):
                  
                if (curr.data % 2 == 0):
                      
                    prev = curr
                    curr = curr.next
                      
                else:
                      
                    # Break the link between prev and curr
                    prev.next = curr.next
      
                    # Make next of curr as None 
                    curr.next = None
      
                    # Move curr to end 
                    new_end.next = curr
      
                    # Make curr as new end of list 
                    new_end = curr
      
                    # Update curr pointer 
                    curr = prev.next
                  
        # We have to set prev before executing rest of this code 
        else:
            prev = curr
      
        if (new_end != end and end.data % 2 != 0):
              
            prev.next = end.next
            end.next = None
            new_end.next = end
        return head
