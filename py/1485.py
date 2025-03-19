T=int(input())
for _ in range(T):
    #마주보는 변은 x값기준으로 정렬했을때 1,2번에 있음.
    arr=[]
    for _ in range(4):
        arr.append(list(map(int,input().split())))
    arr.sort()
    n1=(arr[1][0]-arr[2][0])**2+(arr[1][1]-arr[2][1])**2
    n2=(arr[0][0]-arr[3][0])**2+(arr[0][1]-arr[3][1])**2
    n3=(arr[0][0]-arr[1][0])**2+(arr[0][1]-arr[1][1])**2
    n4=(arr[1][0]-arr[2][0])**2+(arr[1][1]-arr[2][1])**2
    if n1==n2:
        if n3==n4:
            print("1")
        else:
            print("0")
    else:
        print("0")
    
