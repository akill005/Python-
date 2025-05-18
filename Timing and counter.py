#Timing programs  
import time
import dateutil
def c2f(c):
    return c*9.0/5 + 32

def mysum(w):
    tot=1
    for i in range (2,w+1):
        tot+=i
    return tot

def square(n):
    sq=0
    for i in range(n):
        for j in range(n):
            sq+=1
    return sq

def timey(f,l):
    print('Timing',f.__name__)
    for i in l:
        t=time.time()
        f(i)
        dt=time.time()-t
        print(f'{f.__name__}({i}) took {dt} sec')
    
l=[1]
for i in range(5):
    l.append(l[-1]*10)

timey(c2f,l)        
timey(mysum,l)  
        
 #counting
def c2f(c):
    counter=3
    return (counter,c*9.0/5 + 32)

def mysum(w):
    counter=1
    tot=1
    for i in range (2,w+1):
        counter+=3
        tot+=i
    return (counter,tot)

def square(n):
    counter=1
    sq=0
    for i in range(n):
        counter+=1
        for j in range(n):
            counter+=3
            sq+=1
    return (counter,sq)  
def count_wrap(f,l):
    print('Counting',f.__name__)
    for i in l:
        counter=f(i)[0]
        if i==min(l):
            mul=1.0
        else:
            mul=counter/float(prev)
        prev=counter
        print((f"{f.__name__}({i}):{counter} ops,{mul} x more"))
count_wrap(c2f, l)
count_wrap(mysum, l)    
count_wrap(square,l)

        
        