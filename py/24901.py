n=int(input())
str=""
for i in range(n+1):
    b=bin(i)
    str+=b[2:]
print(str)
