##이항계수
n,m=map(int,input().split())
dp=[[0]*1001 for _ in range(1001)]
dp[0][0]=1
for i in range(1,1001):
    dp[i][0]=1
    dp[i][i]=1
    for j in range(1,i):
        dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
print(dp[n][m]%10007)