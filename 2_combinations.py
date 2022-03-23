def combinations(arr,s):
    res=[]
    temp=[]
    arr=sorted(list(set(arr)))
    findingCombo(arr,res,temp,s,0)
    return res
def findingCombo(arr,res,temp,s,ind):
    if(s==0):
        res.append(list(temp))
        return
    for i in range(ind,len(arr)):
        if(s-arr[i]>=0):
            temp.append(arr[i])
            findingCombo(arr,res,temp,s-arr[i],i)
            temp.remove(arr[i])
arr=list(map(int,input().split()))
s=int(input())
res=combinations(arr,s)
print(res)
