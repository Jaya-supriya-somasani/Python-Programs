#Question
'''
There is a robot named The S21. This robot was designed such that it can move only F steps forward and B steps backward. To check the functionality of the S21 an engineer took it to a ground. He tried to give some instructions to move F steps forward and B steps backward by facing it to East side. The S21 started moving forward and backward. At the end of all these instructions the S21 stayed D distance from the boundary line to the ground at the West side.

Write a program to help this engineer to test S21. You will be given an array of steps, where each step contains string with number and the direction, and face of robot F and distance between robot starting position and boundary line. Your program should return two things.

1. Status if S21 reached boundary line, Y for Yes, N for No. 2. In which direction it stopped. E, W, N, S.

3. For No case, return the distance between boundary line and the S21.

Example:

"input 1"-"E 21 21", (Bot Direction, distance of boundary line in forward direction, distance of boundary in backward direction) "input_2" ["2F 3B",

"4B 6F",

"2F 9B",

"4F 6B",

"2F 6B",

"4B 9B"

"output"-"Y W"
'''

#Solution

input1=input().split(" ")
direction=list(input().split(","))

appending_items=""
for i in range(len(direction)):
    appending_items=appending_items+direction[i]+" "
    
list_of_items=appending_items.split(" ")

sum_of_directions=0
for i in range(len(list_of_items)-1):
    element=list_of_items[i]
    if(element[-1]=='B'):
        sum_of_directions=sum_of_directions-int(element[:-1])
    if(element[-1]=='F'):
        sum_of_directions=sum_of_directions+int(element[:-1])
        
first_boundary=int(input1[1])
second_boundary=int(input1[2])

if(sum_of_directions<0 and -(sum_of_directions)>second_boundary):
    if(input1[0]=='E'):
        print("Y W")
    if(input1[0]=='W'):
        print("Y E")
    if(input1[0]=='N'):
        print("Y S")
    if(input1[0]=='S'):
        print("Y N")
    
if(sum_of_directions<0 and -(sum_of_directions)<second_boundary):
    if(input1[0]=='E'):
        print("W",second_boundary+sum_of_directions)
    if(input1[0]=='W'):
        print("E",second_boundary+sum_of_directions)
    if(input1[0]=='N'):
        print("S",second_boundary+sum_of_directions)
    if(input1[0]=='S'):
        print("N",second_boundary+sum_of_directions)
        
if((sum_of_directions>0 and sum_of_directions>=int(first_boundary)) or sum_of_directions==0):
    if(input1[0]=='E'):
        print("Y E")
    if(input1[0]=='W'):
        print("Y W")
    if(input1[0]=='N'):
        print("Y N")
    if(input1[0]=='S'):
        print("Y S")
        
if(sum_of_directions>0 and sum_of_directions<first_boundary):
    if(input1[0]=='E'):
        print("E",first_boundary-sum_of_directions)
    if(input1[0]=='W'):
        print("W",first_boundary-sum_of_directions)
    if(input1[0]=='N'):
        print("N",first_boundary-sum_of_directions)
    if(input1[0]=='S'):
        print("S",first_boundary-sum_of_directions)
    
