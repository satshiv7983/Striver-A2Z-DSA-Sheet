class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        arr=[]
        temp=head
        while temp:
            arr.append(temp.data)
            temp=temp.next
        n=len(arr)
        left,mid,high=0,0,n-1
        while mid<=high:
            if arr[mid]==2:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
            elif arr[mid]==0:
                arr[mid],arr[left]=arr[left],arr[mid]
                left+=1
                mid+=1
            else:
                mid+=1
        dummy=Node(0)
        prev=dummy
        for i in arr:
            temp=Node(i)
            prev.next=temp
            prev=temp
        return dummy.next
                
