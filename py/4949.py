while True:
    s=input()
    flag=0
    if s==".":
        break
    else:
        arr=[]
        for c in s:
            if c=='[' or c=='(':
                arr.append(c)
            elif c==']':
                if len(arr)!=0 and arr[-1]=='[':
                    arr.pop()
                else:
                    flag=1
                    break
            elif c==')':
                if len(arr)!=0 and arr[-1]=='(':
                    arr.pop()
                else:
                    flag=1
                    break
        if len(arr)>0:
            flag=1
        if flag==0:
            print("yes")
        else:
            print("no")
