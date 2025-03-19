s=input()
s_int=[]
max_len=0
if len(s)==1:
    print("0")
else:
    for c in s:
        s_int.append(int(c))
    if sum(s_int)/2==sum(s_int[0:(len(s_int)//2)]):
        print(len(s))
    else:
        for length in range(2, len(s)+1, 2):
            for start in range(len(s)-length+1):
                mid = start + length//2
                left_sum=sum(map(int, s[start:mid]))
                right_sum=sum(map(int, s[mid:start + length]))
                if left_sum==right_sum:
                    max_len=max(max_len, length)
        print(max_len)
