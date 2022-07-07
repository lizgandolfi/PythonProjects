'''
Tim is performing an experiment by choosing lottery numbers.  The numbers range from 1 – 60.  
Time will draw a ball, replace it, and then draw again.  He will do this six times. 
Show the results of Tim's draws.  What is the average of Tim's draws?

'''


import random

draw1 = (random.randint(-100,100))
draw2 = (random.randint(-100,100))
draw3 = (random.randint(-100,100))
draw4 = (random.randint(-100,100))
draw5 = (random.randint(-100,100))
draw6 = (random.randint(-100,100))

avg = (draw1 + draw2 + draw3 + draw4 + draw5 + draw6)/6

print('Draw 1:', draw1)
print('Draw 2:', draw2)
print('Draw 3:', draw3)
print('Draw 4:', draw4)
print('Draw 5:', draw5)
print('Draw 6:', draw6)
print('Average:', avg)



