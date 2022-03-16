""""
Question:
There are 100 doors, all closed. In a nearby cage are 100 monkeys.

The first monkey is let out, and runs along the doors opening every one.
The second monkey is then let out, and runs along the doors closing the 2nd, 4th, 6th,...all the even-numbered doors.
The third monkey is let out. He attends only to the 3rd, 6th, 9th,... doors (every third door, in other words),
closing any that is open and opening any that is closed, and so on.
After all 100 monkeys have done their work in this way,
what state are the doors in after the last pass?
""""

doors=100
monkeys = 100
state=[]
for door in range(doors+1):
    state.append(False)
for door in range(1,doors+1):
    for monkey in range(1,monkeys + 1):
        if(door*monkey<(doors+1)):
            state[door*monkey]= not state[door*monkey]      #here we are changing the state as like not gate
for index in range(1, len(state)):
    status = state[index]
    if(status==True):
        print(index, state[index])
