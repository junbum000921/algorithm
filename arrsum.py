import sys
input=sys.stdin.readline

def prefix_sum(n):
    prefixSum = [0]*n 
    prefixSum[0] = arr[0] 
    for i in range(1,n): 
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum

n,m=map(int,input().split())
max_sum=float('-inf')
arr=list(map(int,input().split()))
prefixSum = prefix_sum(n)

for _ in range(m):
    current_sum=
    if current_sum>max_sum:
        max_sum=current_sum

print(max_sum)
