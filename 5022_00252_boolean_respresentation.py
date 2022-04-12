'''
Question: Function that takes in an array of integers and returns a boolean representing
whether the array is monotonic.
An array is said to be monotonic if its elements, from left to right, are entirely nonincreasing or entirely non-decreasing.
Non-increasing elements aren't necessarily exclusively decreasing; they simply don't
increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they
simply don't decrease.
Note that empty arrays and arrays of one element are monotonic.

Sample Input:
array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

Sample Output:True

'''

array=list(map(int,input().split(" ")))
sorted_array=sorted(array)
reverse_array=sorted(array,reverse=True)
if(array==sorted_array or array==reverse_array):
    print(True)
else:
    print(False)
