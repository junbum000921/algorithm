n=int(input())
dice=list(map(int, input().split()))
sum=0
##각 면의 가운데 면들의 합
sum+=(n-1)**2*min(dice)*5

##위쪽 모서리
##세 면의 합이 최소인거 찾아야됨.
##마주보는 면만 아니면 세개 선택해서 만들 수 있다.
sum_of_3=[
min_of_3=
