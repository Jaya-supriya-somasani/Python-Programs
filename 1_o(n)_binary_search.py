elements=list(map(int,input().split(" ")))
target=int(input())
elements.sort()
list_of_items=[]
for i in range(len(elements)):
    if(elements[i]==target):
       list_of_items.append(i)
if(len(list_of_items)==0):
    print(-1,-1)

else:
    print([list_of_items[0],list_of_items[-1]])
