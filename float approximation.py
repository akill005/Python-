#floats and approximation
#it is for binary conversion in float 

#fractional num binary conversion
x=0.625
p=0
while ((2**p)*x)%1!=0:
    print('rem=',str((2**p)*x - int((2**p)*x)))
    p+=1
num=int((2**p)*x)
result=''
if num==0:
    result='0'
while (num>0):
    result=str(num%2) + result
    num//=2
for i in range (p - len(result)):
    result='0' + result
result=result[0:-p] + '.' + result[:]
print("binary of 0.625  is",str(x),'is', str(result))


   
#guess and check for square root with approximation
x=54321
epsilon=0.01
inc=0.0001
g=0.0
gcount=0
while(abs(g**2 - x)>=epsilon) and (g**2 <=x):
    g+=inc
    gcount+=1
print('guess count',gcount)
if(abs(g**2-x)>=epsilon):
    print('failed to find')
    print('last guess was',g)
else:
    print('guess is close to',g)
#for getting still closer value we should increase the guessing decimal but it is very slow    
            