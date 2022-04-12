'''
ou're given an array of integers and an integer. Write a function that
moves all instances of that integer in the array to the end of the array
and returns the array.
The function should perform this in place (i.e., it should mutate the
input array) and doesn't need to maintain the order of the other
integers.

Sample Input:
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

Sample output:
[1, 3, 4, 2, 2, 2, 2, 2]
'''


input_array=list(map(int,input().split(" ")))
toMove=int(input())
to_move_array=[]
for inp_arr_ele in range(len(input_array)):
    if(input_array[inp_arr_ele]==toMove):
        to_move_array.append(input_array[inp_arr_ele])

        #making particular index element to null when that element is equal to to move element
        input_array[inp_arr_ele]=''
        
final_array=[]
for ele_of_inp_array in range(len(input_array)):
    if(input_array[ele_of_inp_array]!=''):
        #appending elements into final array which are not null in the input array
        final_array.append(input_array[ele_of_inp_array])

#concatenating integer arrays and to move array        
print(final_array+to_move_array)
