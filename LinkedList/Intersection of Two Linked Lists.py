
class Solution:
    def findIntersection(self, head1, head2):
        head1,head2=head2,head1
        
        hashmap = {}
 
    # traversing on first list
        while(head1 != None):
            data = head1.data
            if(data not in hashmap.keys()):
                hashmap[data] = 1
            head1 = head1.next
     
        # making a new linkedList
        ans = linkedList()
        while(head2 != None):
            data = head2.data
            if(data in hashmap.keys()):
                # adding data to new list
                ans.insert(data)
            head2 = head2.next
        return ans.head
            
