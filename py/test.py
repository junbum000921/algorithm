def isItInh(arr):
    if len(arr)<3:
        return 0
    else:
        for i in range(len(arr)-2):
            aaa=arr[:3+i]
            if aaa==inh:
                return 1
        return 0

b=[1,1]
inh=[1,1,1]
print(isItInh(b))
