import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr=list(map(int,input().split()))
wood=0
start=0
end=max(arr)

while wood>=m:
    mid=(end+start)//2
    wood=0
    for i in arr:
        if i<mid:
            wood+=i
        else:
            wood+=(i-mid)

