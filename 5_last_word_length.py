string=list(input().split(" "))
list_of_items=[]
for i in string:
    a=i.replace(" ","")
    list_of_items.append(a)
print(list_of_items)
for i in range(len(list_of_items)-1,-1,-1):
    if(len(list_of_items[i])>=1):
        print(list_of_items[i])
        break

