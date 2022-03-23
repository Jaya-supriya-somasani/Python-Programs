'''
Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order).

If the input array is already sorted, the function should return [-1, -1].
'''

array=list(map(int,input().split(" ")))
sorted_array=[]
for i in range(len(array)):
    sorted_array.append(array[i])
sorted_array.sort()
indexes=[]
if(array!=sorted_array):
    for i in range(len(array)):
        if(array[i]!=sorted_array[i]):
            indexes.append(i)
    print(indexes[0],indexes[-1])
if(array==sorted_array):
    print(-1,-1)