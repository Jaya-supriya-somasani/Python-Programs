'''
Santa came to office to gift employees with some rewards. He came with boxes which contains balls where each ball labelled number on it. i.e each ball contains some number on it. 
He gave one box to each employee. A box can contain balls and another box inside it and so on.
Reward point calculation as follows. 
   1. Reward points will be the sum of each number written on each ball.
   2. If box contain another box, sum will be calculated for inside box and multiplied with depth of it (refer example for clear understanding).
         First box, let's say B, will be having depth of 1. If B contains another box B1, B2 then depth of B1 and B2 will be 2. If B1 contains another box, let's  say B11, then depth of B11 will be 3 and so on.
         Therefore, depth of [x, y] is x + y;  the sum of [x, [y, z]] is x + 2* (y+z); the sum of [x, [y,[z]]] is x + 2* (y+3z);
   3. It will be added to total sum.
Write a function which accepts gift box as an input array and returns sum of reward points.
Example - 
Numbers in gift box - 
         [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Output - 12 // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
'''

def evaluation(elements,depth):
    sum_of_elements=0
    for i in elements:
        if isinstance(i,list):
            sum_of_elements=sum_of_elements+evaluation(i,depth+1)
        else:
            sum_of_elements=sum_of_elements+i
    return sum_of_elements*depth
elements=[5,2,[7,-1],3,[6,[-13,8],4]]
result=evaluation(elements,1)
print(result)
