class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        temp=head
        while temp:
            rear=temp
            temp=temp.next
        res=[]
        while head and rear and head.data<rear.data:
            x=head.data+rear.data
            if x==target:
                res.append((head.data,rear.data))
                head=head.next
                rear=rear.prev
            elif x<target:
                head=head.next
            else:
                rear=rear.prev
        return res
