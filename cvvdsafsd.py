arr=[]
a=0
cnt=0
index=0
for i in range(3):
    s=input()
    if s != "Fizz" and s != "Buzz" and s!= "FizzBuzz":
        a=int(s)
        index=i
current=a+3-index
if current%15==0:
    print("FizzBuzz")
elif current%3==0:
    print("Fizz")
elif current%5==0:
    print("Buzz")
else:
    print(current)
