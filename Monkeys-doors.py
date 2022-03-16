n=100
l=[]
for i in range(n+1):
    l.append(False)
for i in range(1,n+1):
    for j in range(1,101):
        if(i*j<101):
            if(l[i*j]==False):
                l[i*j]=True
            else:
                l[i*j]=False
for i in range(1,len(l)):
    if(l[i]==True):
        print(i,l[i])
