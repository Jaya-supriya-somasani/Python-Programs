""" Series: 1, 4, 10, 22, 46 ....

Write a program to print the given position element?

Eg: input = 6
output = 94 """

indexes=int(input())
current_value=1
next_value=4
sequence=[]
sequence.append(current_value)
sequence.append(next_value)
for index in range(2,indexes+1):
    difference=((next_value-current_value)*2)
    current_value=next_value
    next_value=next_value+difference
    sequence.append(next_value)
print(sequence)
