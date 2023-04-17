        
class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head):
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        return count
        
