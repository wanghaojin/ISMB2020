import random
def init(n):
    map = [[random.choice([-1,1]) for i in range(n)] for j in range(n)]
    return map