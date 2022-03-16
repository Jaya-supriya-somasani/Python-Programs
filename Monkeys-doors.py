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

n=100
l=[]
for i in range(n+1):
    l.append(False)
for i in range(1,n+1):
    for j in range(1,101):
        if(i*j<101):
            if(l[i*j]==False):
                l[i*j]=True
            else:
                l[i*j]=False
for i in range(1,len(l)):
    if(l[i]==True):
        print(i,l[i])
