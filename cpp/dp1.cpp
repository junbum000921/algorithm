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

int main(){
    int n;
    scanf("%d", &n);
    int dp[1001] = {0,};
    for(int i=1; i<=n; i++){
        dp[i]=min(dp[i-1]+1, dp[i/2]+1, dp[i/3]+1);
    }
    printf("%d\n", dp[n]);
    return 0;
}