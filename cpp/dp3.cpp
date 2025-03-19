#include <stdio.h>

int min(int a, int b, int c){
    if(a<b){
        if(a<c) return a;
        else return c;
    }
    else{
        if(b<c) return b;
        else return c;
    }
}
int min(int a, int b){
    if(a<b){
        return a;
    }
    else{
        return b;
    }
}

int main(void){
    int n;
    scanf("%d", &n);
    int house[n][3];
    for(int i=0; i<n; i++){
        scanf("%d %d %d", &house[i][0], &house[i][1], &house[i][2]);
    }
    int dp[1001][3] = {0,};
    for(int i=0; i<=n; i++){
        dp[i][0]=min(dp[i-1][1]+house[i][0], dp[i-1][2]+house[i][0]);
        dp[i][1]=min(dp[i-1][0]+house[i][1], dp[i-1][2]+house[i][1]);
        dp[i][2]=min(dp[i-1][0]+house[i][2], dp[i-1][1]+house[i][2]);
    }
    printf("%d\n", min(dp[n][0], dp[n][1], dp[n][2]));
    return 0;
}