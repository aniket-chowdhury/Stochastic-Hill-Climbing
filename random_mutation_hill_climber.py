import random
from copy import deepcopy

def onemax(l):
    return sum(l)

def random_bits(num):
    return [random.randint(0,1) for i in range(num)]
def random_neighbour(l):
    # k=deepcopy(l)
    k=l
    global c

    random_position=random.randint(0,len(l)-1)
    c.append(random_position)
    
    if(k[random_position]==0):
        k[random_position]=1
    return k

def hill_climb(iterations,num_bits):
    best={}
    l=random_bits(num_bits)
    for i in range(iterations):
        d={}
        d['list']=random_neighbour(l)
        d['cost']=onemax(l)

        try:
            if(d['cost']>best['cost']):
                l=d['list']
                best=d
        except:
            best=d
            l=best['list']
        # print("".join([str(i)for i in d['list']]),best['cost'])
        if(best['cost']==num_bits): break
    return best

iterations = 1000

for i in range(1,7):
    c=[]
    print(hill_climb(1000,2**i)['cost'],end=' ')
    print('\tChanged bits =',len(c))
    # print()
