l=list(map(int,input().split(" ")))

length=len(l)
index=0
while(index<length-1):
    if(l[index]==0):
        break
    else:    
        index=index+l[index]
    
if(length==index+1):
    print(True)
else:
    print(False)
