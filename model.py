import random
import math
def rand(p):
    random = random.uniform(0,1)
    if random <= p:
        return 1
    else:
        return -1
    
def eval(x,y,map,n,beta):
    upward = 0 if y==0 else map[x][y-1]
    rightward = 0 if x == n-1 else map[x+1][y]
    downward = 0 if y == n -1 else map[x][y+1]
    lefyward = 0 if x==0 else map[x-1][y]
    sum = lefyward + upward + rightward + downward
    probability = 1 / (math.exp(-2*beta * sum))
    return rand(probability)
def update():
    pass