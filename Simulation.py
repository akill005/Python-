#simulation
import random
import matplotlib.pyplot as plt
def prob(side):
    dice=['.',':',':.','::','::.',':::']
    sim=10000
    count=0
    for i in range(sim):
        roll=random.choice(dice)
        if roll==side:
            count+=1
    print(count,count/sim)
prob('.')
prob('::.')



def probd(n,at):
    dice=['.',':',':.','::','::.',':::']
    sim=10000
    how=[]
    count=0
    for i in range(sim):
        matched=0
        for i in range(n):
            
            roll=random.choice(dice)
            if roll=='::':
                matched+=1
        how.append(matched)
    for i in how:
        if i>=at:
            count+=1
    print(count,count/sim)
probd(7,3)
probd(1,1)



def fill(size):
    rate=[]
    time=[]
    npt=10000
    for i in range(npt):
        r=1+2*random.random()
        rate.append(r)
        time.append(size/r)
    print('avg flow',sum(rate)/len(rate))
    print('avg time',sum(time)/len(time))
    plt.figure()
    plt.scatter(range(npt),rate,s=1)
    plt.figure()
    plt.scatter(range (npt),time,s=1)
    plt.show()
fill(600)
























