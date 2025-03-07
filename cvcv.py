net="()[]"
while True:
    s=input()
    ans="yes"
    cnt=0
    if s==".":
        break
    else:
        check=[]
        for i in range(len(s)):
            if s[i]=='(':
                check.append(s[i])
            elif s[i]=='[':
                check.append(s[i])
            elif s[i]==')':
                if check[-1]=='(':
                    check.pop()
                else:
                    cnt+=1
            elif s[i]==']':
                if check[-1]=='[':
                    check.pop()
                else:
                    cnt+=1
        if cnt!=0:
            ans="no"
        print(ans)
            
            
        
            
            
        
        
