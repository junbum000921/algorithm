T=int(input())
def getnear(a):
    start=0
    end=len(arr2)
    while True:
        mid=(start+end)//2
        if a>=arr2[mid]:
            start=mid
        else:
            end=mid
        if start==end:
            return arr2[mid]


for _ in range(T):
    n,m=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr3=[]
    arr2.sort()
    for comp in arr1:
        sum+=getnear(comp)
    print(sum)
