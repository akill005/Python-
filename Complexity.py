# Complexity


# constant o(1)

def mul1(a,b):
    return a*b


# linear
    e in l
    subset of list
    l1==l2
    del(l[0'])    
        
def mul(x,y):          #O(y) for y and O(1) for x
    tot=0
    for i in range (y):
        tot+=x
    return tot

# recursion - linear

# polynomial complexity - o(n^2)

# exponential complexity - fib recursive


# subsets of list [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]
def gen(l):
    if len(l)==0:
        return [[]]
    extra=l[-1:]
    smaller=gen(l[:-1])
    new=[]
    for i in smaller:
        new.append(i+extra)
    return new+smaller
print((gen([1,2,3])))

#linear search
def lin(l,e):
    found=False
    for i in range len(l):
        if e==l[i]:
            found=True
    return found



