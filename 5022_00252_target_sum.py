''''
Write a function that takes in a non-empty array of distinct integers and an integer
representing a target sum. If any two numbers in the input array sum up to the
target sum, the function should return them in an array, in any order. If no two
numbers sum up to the target sum, the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in
the array; you can't add a single integer to itself in order to obtain the target sum.
You can assume that there will be at most one pair of numbers summing up to the
target sum.

Sample Input:
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

Sample Output:
[-1, 11]
'''

array=list(map(int,input().split(" ")))
target_sum=int(input())
c=0
for array_indx in range(len(array)):
    for next_indx in range(array_indx+1,len(array)):
        if((array[array_indx]+array[next_indx])==target_sum):
            print("Target Sum Elements : ",array[array_indx],array[next_indx])
            c=c+1
if(c==0):
    print([])
            
