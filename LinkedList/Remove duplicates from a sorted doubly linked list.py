class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        temp=head
        prev=Node(-11)
        while temp:
            if temp.data==prev.data:
                prev.next=temp.next
            else:
                prev=temp
            temp=temp.next
                
        return head
