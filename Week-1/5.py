string=input()
sort_string = sorted(string)
l=[]
o=[]
s=[]
e=[]
if(string.isalnum()==True):
    for i in sort_string:
        if(i.isalpha()):
            if i.isupper():
                l.append(i)
            else:
                s.append(i)

        if i.isdigit():
            if(int(i)%2==0):
                e.append(i)
            else:
                o.append(i)
print("".join(s+l+o+e))

            

    
