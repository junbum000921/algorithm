from collections import deque
T=int(input())
for _ in range(T):
    cnt=0
    n,track=map(int,input().split())
    arr=deque(map(int,input().split()))
    track_arr=deque()
    for i in range(n):
        track_arr.append(i)
    while len(arr)>0:
        top_arr=max(arr)
        if arr[0]==top_arr:
            arr.popleft()
            check=track_arr.popleft()
            cnt+=1
            if check==track:
                print(cnt)
        else:
            arr.append(arr.popleft())
            track_arr.append(track_arr.popleft())
        
    

