def nums(arr,n):
    greater_elements=[]
    for first_ele in range(0,n):
        greater=-1
        second_ele= first_ele + 1
        
        if(second_ele== n):
            second_ele= 0
            
        while(second_ele!=first_ele):
            if(second_ele== n):
                second_ele= 0
                
            if(first_ele== 0 and second_ele== n - 1):
                break
            
            if(arr[second_ele] > arr[first_ele]):
                greater= 1
                greater_elements.append(arr[second_ele])
                break
            second_ele+=1
            
        if(greater==-1):
            greater_elements.append(-1)
    return greater_elements
arr=list(map(int,input().split(",")))
elements=nums(arr,len(arr))
print(elements)
