import model
import random


n =100
beta = -1
map = [[random.choice([-1,1]) for i in range(n)] for j in range(n)]

while(1):
    model.update(map,n,beta)

