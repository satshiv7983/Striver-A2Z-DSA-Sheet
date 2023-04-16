from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=Counter(arr)
    res=sorted(c.items(),key=lambda x:x[1],reverse=True)
    for x,y in res:
        for j in range(y):
            print(x,end=" ")
    print()
            
