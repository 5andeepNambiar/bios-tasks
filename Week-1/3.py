n=list(map(int,input().split()))
flag=0
for i in n:
    if (i>0):
        s=str(i)
        if (s==s[::-1]):
            flag=1
    else:
        print("False")
        exit()
        
if(flag):
    print("True")
else:
    print("False")