a,b,c=map(int,input().split())
def recursive_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = recursive_power(a, n // 2)
        return half_power * half_power
    else:
        half_power = recursive_power(a, (n-1) // 2)
        return half_power * half_power * a
print(recursive_power(a,b)%c)
