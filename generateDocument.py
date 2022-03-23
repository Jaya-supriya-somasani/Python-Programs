c=list(input())
d=list(input())
count=0
def removing(ele):
    c.remove(ele)
    return c
for i in range(0,len(d)):
    for j in range(0,len(c)):
        if(c[j]==d[i]):
            removing(d[i])
            count=count+1
            break
if(len(d)==count):
    print(True)
else:
    print(False)
